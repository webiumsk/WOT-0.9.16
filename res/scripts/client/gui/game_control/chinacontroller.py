# 2016.10.11 22:09:57 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/ChinaController.py
from adisp import process
from gui.Scaleform.locale.MENU import MENU
from gui.game_control import gc_constants
from gui.game_control.controllers import Controller

class ChinaController(Controller):

    def __init__(self, proxy):
        super(ChinaController, self).__init__(proxy)
        self.__browserID = None
        return

    def onLobbyInited(self, event):
        if not self._proxy.gameSession.battlesCount % gc_constants.BROWSER.CHINA_BROWSER_COUNT:
            self.showBrowser()

    def onDisconnected(self):
        if self.__browserID is not None:
            self.__browserClosed(self.__browserID)
        return

    def __browserClosed(self, browserId):
        if browserId == self.__browserID:
            self.__browserID = None
            self._getBrowserController().onBrowserDeleted -= self.__browserClosed
        return

    @process
    def showBrowser(self):
        self.__browserID = yield self._getBrowserController().load(title=MENU.BROWSER_WINDOW_TITLE, browserID=self.__browserID)
        self._getBrowserController().onBrowserDeleted += self.__browserClosed

    def _getBrowserController(self):
        return self._proxy.getController(gc_constants.CONTROLLER.BROWSER)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\game_control\chinacontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:09:57 St�edn� Evropa (letn� �as)
