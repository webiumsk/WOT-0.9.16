# 2016.10.11 22:16:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Listeners.py
import weakref
_languageChangeListeners = []
_deviceListeners = []

def registerInputLangChangeListener(listener):
    global _languageChangeListeners
    _languageChangeListeners.append(weakref.ref(listener))


def registerDeviceListener(listener):
    _deviceListeners.append(weakref.ref(listener))


def handleInputLangChangeEvent():
    import GUI
    for listener in [ x() for x in _languageChangeListeners if x() is not None ]:
        if hasattr(listener, 'handleInputLangChangeEvent'):
            listener.handleInputLangChangeEvent()

    return True


def onRecreateDevice():
    for listener in [ x() for x in _deviceListeners if x() is not None ]:
        if hasattr(listener, 'onRecreateDevice'):
            listener.onRecreateDevice()

    return
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\bwobsolete_helpers\pygui\listeners.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:16:58 St�edn� Evropa (letn� �as)
