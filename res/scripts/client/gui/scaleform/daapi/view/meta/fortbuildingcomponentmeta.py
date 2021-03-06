# 2016.10.11 22:12:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBuildingComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortBuildingComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onTransportingRequest(self, exportFrom, importTo):
        self._printOverrideError('onTransportingRequest')

    def requestBuildingProcess(self, direction, position):
        self._printOverrideError('requestBuildingProcess')

    def upgradeVisitedBuilding(self, uid):
        self._printOverrideError('upgradeVisitedBuilding')

    def requestBuildingToolTipData(self, uid, type):
        self._printOverrideError('requestBuildingToolTipData')

    def as_setDataS(self, data):
        """
        :param data: Represented by BuildingsComponentVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setBuildingDataS(self, data):
        """
        :param data: Represented by BuildingVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBuildingData(data)

    def as_setBuildingToolTipDataS(self, uid, type, header, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuildingToolTipData(uid, type, header, value)

    def as_refreshTransportingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refreshTransporting()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortbuildingcomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:25 St�edn� Evropa (letn� �as)
