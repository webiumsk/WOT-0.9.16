# 2016.10.11 22:12:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EULAMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class EULAMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def requestEULAText(self):
        self._printOverrideError('requestEULAText')

    def onLinkClick(self, url):
        self._printOverrideError('onLinkClick')

    def onApply(self):
        self._printOverrideError('onApply')

    def as_setEULATextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setEULAText(text)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\eulameta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:24 Støední Evropa (letní èas)
