# 2016.10.11 22:12:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ResearchPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def goToResearch(self):
        self._printOverrideError('goToResearch')

    def addVehToCompare(self):
        self._printOverrideError('addVehToCompare')

    def as_updateCurrentVehicleS(self, data):
        """
        :param data: Represented by ResearchPanelVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateCurrentVehicle(data)

    def as_setEarnedXPS(self, earnedXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setEarnedXP(earnedXP)

    def as_setEliteS(self, isElite):
        if self._isDAAPIInited():
            return self.flashObject.as_setElite(isElite)

    def as_setIGRLabelS(self, visible, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIGRLabel(visible, value)

    def as_actionIGRDaysLeftS(self, visible, value):
        if self._isDAAPIInited():
            return self.flashObject.as_actionIGRDaysLeft(visible, value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\researchpanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:35 St�edn� Evropa (letn� �as)
