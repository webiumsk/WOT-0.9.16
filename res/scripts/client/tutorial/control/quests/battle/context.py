# 2016.10.11 22:15:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/control/quests/battle/context.py
from account_helpers.AccountSettings import AccountSettings
from account_helpers.settings_core.settings_constants import TUTORIAL
from constants import ARENA_GUI_TYPE, IS_DEVELOPMENT
from gui.battle_control import g_sessionProvider
from tutorial.control import context

class BattleQuestsStartReqs(context.StartReqs):

    def isEnabled(self):
        areSettingsInited = self.__areSettingsInited()
        arenaGuiTypes = [ARENA_GUI_TYPE.RANDOM, ARENA_GUI_TYPE.SANDBOX, ARENA_GUI_TYPE.RATED_SANDBOX]
        if IS_DEVELOPMENT:
            arenaGuiTypes.append(ARENA_GUI_TYPE.TRAINING)
        return g_sessionProvider.arenaVisitor.getArenaGuiType() in arenaGuiTypes and areSettingsInited

    def __areSettingsInited(self):
        validateSettings = (TUTORIAL.FIRE_EXTINGUISHER_INSTALLED, TUTORIAL.MEDKIT_INSTALLED, TUTORIAL.REPAIRKIT_INSTALLED)
        getter = AccountSettings.getSettings
        for setting in validateSettings:
            if getter(setting):
                return True

        return False

    def prepare(self, ctx):
        pass

    def process(self, descriptor, ctx):
        return True


class FakeBonusesRequester(context.BonusesRequester):

    def request(self, chapterID = None):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\quests\battle\context.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:35 St�edn� Evropa (letn� �as)
