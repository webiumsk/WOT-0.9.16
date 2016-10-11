# 2016.10.11 22:12:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehiclePreview/VehiclePreview.py
from collections import namedtuple
import BigWorld
from CurrentVehicle import g_currentPreviewVehicle
from account_helpers import AccountSettings
from account_helpers.AccountSettings import PREVIEW_INFO_PANEL_IDX
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip
from gui.Scaleform.daapi.view.meta.VehiclePreviewMeta import VehiclePreviewMeta
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.VEHICLE_PREVIEW import VEHICLE_PREVIEW
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.customization.shared import getBonusIcon42x42
from gui.game_control import getVehicleComparisonBasketCtrl
from gui.shared import event_dispatcher
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.economics import getGUIPrice
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles, icons
from gui.shared.gui_items.Vehicle import getLobbyDescription
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.money import Currency
from gui.shared.tooltips.formatters import getActionPriceData
from helpers.i18n import makeString as _ms
CREW_INFO_TAB_ID = 'crewInfoTab'
FACT_SHEET_TAB_ID = 'factSheetTab'
TAB_ORDER = [FACT_SHEET_TAB_ID, CREW_INFO_TAB_ID]
TAB_DATA_MAP = {FACT_SHEET_TAB_ID: (VEHPREVIEW_CONSTANTS.FACT_SHEET_LINKAGE, VEHICLE_PREVIEW.INFOPANEL_TAB_FACTSHEET_NAME),
 CREW_INFO_TAB_ID: (VEHPREVIEW_CONSTANTS.CREW_INFO_LINKAGE, VEHICLE_PREVIEW.INFOPANEL_TAB_CREWINFO_NAME)}
_ButtonState = namedtuple('_ButtonState', 'enabled, price, label, isAction, currencyIcon, actionType, action')
_BACK_BTN_LABELS = {VIEW_ALIAS.LOBBY_HANGAR: 'hangar',
 VIEW_ALIAS.LOBBY_STORE: 'shop',
 VIEW_ALIAS.LOBBY_RESEARCH: 'researchTree',
 VIEW_ALIAS.LOBBY_TECHTREE: 'researchTree',
 VIEW_ALIAS.VEHICLE_COMPARE: 'vehicleCompare'}

class VehiclePreview(LobbySubView, VehiclePreviewMeta):
    __background_alpha__ = 0.0

    def __init__(self, ctx = None):
        super(VehiclePreview, self).__init__(ctx)
        self._actionType = None
        self.__vehicleCD = ctx.get('itemCD')
        self.__backAlias = ctx.get('previewAlias', VIEW_ALIAS.LOBBY_HANGAR)
        g_currentPreviewVehicle.selectVehicle(self.__vehicleCD)
        return

    def _populate(self):
        super(VehiclePreview, self)._populate()
        g_clientUpdateManager.addCallbacks({'stats.credits': self.__updateBtnState,
         'stats.gold': self.__updateBtnState,
         'stats.freeXP': self.__updateBtnState})
        g_currentPreviewVehicle.onComponentInstalled += self.__updateStatus
        g_currentPreviewVehicle.onVehicleUnlocked += self.__updateBtnState
        g_currentPreviewVehicle.onVehicleInventoryChanged += self.__onInventoryChanged
        g_currentPreviewVehicle.onChanged += self.__onVehicleChanged
        comparisonBasket = getVehicleComparisonBasketCtrl()
        comparisonBasket.onChange += self.__onCompareBasketChanged
        comparisonBasket.onSwitchChange += self.__updateHeaderData
        if g_currentPreviewVehicle.isPresent():
            self.__updateHeaderData()
            self.__fullUpdate()
        else:
            event_dispatcher.showHangar()

    def _dispose(self):
        super(VehiclePreview, self)._dispose()
        g_clientUpdateManager.removeObjectCallbacks(self)
        g_currentPreviewVehicle.onComponentInstalled -= self.__updateStatus
        g_currentPreviewVehicle.onVehicleUnlocked -= self.__updateBtnState
        g_currentPreviewVehicle.onVehicleInventoryChanged -= self.__onInventoryChanged
        g_currentPreviewVehicle.onChanged -= self.__onVehicleChanged
        comparisonBasket = getVehicleComparisonBasketCtrl()
        comparisonBasket.onChange -= self.__onCompareBasketChanged
        comparisonBasket.onSwitchChange -= self.__updateHeaderData
        g_currentPreviewVehicle.selectNoVehicle()

    def closeView(self):
        self.onBackClick()

    def onBackClick(self):
        if self.__backAlias == VIEW_ALIAS.LOBBY_RESEARCH:
            event_dispatcher.showResearchView(self.__vehicleCD)
        else:
            event = g_entitiesFactories.makeLoadEvent(self.__backAlias)
            self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)

    def onOpenInfoTab(self, index):
        AccountSettings.setSettings(PREVIEW_INFO_PANEL_IDX, index)

    def onBuyOrResearchClick(self):
        if self._actionType == ItemsActionsFactory.UNLOCK_ITEM:
            unlockProps = g_techTreeDP.getUnlockProps(self.__vehicleCD)
            ItemsActionsFactory.doAction(ItemsActionsFactory.UNLOCK_ITEM, self.__vehicleCD, unlockProps.parentID, unlockProps.unlockIdx, unlockProps.xpCost)
        else:
            ItemsActionsFactory.doAction(ItemsActionsFactory.BUY_VEHICLE, self.__vehicleCD)

    def onCompareClick(self):
        """
        Add to compare button click handler
        """
        getVehicleComparisonBasketCtrl().addVehicle(self.__vehicleCD)

    def __fullUpdate(self):
        selectedTabInd = AccountSettings.getSettings(PREVIEW_INFO_PANEL_IDX)
        self.__updateHeaderData()
        self.as_updateInfoDataS(self.__getInfoData(selectedTabInd))
        self.__updateBtnState()
        self.__updateStatus()

    def __onVehicleChanged(self, *args):
        if g_currentPreviewVehicle.isPresent():
            self.__vehicleCD = g_currentPreviewVehicle.item.intCD
            self.__fullUpdate()

    def __getVehiclePanelData(self):
        vehicle = g_currentPreviewVehicle.item
        data = {'info': text_styles.main(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_BODY),
         'infoTooltip': TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO,
         'vehCompareData': self.__getVehCompareData(vehicle)}
        return data

    def __getVehCompareData(self, vehicle):
        comparisonBasket = getVehicleComparisonBasketCtrl()
        state, tooltip = resolveStateTooltip(comparisonBasket, vehicle, enabledTooltip=None, fullTooltip=VEH_COMPARE.STORE_COMPAREVEHICLEBTN_TOOLTIPS_DISABLED)
        return {'modeAvailable': comparisonBasket.isEnabled(),
         'btnEnabled': state,
         'btnTooltip': tooltip,
         'label': text_styles.main(VEH_COMPARE.VEHPREVIEW_COMPAREINFO_ADDTOCOMPARE)}

    def __onCompareBasketChanged(self, changedData):
        """
        gui.game_control.VehComparisonBasket.onChange event handler
        :param changedData: instance of gui.game_control.veh_comparison_basket._ChangedData
        """
        if changedData.isFullChanged:
            self.__updateHeaderData()

    def __onInventoryChanged(self, *arg):
        if not g_currentPreviewVehicle.isPresent():
            event_dispatcher.selectVehicleInHangar(self.__vehicleCD)

    def __updateStatus(self):
        if g_currentPreviewVehicle.isPresent():
            if g_currentPreviewVehicle.isModified():
                icon = icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ATTENTIONICONFILLED, 16, 16, -3, 0)
                text = text_styles.neutral('%s %s' % (icon, _ms(VEHICLE_PREVIEW.MODULESPANEL_STATUS_TEXT)))
            else:
                text = text_styles.main(VEHICLE_PREVIEW.MODULESPANEL_LABEL)
            self.as_updateVehicleStatusS(text)

    def __updateBtnState(self, *args):
        if g_currentPreviewVehicle.isPresent():
            btnState = self.__getBtnState()
            isAction = btnState.isAction
            self._actionType = btnState.actionType
            self.as_updateBuyButtonS(btnState.enabled, btnState.label)
            self.as_updatePriceS({'value': btnState.price,
             'icon': btnState.currencyIcon,
             'showAction': isAction,
             'actionTooltipType': TOOLTIPS_CONSTANTS.ACTION_PRICE if isAction else None,
             'actionData': btnState.action})
        return

    def __updateHeaderData(self):
        self.as_setStaticDataS(self.__getStaticData())

    def __getBtnState(self):
        vehicle = g_currentPreviewVehicle.item
        if vehicle.isUnlocked:
            money = g_itemsCache.items.stats.money
            exchangeRate = g_itemsCache.items.shop.exchangeRate
            price = getGUIPrice(vehicle, money, exchangeRate)
            currency = price.getCurrency(byWeight=True)
            action = getActionPriceData(vehicle)
            mayObtainForMoney = vehicle.mayObtainWithMoneyExchange(money, exchangeRate)
            if currency == Currency.GOLD:
                currencyIcon = RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICONBIG
                formatter = text_styles.goldTextBig if mayObtainForMoney else text_styles.errCurrencyTextBig
            else:
                currencyIcon = RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICONBIG
                formatter = text_styles.creditsTextBig if mayObtainForMoney else text_styles.errCurrencyTextBig
            return _ButtonState(mayObtainForMoney, formatter(BigWorld.wg_getIntegralFormat(price.get(currency))), VEHICLE_PREVIEW.BUYINGPANEL_BUYBTN_LABEL_RESTORE if vehicle.isRestorePossible() else VEHICLE_PREVIEW.BUYINGPANEL_BUYBTN_LABEL_BUY, action is not None, currencyIcon, ItemsActionsFactory.BUY_VEHICLE, action)
        else:
            nodeCD = vehicle.intCD
            currencyIcon = RES_ICONS.MAPS_ICONS_LIBRARY_XPCOSTICONBIG
            isAvailableToUnlock, xpCost, possibleXp = g_techTreeDP.isVehicleAvailableToUnlock(nodeCD)
            formatter = text_styles.creditsTextBig if possibleXp >= xpCost else text_styles.errCurrencyTextBig
            return _ButtonState(isAvailableToUnlock, formatter(BigWorld.wg_getIntegralFormat(xpCost)), VEHICLE_PREVIEW.BUYINGPANEL_BUYBTN_LABEL_RESEARCH, False, currencyIcon, ItemsActionsFactory.UNLOCK_ITEM, None)
            return None

    def __getStaticData(self):
        return {'header': self.__getHeaderData(),
         'bottomPanel': self.__getBottomPanelData(),
         'tabButtonsData': self.__packTabButtonsData(),
         'vehicleInfo': self.__getVehiclePanelData()}

    def __getHeaderData(self):
        vehicle = g_currentPreviewVehicle.item
        return {'tankType': '{}_elite'.format(vehicle.type) if vehicle.isElite else vehicle.type,
         'tankInfo': text_styles.concatStylesToMultiLine(text_styles.promoSubTitle(vehicle.shortUserName), text_styles.stats(MENU.levels_roman(vehicle.level))),
         'closeBtnLabel': VEHICLE_PREVIEW.HEADER_CLOSEBTN_LABEL,
         'backBtnLabel': VEHICLE_PREVIEW.HEADER_BACKBTN_LABEL,
         'backBtnDescrLabel': self.__getBackBtnLabel(),
         'titleText': text_styles.promoTitle(VEHICLE_PREVIEW.HEADER_TITLE),
         'isPremiumIGR': vehicle.isPremiumIGR}

    def __getBackBtnLabel(self):
        key = _BACK_BTN_LABELS.get(self.__backAlias, 'hangar')
        return '#vehicle_preview:header/backBtn/descrLabel/%s' % key

    def __getBottomPanelData(self):
        item = g_currentPreviewVehicle.item
        isBuyingAvailable = not item.isHidden or item.isRentable or item.isRestorePossible()
        if isBuyingAvailable:
            buyingLabel = text_styles.main(VEHICLE_PREVIEW.BUYINGPANEL_LABEL)
        else:
            buyingLabel = text_styles.alert(VEHICLE_PREVIEW.BUYINGPANEL_ALERTLABEL)
        return {'buyingLabel': buyingLabel,
         'modulesLabel': text_styles.middleTitle(VEHICLE_PREVIEW.MODULESPANEL_TITLE),
         'isBuyingAvailable': isBuyingAvailable}

    def __getInfoData(self, selectedTabInd):
        return {'selectedTab': selectedTabInd,
         'tabData': self.__packTabData(),
         'nation': g_currentPreviewVehicle.item.nationName}

    def __packTabButtonsData(self):
        data = []
        for id in TAB_ORDER:
            linkage, label = TAB_DATA_MAP[id]
            data.append({'label': label,
             'linkage': linkage})

        return data

    def __packTabData(self):
        return [self.__packDataItem(VEHPREVIEW_CONSTANTS.FACT_SHEET_DATA_CLASS_NAME, self.__packFactSheetData()), self.__packDataItem(VEHPREVIEW_CONSTANTS.CREW_INFO_DATA_CLASS_NAME, self.__packCrewInfoData())]

    def __packCrewInfoData(self):
        crewData = []
        for idx, tankman in g_currentPreviewVehicle.item.crew:
            role = tankman.descriptor.role
            crewData.append({'icon': getBonusIcon42x42(role),
             'name': text_styles.middleTitle(ITEM_TYPES.tankman_roles(role)),
             'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER,
             'role': role})

        return {'listDesc': text_styles.main(VEHICLE_PREVIEW.INFOPANEL_TAB_CREWINFO_LISTDESC_TEXT),
         'crewList': crewData,
         'showNationFlag': False}

    def __packFactSheetData(self):
        return {'historicReferenceTxt': text_styles.main(g_currentPreviewVehicle.item.fullDescription),
         'showNationFlag': True}

    def __packDataItem(self, className, data):
        return {'voClassName': className,
         'voData': data}
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\vehiclepreview\vehiclepreview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:09 St�edn� Evropa (letn� �as)
