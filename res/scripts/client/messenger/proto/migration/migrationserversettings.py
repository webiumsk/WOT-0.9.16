# 2016.10.11 22:15:06 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/migration/MigrationServerSettings.py
from messenger.proto.interfaces import IProtoSettings

class MigrationServerSettings(IProtoSettings):

    def __init__(self):
        super(MigrationServerSettings, self).__init__()

    def isEnabled(self):
        return True
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\proto\migration\migrationserversettings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:15:06 Støední Evropa (letní èas)
