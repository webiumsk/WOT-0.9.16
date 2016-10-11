# 2016.10.11 22:10:13 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/factories/ControlFactory.py
from debug_utils import LOG_DEBUG
from gui.prb_control.items import PlayerDecorator
from gui.prb_control.settings import FUNCTIONAL_FLAG

class ControlFactory(object):

    def __del__(self):
        LOG_DEBUG('ControlFactory is deleted', self)

    def createEntry(self, ctx):
        raise NotImplementedError()

    def createEntryByAction(self, action):
        raise NotImplementedError()

    def createFunctional(self, ctx):
        raise NotImplementedError()

    def createPlayerInfo(self, functional):
        return PlayerDecorator()

    def createStateEntity(self, functional):
        raise NotImplementedError()

    def createLeaveCtx(self, flags = FUNCTIONAL_FLAG.UNDEFINED):
        raise NotImplementedError()

    @staticmethod
    def _createEntryByAction(action, available):
        result = None
        if action.actionName in available:
            clazz, args = available[action.actionName]
            if args:
                result = clazz(*args)
            else:
                result = clazz()
            result.setAccountsToInvite(action.accountsToInvite)
        return result
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\factories\controlfactory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:13 St�edn� Evropa (letn� �as)
