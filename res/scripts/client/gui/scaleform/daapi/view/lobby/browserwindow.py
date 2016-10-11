# 2016.10.11 22:10:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/BrowserWindow.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.BrowserWindowMeta import BrowserWindowMeta
from gui.Scaleform.locale.WAITING import WAITING

class BrowserWindow(BrowserWindowMeta):

    def __init__(self, ctx = None):
        super(BrowserWindow, self).__init__()
        self.__size = ctx.get('size')
        self.__browserID = ctx.get('browserID')
        self.__customTitle = ctx.get('title')
        self.__showActionBtn = ctx.get('showActionBtn', True)
        self.__showWaiting = ctx.get('showWaiting', False)
        self.__showCloseBtn = ctx.get('showCloseBtn', False)

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(BrowserWindow, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VIEW_ALIAS.BROWSER:
            viewPy.init(self.__browserID)

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(BrowserWindow, self)._populate()
        self.as_configureS(self.__customTitle, self.__showActionBtn, self.__showCloseBtn)
        self.as_setSizeS(*self.__size)
        if self.__showWaiting:
            self.as_showWaitingS(WAITING.LOADCONTENT, {})
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\browserwindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:55 St�edn� Evropa (letn� �as)
