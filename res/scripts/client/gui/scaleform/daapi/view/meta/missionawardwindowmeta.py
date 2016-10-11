# 2016.10.11 22:12:31 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionAwardWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class MissionAwardWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onCurrentQuestClick(self):
        self._printOverrideError('onCurrentQuestClick')

    def onNextQuestClick(self):
        self._printOverrideError('onNextQuestClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by MissionAwardWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\missionawardwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:31 Støední Evropa (letní èas)
