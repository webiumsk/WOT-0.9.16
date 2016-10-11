# 2016.10.11 22:10:01 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/veh_comparison_basket.py
from collections import namedtuple
import Event
from adisp import process
from debug_utils import LOG_WARNING, LOG_DEBUG, LOG_ERROR
from gui import SystemMessages
from gui.LobbyContext import g_lobbyContext
from gui.SystemMessages import SM_TYPE
from gui.game_control.controllers import Controller
from gui.shared.ItemsCache import g_itemsCache, CACHE_SYNC_REASON
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.processors.module import PreviewVehicleModuleInstaller
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from items import getTypeOfCompactDescr, ITEM_TYPE_NAMES
MAX_VEHICLES_TO_COMPARE_COUNT = 20
_ChangedData = namedtuple('_ChangedData', ('addedIDXs', 'addedCDs', 'removedIDXs', 'removedCDs', 'isFullChanged'))
_COMPARE_INVALID_CRITERIA = ~REQ_CRITERIA.VEHICLE.EVENT_BATTLE | ~REQ_CRITERIA.SECRET

def getVehicleCriteriaForComparing():
    return _COMPARE_INVALID_CRITERIA


def isValidVehicleForComparing(vehicle):
    validCriteria = getVehicleCriteriaForComparing()
    return validCriteria(vehicle)


def _makeStrCD(vehicle):
    return vehicle.descriptor.makeCompactDescr()


def getSuitableChassis(vehicle):
    """
    :param vehicle: instance of vehicle
    :return: list of chassis that is not installed and fit provided vehicle
    """
    chassis = []
    for _, _, nodeCD, _ in vehicle.getUnlocksDescrs():
        itemTypeID = getTypeOfCompactDescr(nodeCD)
        if itemTypeID == GUI_ITEM_TYPE.CHASSIS:
            chassisCand = g_itemsCache.items.getItemByCD(nodeCD)
            if chassisCand.mayInstall(vehicle) and not chassisCand.isInstalled(vehicle):
                chassis.append(chassisCand)

    return chassis


def getInstalledModulesCDs(vehicle):
    """
    :param vehicle: instance of vehicle which modules have to be collected
    :return: compact descriptors list of modules currently installed on provided vehicle
    """
    outcome = []
    raise vehicle or AssertionError('Instance of vehicle must be not None!')
    for guiItemType in GUI_ITEM_TYPE.VEHICLE_MODULES:
        if guiItemType == GUI_ITEM_TYPE.TURRET and not vehicle.hasTurrets:
            outcome.append(None)
        else:
            cmp = vehicle.descriptor.getComponentsByType(ITEM_TYPE_NAMES[guiItemType])
            outcome.append(cmp[0]['compactDescr'])

    return outcome


class CREW_TYPES(object):
    SKILL_100 = 100
    SKILL_75 = 75
    SKILL_50 = 50
    CURRENT = -1
    ALL = (SKILL_100,
     SKILL_75,
     SKILL_50,
     CURRENT)


class MODULES_TYPES(object):
    BASIC = 'basic'
    CURRENT = 'current'
    CUSTOM = 'custom'


class _VehCompareData(object):

    def __init__(self, vehicleCD):
        super(_VehCompareData, self).__init__()
        self.__isActualModules = True
        self.__isInInventory = False
        self.__invVehStrCD = None
        self.__vehicleCD = vehicleCD
        self.initVehicle()
        self.__stockVehStrCD = _makeStrCD(self._getStockVehicle(self.__vehicleCD))
        if self.__isInInventory:
            self.__crewLvl = CREW_TYPES.CURRENT
        else:
            self.__crewLvl = CREW_TYPES.SKILL_100
        self.__strCD = self.__invVehStrCD if self.__isInInventory else self.__stockVehStrCD
        return

    def initVehicle(self):
        vehicle = self._getVehicle(self.__vehicleCD)
        self.__isActualModules = True
        self.__isInInventory = vehicle.isInInventory
        if self.__isInInventory:
            cloneVeh = self.__fitVehicle(vehicle.strCD)
            self.__invVehStrCD = _makeStrCD(cloneVeh)
        else:
            self.__invVehStrCD = None
        return

    def setCrewLevel(self, crewLvl):
        raise crewLvl in CREW_TYPES.ALL or AssertionError('Unsupported crew level type!')
        self.__crewLvl = crewLvl

    def getVehicleCD(self):
        return self.__vehicleCD

    def setVehicleStrCD(self, strCD):
        self.__strCD = strCD

    def getVehicleStrCD(self):
        return self.__strCD

    def getModulesType(self, strCD = None):
        strCD = strCD or self.__strCD
        if strCD == self.__invVehStrCD:
            return MODULES_TYPES.CURRENT
        elif strCD == self.__stockVehStrCD:
            return MODULES_TYPES.BASIC
        else:
            return MODULES_TYPES.CUSTOM

    def getInvVehStrCD(self):
        return self.__invVehStrCD

    def getStockVehStrCD(self):
        return self.__stockVehStrCD

    def isInInventory(self):
        return self.__isInInventory

    def getCrewLevel(self):
        return self.__crewLvl

    def isActualModules(self):
        return self.__isActualModules

    def clone(self):
        """
        Create copy of current object
        :return: _VehCompareData object which is copy of current
        """
        dataClone = _VehCompareData(self.getVehicleCD())
        dataClone.setCrewLevel(self.getCrewLevel())
        dataClone.setVehicleStrCD(self.getVehicleStrCD())
        return dataClone

    def _getVehicle(self, intCD):
        vehicle = g_itemsCache.items.getItemByCD(intCD)
        raise vehicle.itemTypeID == GUI_ITEM_TYPE.VEHICLE or AssertionError
        return vehicle

    def _getStockVehicle(self, intCD):
        vehicle = g_itemsCache.items.getStockVehicle(intCD)
        raise vehicle.itemTypeID == GUI_ITEM_TYPE.VEHICLE or AssertionError
        return vehicle

    def __fitVehicle(self, strCD):
        """
        WOTD-69910. Optional devices are not participated in the vehicles comparing functionality.
        But some of optional devices may influence on vehicle parameters such as allowed weight.
        In case of detecting such devices it have to be removed from vehicle
        but suitable chassis have to be installed instead.
        :param strCD: string vehicle compact descriptor
        :return: clone of vehicle without any optional devices but installed suitable chassis
        """
        cloneVehicle = Vehicle(strCD, typeCompDescr=self.__vehicleCD)
        vehDescriptor = cloneVehicle.descriptor
        for i, optDevice in enumerate(vehDescriptor.optionalDevices):
            if optDevice is not None:
                success, reason = vehDescriptor.mayRemoveOptionalDevice(i)
                if not success:
                    if reason == 'too heavy':
                        suitableChassis = getSuitableChassis(cloneVehicle)
                        for chassis in suitableChassis:
                            chSuccess, chReason = chassis.mayInstall(cloneVehicle)
                            if chSuccess:
                                self.__installModule(cloneVehicle, chassis)
                                success, reason = vehDescriptor.mayRemoveOptionalDevice(i)
                                if success:
                                    self.__isActualModules = False
                                    vehDescriptor.removeOptionalDevice(i)
                                    break
                        else:
                            LOG_ERROR('Could not apply any chassis on this vehicle {}!'.format(cloneVehicle))
                            LOG_ERROR('Optional device can not be removed {}, because vehicle is still heavy!'.format(optDevice))

                    else:
                        LOG_ERROR('Unsupported optional device removing error: {}!!!'.format(reason))
                else:
                    vehDescriptor.removeOptionalDevice(i)

        return cloneVehicle

    @process
    def __installModule(self, vehicle, module):
        yield PreviewVehicleModuleInstaller(vehicle, module).request()


def _ErrorNotification(func):

    def funcWithMessage(self, *args, **kwargs):
        if self.isEnabled() and self.isAvailable():
            func(self, *args, **kwargs)
        else:
            SystemMessages.g_instance.pushI18nMessage('#system_messages:vehicleCompare/disabled', type=SM_TYPE.Error)

    return funcWithMessage


def _indexCanBePerformed(func):

    def __wrapper(self, *args, **kwargs):
        index = args[0]
        vehCount = self.getVehiclesCount()
        if not 0 <= index < vehCount:
            LOG_WARNING('Item with requested index ({}), can not be performed! Vehicles count in basket: {}'.format(index, vehCount))
            return None
        else:
            return func(self, *args, **kwargs)

    return __wrapper


class VehComparisonBasket(Controller):

    def __init__(self, proxy):
        super(VehComparisonBasket, self).__init__(proxy)
        self.__vehicles = []
        self.__isFull = False
        self.onChange = Event.Event()
        self.onParametersChange = Event.Event()
        self.onSwitchChange = Event.Event()
        self.__isEnabled = True

    def onConnected(self):
        self.__vehicles = []

    def onLobbyStarted(self, ctx):
        self.__isEnabled = g_lobbyContext.getServerSettings().isVehicleComparingEnabled()

    def onLobbyInited(self, event):
        self.__initHandlers()

    def onAvatarBecomePlayer(self):
        self.__disposeHandlers()

    def onDisconnected(self):
        self.__vehicles = []
        self.__disposeHandlers()
        super(VehComparisonBasket, self).onDisconnected()

    def fini(self):
        self.__vehicles = None
        self.onChange.clear()
        self.onParametersChange.clear()
        self.onSwitchChange.clear()
        super(VehComparisonBasket, self).fini()
        return

    @_ErrorNotification
    @_indexCanBePerformed
    def setVehicleCrew(self, index, crewLevel):
        vehCompareData = self.__vehicles[index]
        if crewLevel != vehCompareData.getCrewLevel():
            vehCompareData.setCrewLevel(crewLevel)
            self.onParametersChange((index,))

    @_ErrorNotification
    @_indexCanBePerformed
    def applyModulesFromVehicle(self, index, vehicle):
        """
        :param index: int item index in self.__vehicles list
        :param vehicle: gui.shared.gui_items.Vehicle
        """
        vehCompareData = self.__vehicles[index]
        if not vehCompareData.getVehicleCD() == vehicle.intCD:
            raise AssertionError
            newStrCD = _makeStrCD(vehicle)
            vehCompareData.getVehicleStrCD() != newStrCD and vehCompareData.setVehicleStrCD(newStrCD)
            self.onParametersChange((index,))
        else:
            LOG_DEBUG('Modules has not been applied because they are not different.')

    @_ErrorNotification
    def addVehicle(self, vehicleCompactDesr):
        if not isinstance(vehicleCompactDesr, (int, float)):
            raise AssertionError
            self.__canBeAdded() and self.__vehicles.append(self._createVehCompareData(vehicleCompactDesr))
            self.__applyChanges(addedIDXs=[len(self.__vehicles) - 1], addedCDs=[vehicleCompactDesr])

    @_ErrorNotification
    def addVehicles(self, vehCDs):
        newVehsCount = len(vehCDs)
        currVehsCount = len(self.__vehicles)
        if newVehsCount + currVehsCount <= MAX_VEHICLES_TO_COMPARE_COUNT:
            self.__vehicles.extend(map(lambda cd: self._createVehCompareData(cd), vehCDs))
            self.__applyChanges(addedIDXs=range(currVehsCount, currVehsCount + newVehsCount), addedCDs=vehCDs)
        else:
            LOG_DEBUG("Couldn't add vehicles in the comparison basket, basket is full!")

    @_ErrorNotification
    @_indexCanBePerformed
    def removeVehicleByIdx(self, index):
        vehCompareData = self.__vehicles[index]
        removedVehCD = vehCompareData.getVehicleCD()
        del self.__vehicles[index]
        self.__applyChanges(removedIDXs=[index], removedCDs=[removedVehCD])

    @_ErrorNotification
    def removeAllVehicles(self):
        removedCDs = []
        for vehCompareData in self.__vehicles:
            removedCDs.append(vehCompareData.getVehicleCD())

        self.__vehicles = []
        self.__applyChanges(removedIDXs=range(len(removedCDs) - 1, -1, -1), removedCDs=removedCDs)

    def isFull(self):
        return self.__isFull

    def isReadyToAdd(self, vehicle):
        """
        :param vehicle: instance of gui.shared.gui_items.Vehicle.Vehicle
        :return: True if compare feature is available and basket is not full and valid for vehicle, otherwise - False.
        """
        return self.isAvailable() and not self.isFull() and isValidVehicleForComparing(vehicle)

    def isAvailable(self):
        """
        GUI elements visible, but not available(e.g. miniclient)
        :return: True if vehicle compare feature is available, otherwise - False.
        """
        return True

    def isEnabled(self):
        """
        GUI elements not visible.
        :return: True if vehicle compare feature is enabled on the server, otherwise - False.
        """
        return self.__isEnabled

    @_ErrorNotification
    @_indexCanBePerformed
    def cloneVehicle(self, index):
        """
        Creates copy of vehicle which index has been provided and adds it at the end of list.
        :param index: copied item index
        """
        if self.__canBeAdded():
            target = self.__vehicles[index]
            self.__vehicles.append(target.clone())
            self.__applyChanges(addedIDXs=[len(self.__vehicles) - 1], addedCDs=[target.getVehicleCD()])

    def getVehiclesCDs(self):
        return map(lambda vehCompareData: vehCompareData.getVehicleCD(), self.__vehicles)

    def getVehiclesCount(self):
        return len(self.__vehicles)

    @_indexCanBePerformed
    def getVehicleAt(self, index):
        return self.__vehicles[index]

    @staticmethod
    def _createVehCompareData(cd):
        return _VehCompareData(cd)

    def __applyChanges(self, addedIDXs = None, addedCDs = None, removedIDXs = None, removedCDs = None):
        oldVal = self.__isFull
        self.__isFull = len(self.__vehicles) == MAX_VEHICLES_TO_COMPARE_COUNT
        self.onChange(_ChangedData(addedIDXs, addedCDs, removedIDXs, removedCDs, self.__isFull != oldVal))

    def __initHandlers(self):
        g_itemsCache.onSyncCompleted += self.__onCacheResync
        g_lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged

    def __disposeHandlers(self):
        g_itemsCache.onSyncCompleted -= self.__onCacheResync
        settings = g_lobbyContext.getServerSettings()
        if settings:
            settings.onServerSettingsChange -= self.__onServerSettingChanged

    def __onCacheResync(self, reason, diff):
        if reason != CACHE_SYNC_REASON.CLIENT_UPDATE:
            return
        else:
            changedIDXs = []
            if diff is not None and GUI_ITEM_TYPE.VEHICLE in diff:
                vehDiff = diff[GUI_ITEM_TYPE.VEHICLE]
                isModulesChanged = set(diff.keys()).intersection(set(GUI_ITEM_TYPE.VEHICLE_MODULES))
                for changedVehCD in vehDiff:
                    for idx, vehCompareData in enumerate(self.__vehicles):
                        if changedVehCD == vehCompareData.getVehicleCD():
                            isCachedVehInInv = g_itemsCache.items.getItemByCD(changedVehCD).isInInventory
                            if vehCompareData.isInInventory() != isCachedVehInInv:
                                if not isCachedVehInInv:
                                    if vehCompareData.getCrewLevel() == CREW_TYPES.CURRENT:
                                        vehCompareData.setCrewLevel(CREW_TYPES.SKILL_100)
                                vehCompareData.initVehicle()
                                changedIDXs.append(idx)
                            elif isModulesChanged:
                                vehCompareData.initVehicle()
                                changedIDXs.append(idx)

            if changedIDXs:
                self.onParametersChange(changedIDXs)
            return

    def __onServerSettingChanged(self, diff):
        if 'isVehiclesCompareEnabled' in diff:
            self.__isEnabled = diff['isVehiclesCompareEnabled']
            self.onSwitchChange()

    def __canBeAdded(self):
        if self.__isFull:
            LOG_DEBUG("Couldn't add vehicle into the comparison basket, basket is full!")
            return False
        else:
            return True
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\game_control\veh_comparison_basket.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:02 St�edn� Evropa (letn� �as)
