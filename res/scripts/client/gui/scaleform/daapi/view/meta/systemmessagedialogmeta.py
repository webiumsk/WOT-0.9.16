# 2016.10.11 22:12:38 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SystemMessageDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SystemMessageDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setInitDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setMessageDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessageData(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\systemmessagedialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:38 St�edn� Evropa (letn� �as)
