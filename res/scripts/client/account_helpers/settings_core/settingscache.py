# 2016.10.11 22:09:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/account_helpers/settings_core/SettingsCache.py
from Event import Event
from adisp import async
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared.utils.requesters.IntSettingsRequester import IntSettingsRequester
from account_helpers.settings_core.settings_constants import VERSION

class _SettingsCache(object):

    def __init__(self):
        self.__intSettings = IntSettingsRequester()
        self.__waitForSync = False
        self.onSyncStarted = Event()
        self.onSyncCompleted = Event()

    def init(self):
        g_clientUpdateManager.addCallbacks({'intUserSettings': self._onResync})

    def fini(self):
        self.onSyncStarted.clear()
        self.onSyncCompleted.clear()
        g_clientUpdateManager.removeObjectCallbacks(self)

    @property
    def waitForSync(self):
        return self.__waitForSync

    @property
    def settings(self):
        return self.__intSettings

    def _onResync(self, *args):
        self.__invalidateData()

    @async
    def update(self, callback = None):
        self.__invalidateData(callback)

    def getSectionSettings(self, section, defaultValue = 0):
        return self.__intSettings.getSetting(section, defaultValue)

    def setSectionSettings(self, section, value):
        self.__intSettings.setSetting(section, value)

    def setSettings(self, settings):
        self.__intSettings.setSettings(settings)

    def getSetting(self, key, defaultValue = 0):
        return self.__intSettings.getSetting(key, defaultValue)

    def getVersion(self, defaultValue = 0):
        return self.__intSettings.getSetting(VERSION, defaultValue)

    def setVersion(self, value):
        self.__intSettings.setSetting(VERSION, value)

    def __invalidateData(self, callback = lambda *args: None):

        def cbWrapper(*args):
            self.__waitForSync = False
            self.onSyncCompleted()
            callback(*args)

        self.__waitForSync = True
        self.onSyncStarted()
        import BattleReplay
        if BattleReplay.g_replayCtrl.isPlaying:
            cbWrapper(dict())
            return
        self.__intSettings.request()(cbWrapper)


g_settingsCache = _SettingsCache()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\account_helpers\settings_core\settingscache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:09:04 St�edn� Evropa (letn� �as)
