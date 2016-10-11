# 2016.10.11 22:14:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ConnectToSecureChannelWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConnectToSecureChannelWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def sendPassword(self, value):
        self._printOverrideError('sendPassword')

    def cancelPassword(self):
        self._printOverrideError('cancelPassword')

    def as_infoMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_infoMessage(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\connecttosecurechannelwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:14:53 Støední Evropa (letní èas)
