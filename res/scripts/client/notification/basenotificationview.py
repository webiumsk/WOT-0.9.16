# 2016.10.11 22:15:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/notification/BaseNotificationView.py


class BaseNotificationView(object):

    def __init__(self, model = None):
        super(BaseNotificationView, self).__init__()
        self._model = None
        self.setModel(model)
        return

    def setModel(self, value):
        self._model = value

    def cleanUp(self):
        self._model = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\notification\basenotificationview.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:21 St�edn� Evropa (letn� �as)
