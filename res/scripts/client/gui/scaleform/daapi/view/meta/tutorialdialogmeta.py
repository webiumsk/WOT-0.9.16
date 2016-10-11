# 2016.10.11 22:12:39 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TutorialDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self):
        self._printOverrideError('submit')

    def cancel(self):
        self._printOverrideError('cancel')

    def as_setContentS(self, data):
        """
        :param data: Represented by TutorialDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setContent(data)

    def as_updateContentS(self, data):
        """
        :param data: Represented by TutorialDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateContent(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\tutorialdialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:39 Støední Evropa (letní èas)
