# 2016.10.11 22:12:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/PopoverManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class PopoverManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def requestShowPopover(self, alias, data):
        self._printOverrideError('requestShowPopover')

    def requestHidePopover(self):
        self._printOverrideError('requestHidePopover')

    def as_onPopoverDestroyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onPopoverDestroy()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\popovermanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:45 St�edn� Evropa (letn� �as)
