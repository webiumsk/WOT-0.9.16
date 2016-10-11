# 2016.10.11 22:12:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationStaffViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StaticFormationStaffViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showRecriutmentWindow(self):
        self._printOverrideError('showRecriutmentWindow')

    def showInviteWindow(self):
        self._printOverrideError('showInviteWindow')

    def setRecruitmentOpened(self, opened):
        self._printOverrideError('setRecruitmentOpened')

    def removeMe(self):
        self._printOverrideError('removeMe')

    def removeMember(self, id, userName):
        self._printOverrideError('removeMember')

    def assignOfficer(self, id, userName):
        self._printOverrideError('assignOfficer')

    def assignPrivate(self, id, userName):
        self._printOverrideError('assignPrivate')

    def as_setStaticHeaderDataS(self, data):
        """
        :param data: Represented by StaticFormationStaffViewStaticHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticHeaderData(data)

    def as_updateHeaderDataS(self, data):
        """
        :param data: Represented by StaticFormationStaffViewHeaderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateHeaderData(data)

    def as_updateStaffDataS(self, data):
        """
        :param data: Represented by StaticFormationStaffViewStaffVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateStaffData(data)

    def as_setRecruitmentAvailabilityS(self, available):
        if self._isDAAPIInited():
            return self.flashObject.as_setRecruitmentAvailability(available)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\staticformationstaffviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:37 Støední Evropa (letní èas)
