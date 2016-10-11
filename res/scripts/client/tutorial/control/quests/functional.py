# 2016.10.11 22:15:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/control/quests/functional.py
import copy
from account_helpers.AccountSettings import AccountSettings
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from account_helpers.settings_core.SettingsCore import g_settingsCore
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from shared_utils import findFirst
from tutorial.control.functional import FunctionalEffect, FunctionalShowWindowEffect, FunctionalRunTriggerEffect
from tutorial.logger import LOG_ERROR
from gui.shared import event_dispatcher

class SaveTutorialSettingEffect(FunctionalEffect):

    def triggerEffect(self):
        setting = self.getTarget()
        if setting is None:
            LOG_ERROR('Tutorial setting is not found', self._effect.getTargetID())
            return
        else:
            g_settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.TUTORIAL, {setting.getSettingName(): setting.getSettingValue()})
            return


class SaveAccountSettingEffect(FunctionalEffect):

    def triggerEffect(self):
        setting = self.getTarget()
        if setting is None:
            LOG_ERROR('Tutorial setting is not found', self._effect.getTargetID())
            return
        else:
            AccountSettings.setSettings(setting.getSettingName(), setting.getSettingValue())
            return


class SelectVehicleInHangar(FunctionalEffect):

    def triggerEffect(self):
        vehicleCriteria = self._tutorial.getVars().get(self.getTargetID())
        if vehicleCriteria is None:
            LOG_ERROR('Tutorial setting is not found', self._effect.getTargetID())
            return
        else:
            minLvl, maxLvl = vehicleCriteria.get('levelsRange', (1, 10))
            criteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.LEVELS(range(minLvl, maxLvl)) | ~REQ_CRITERIA.VEHICLE.EXPIRED_RENT | ~REQ_CRITERIA.VEHICLE.EVENT_BATTLE
            vehicles = sorted(g_itemsCache.items.getVehicles(criteria=criteria).values(), key=lambda item: item.level)
            vehicle = findFirst(None, vehicles)
            if vehicle is not None:
                event_dispatcher.selectVehicleInHangar(vehicle.intCD)
            return


class ShowSharedWindowEffect(FunctionalShowWindowEffect):

    def _setActions(self, window):
        self._tutorial.getFunctionalScene().setActions(copy.deepcopy(window.getActions()))


class QuestsFunctionalRunTriggerEffect(FunctionalRunTriggerEffect):

    def isInstantaneous(self):
        return True
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\quests\functional.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:34 St�edn� Evropa (letn� �as)
