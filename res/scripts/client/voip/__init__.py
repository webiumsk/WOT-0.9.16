# 2016.10.11 22:15:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/VOIP/__init__.py
import BigWorld

def getVOIPManager():
    if not globals().has_key('__handler'):
        from VOIPManager import VOIPManager
        globals()['__handler'] = VOIPManager()
        BigWorld.VOIP.setHandler(__handler)
    return __handler
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\voip\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:51 Støední Evropa (letní èas)
