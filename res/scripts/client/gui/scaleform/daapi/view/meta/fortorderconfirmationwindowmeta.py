# 2016.10.11 22:12:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortOrderConfirmationWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortOrderConfirmationWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self, count):
        self._printOverrideError('submit')

    def getTimeStr(self, time):
        self._printOverrideError('getTimeStr')

    def as_setDataS(self, data):
        """
        :param data: Represented by ConfirmOrderVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setSettingsS(self, data):
        """
        :param data: Represented by DialogSettingsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSettings(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortorderconfirmationwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:27 Støední Evropa (letní èas)
