# 2016.10.11 22:12:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SlotsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SlotsPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def getSlotTooltipBody(self, orderID):
        self._printOverrideError('getSlotTooltipBody')

    def as_setPanelPropsS(self, data):
        """
        :param data: Represented by SlotsPanelPropsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelProps(data)

    def as_setSlotsS(self, orders):
        if self._isDAAPIInited():
            return self.flashObject.as_setSlots(orders)

    def as_updateSlotS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSlot(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\slotspanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:36 St�edn� Evropa (letn� �as)
