# 2016.10.11 22:12:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortCreationCongratulationsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortCreationCongratulationsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setText(value)

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setButtonLblS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonLbl(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortcreationcongratulationswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:26 St�edn� Evropa (letn� �as)
