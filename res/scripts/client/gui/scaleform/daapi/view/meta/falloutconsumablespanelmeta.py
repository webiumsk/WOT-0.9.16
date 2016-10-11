# 2016.10.11 22:12:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutConsumablesPanelMeta.py
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel

class FalloutConsumablesPanelMeta(ConsumablesPanel):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ConsumablesPanel
    """

    def as_initializeRageProgressS(self, show, barProps):
        if self._isDAAPIInited():
            return self.flashObject.as_initializeRageProgress(show, barProps)

    def as_updateProgressBarValueByDeltaS(self, delta):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressBarValueByDelta(delta)

    def as_updateProgressBarValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressBarValue(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\falloutconsumablespanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:24 Støední Evropa (letní èas)
