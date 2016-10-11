# 2016.10.11 22:12:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContextMenuManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ContextMenuManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def requestOptions(self, type, ctx):
        self._printOverrideError('requestOptions')

    def onOptionSelect(self, optionId):
        self._printOverrideError('onOptionSelect')

    def onHide(self):
        self._printOverrideError('onHide')

    def as_setOptionsS(self, data):
        """
        :param data: Represented by ContextMenuOptionsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOptions(data)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\contextmenumanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:44 Støední Evropa (letní èas)
