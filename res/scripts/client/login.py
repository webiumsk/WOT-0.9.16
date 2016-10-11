# 2016.10.11 22:08:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/Login.py
import BigWorld
from PlayerEvents import g_playerEvents
from ConnectionManager import connectionManager
from debug_utils import *

class PlayerLogin(BigWorld.Entity):

    def __init__(self):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def onKickedFromServer(self, checkoutPeripheryID):
        LOG_DEBUG('onKickedFromServer', checkoutPeripheryID)
        g_playerEvents.onKickWhileLoginReceived(checkoutPeripheryID)

    def receiveLoginQueueNumber(self, queueNumber):
        LOG_DEBUG('receiveLoginQueueNumber', queueNumber)
        g_playerEvents.onLoginQueueNumberReceived(queueNumber)

    def handleKeyEvent(self, event):
        return False


Login = PlayerLogin
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\login.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:08:41 St�edn� Evropa (letn� �as)
