# 2016.10.11 22:12:25 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBuildingCardPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortBuildingCardPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def openUpgradeWindow(self, value):
        self._printOverrideError('openUpgradeWindow')

    def openAssignedPlayersWindow(self, value):
        self._printOverrideError('openAssignedPlayersWindow')

    def openDemountBuildingWindow(self, value):
        self._printOverrideError('openDemountBuildingWindow')

    def openDirectionControlWindow(self):
        self._printOverrideError('openDirectionControlWindow')

    def openBuyOrderWindow(self):
        self._printOverrideError('openBuyOrderWindow')

    def as_setDataS(self, data):
        """
        :param data: Represented by BuildingCardPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setModernizationDestructionEnablingS(self, modernizationButtonEnabled, destroyButtonEnabled, modernizationButtonTooltip, destroyButtonTooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setModernizationDestructionEnabling(modernizationButtonEnabled, destroyButtonEnabled, modernizationButtonTooltip, destroyButtonTooltip)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortbuildingcardpopovermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:25 St�edn� Evropa (letn� �as)
