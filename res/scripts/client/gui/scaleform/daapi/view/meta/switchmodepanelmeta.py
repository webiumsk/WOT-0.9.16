# 2016.10.11 22:12:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SwitchModePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SwitchModePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def switchMode(self):
        self._printOverrideError('switchMode')

    def onSelectCheckBoxAutoSquad(self, isSelected):
        self._printOverrideError('onSelectCheckBoxAutoSquad')

    def as_setDataS(self, data):
        """
        :param data: Represented by SwitchModePanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\switchmodepanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:38 St�edn� Evropa (letn� �as)
