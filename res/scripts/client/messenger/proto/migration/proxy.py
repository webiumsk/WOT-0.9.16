# 2016.10.11 22:15:06 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/migration/proxy.py


class MigrationProxy(object):
    __slots__ = ('_proto',)

    def __init__(self, proto):
        super(MigrationProxy, self).__init__()
        self._proto = proto

    def clear(self):
        self._proto = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\proto\migration\proxy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:06 St�edn� Evropa (letn� �as)
