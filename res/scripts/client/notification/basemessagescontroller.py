# 2016.10.11 22:15:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/notification/BaseMessagesController.py


class BaseMessagesController(object):

    def __init__(self, model):
        self._model = model

    def cleanUp(self):
        self._model = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\notification\basemessagescontroller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:21 St�edn� Evropa (letn� �as)
