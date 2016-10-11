# 2016.10.11 22:12:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ToolTipMgrMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ToolTipMgrMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def onCreateComplexTooltip(self, tooltipId, stateType):
        self._printOverrideError('onCreateComplexTooltip')

    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        self._printOverrideError('onCreateTypedTooltip')

    def as_showS(self, tooltipData, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_show(tooltipData, linkage)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\tooltipmgrmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:45 Støední Evropa (letní èas)
