# 2016.10.11 22:12:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RibbonsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RibbonsPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onShow(self):
        self._printOverrideError('onShow')

    def onChange(self):
        self._printOverrideError('onChange')

    def onHide(self, ribbonType):
        self._printOverrideError('onHide')

    def as_setupS(self, items, isExtendedAnim, isVisible, isWithRibbonName, isWithVehName):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(items, isExtendedAnim, isVisible, isWithRibbonName, isWithVehName)

    def as_addBattleEfficiencyEventS(self, ribbonType, leftFieldStr, vehName, vehType, rightFieldStr):
        if self._isDAAPIInited():
            return self.flashObject.as_addBattleEfficiencyEvent(ribbonType, leftFieldStr, vehName, vehType, rightFieldStr)

    def as_setSettingsS(self, isVisible, isExtendedAnim, isWithRibbonName, isWithVehName):
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(isVisible, isExtendedAnim, isWithRibbonName, isWithVehName)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\ribbonspanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:35 St�edn� Evropa (letn� �as)
