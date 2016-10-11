# 2016.10.11 22:12:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialHangarQuestDetailsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TutorialHangarQuestDetailsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def requestQuestInfo(self, questID):
        self._printOverrideError('requestQuestInfo')

    def showTip(self, id, type):
        self._printOverrideError('showTip')

    def getSortedTableData(self, data):
        self._printOverrideError('getSortedTableData')

    def as_updateQuestInfoS(self, data):
        """
        :param data: Represented by TutorialHangarQuestDetailsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestInfo(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\tutorialhangarquestdetailsmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:39 Støední Evropa (letní èas)
