# 2016.10.11 22:15:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/control/listener.py
from gui.app_loader import g_appLoader, settings
_SPACE_ID = settings.GUI_GLOBAL_SPACE_ID

class AppLoaderListener(object):

    def __init__(self):
        super(AppLoaderListener, self).__init__()
        self.__loader = None
        return

    def start(self, loader):
        self.__loader = loader
        g_appLoader.onGUISpaceEntered += self.__onGUISpaceEntered
        g_appLoader.onGUISpaceLeft += self.__onGUISpaceLeft

    def stop(self):
        g_appLoader.onGUISpaceEntered -= self.__onGUISpaceEntered
        g_appLoader.onGUISpaceLeft -= self.__onGUISpaceLeft

    def __onGUISpaceEntered(self, spaceID):
        if spaceID == _SPACE_ID.LOGIN:
            self.__loader.goToLogin()
        elif spaceID == _SPACE_ID.LOBBY:
            self.__loader.goToLobby()
        elif spaceID == _SPACE_ID.BATTLE:
            self.__loader.goToBattle()

    def __onGUISpaceLeft(self, spaceID):
        if spaceID == _SPACE_ID.LOBBY:
            self.__loader.leaveLobby()
        elif spaceID == _SPACE_ID.BATTLE:
            self.__loader.leaveBattle()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:28 St�edn� Evropa (letn� �as)
