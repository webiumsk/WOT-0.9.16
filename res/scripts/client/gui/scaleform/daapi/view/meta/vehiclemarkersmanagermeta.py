# 2016.10.11 22:12:40 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleMarkersManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleMarkersManagerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setMarkerDurationS(self, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_setMarkerDuration(duration)

    def as_setMarkerSettingsS(self, settings):
        if self._isDAAPIInited():
            return self.flashObject.as_setMarkerSettings(settings)

    def as_setShowExInfoFlagS(self, flag):
        if self._isDAAPIInited():
            return self.flashObject.as_setShowExInfoFlag(flag)

    def as_updateMarkersSettingsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMarkersSettings()

    def as_setColorBlindS(self, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorBlind(isColorBlind)

    def as_setColorSchemesS(self, defaultSchemes, colorBlindSchemes):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorSchemes(defaultSchemes, colorBlindSchemes)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\vehiclemarkersmanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:40 St�edn� Evropa (letn� �as)
