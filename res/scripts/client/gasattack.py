# 2016.10.11 22:08:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/GasAttack.py
import BigWorld
from debug_utils import LOG_DEBUG

class GasAttack(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('GasAttack ', self.position)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gasattack.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:08:41 St�edn� Evropa (letn� �as)
