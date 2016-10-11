# 2016.10.11 22:12:30 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MessengerBarMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MessengerBarMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def channelButtonClick(self):
        self._printOverrideError('channelButtonClick')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by MessegerBarInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setVehicleCompareCartButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleCompareCartButtonVisible(value)

    def as_openVehicleCompareCartPopoverS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_openVehicleCompareCartPopover(value)

    def as_showAddVehicleCompareAnimS(self, data):
        """
        :param data: Represented by VehicleCompareAnimVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showAddVehicleCompareAnim(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\messengerbarmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:30 Støední Evropa (letní èas)
