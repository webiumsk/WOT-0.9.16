# 2016.10.11 22:12:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/EventLogManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class EventLogManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def logEvent(self, subSystemType, eventType, uiid, arg):
        self._printOverrideError('logEvent')

    def as_setSystemEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setSystemEnabled(isEnabled)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\eventlogmanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:44 Støední Evropa (letní èas)
