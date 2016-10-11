# 2016.10.11 22:10:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/Browser.py
from gui import game_control
from gui.Scaleform.daapi.view.meta.BrowserMeta import BrowserMeta
from gui.Scaleform.locale.MENU import MENU
from gui.shared.formatters import icons
from helpers import i18n
from gui.shared import g_eventBus
from gui.shared.events import BrowserEvent

class Browser(BrowserMeta):

    def __init__(self):
        super(Browser, self).__init__()
        self.__browserID = None
        self.__browser = None
        self.__size = None
        self.__isLoaded = True
        return

    def init(self, browserID):
        self.__browserID = browserID
        self.__browser = game_control.getBrowserCtrl().getBrowser(self.__browserID)
        if not self.__browser is not None:
            raise AssertionError('Cannot find browser')
            self.__browser.hasBrowser or g_eventBus.addListener(BrowserEvent.BROWSER_CREATED, self.__handleBrowserCreated)
        else:
            self.__prepareBrowser()
        return

    def onWindowClose(self):
        self.destroy()

    def browserAction(self, action):
        if self.__browser is not None:
            self.__browser.browserAction(action)
        return

    def browserMove(self, x, y, z):
        if self.__browser is not None:
            self.__browser.browserMove(x, y, z)
        return

    def browserDown(self, x, y, z):
        if self.__browser is not None:
            self.__browser.browserDown(x, y, z)
        return

    def browserUp(self, x, y, z):
        if self.__browser is not None:
            self.__browser.browserUp(x, y, z)
        return

    def browserFocusOut(self):
        if self.__browser is not None:
            self.__browser.browserFocusOut()
        return

    def onBrowserShow(self, needRefresh = False):
        self.__browser.onBrowserShow(needRefresh)

    def onBrowserHide(self):
        if self.__browser is not None:
            self.__browser.onBrowserHide()
        return

    def setBrowserSize(self, width, height):
        self.__size = (width, height)
        if self.__browser is not None:
            self.__browser.updateSize(self.__size)
        return

    def _dispose(self):
        self.__browser.onLoadStart -= self.__onLoadStart
        self.__browser.onLoadingStateChange -= self.__onLoadingStateChange
        self.__browser.onLoadEnd -= self.__onLoadEnd
        self.__browser.onNavigate -= self.__onNavigate
        self.__browser = None
        game_control.g_instance.browser.delBrowser(self.__browserID)
        g_eventBus.removeListener(BrowserEvent.BROWSER_CREATED, self.__handleBrowserCreated)
        super(Browser, self)._dispose()
        return

    def __showDataUnavailableView(self):
        header = icons.alert() + i18n.makeString(MENU.BROWSER_DATAUNAVAILABLE_HEADER)
        description = i18n.makeString(MENU.BROWSER_DATAUNAVAILABLE_DESCRIPTION)
        self.as_showServiceViewS(header, description)

    def __onLoadStart(self, url):
        pass

    def __onLoadEnd(self, url, isLoaded = True):
        self.__isLoaded = self.__isLoaded and isLoaded
        if not self.__isLoaded:
            self.__showDataUnavailableView()

    def __onLoadingStateChange(self, isLoading):
        if isLoading:
            self.as_loadingStartS()
        else:
            self.as_loadingStopS()

    def __onNavigate(self, url):
        self.as_hideServiceViewS()
        self.__isLoaded = True

    def __handleBrowserCreated(self, event):
        event.ctx['browserID'] == self.__browserID and g_eventBus.removeListener(BrowserEvent.BROWSER_CREATED, self.__handleBrowserCreated)
        self.__browser = game_control.g_instance.browser.getBrowser(self.__browserID)
        if not self.__browser is not None:
            raise AssertionError('Cannot find browser')
            self.__prepareBrowser()
        return

    def __prepareBrowser(self):
        self.__browser.onLoadStart += self.__onLoadStart
        self.__browser.onLoadingStateChange += self.__onLoadingStateChange
        self.__browser.onLoadEnd += self.__onLoadEnd
        self.__browser.onNavigate += self.__onNavigate
        if self.__size is not None:
            self.__browser.updateSize(self.__size)
        if self.__browser.isNavigationComplete:
            self.as_loadingStopS()
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\browser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:55 St�edn� Evropa (letn� �as)
