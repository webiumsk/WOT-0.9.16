# 2016.10.11 22:14:53 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelsManagementWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelsManagementWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def getSearchLimitLabel(self):
        self._printOverrideError('getSearchLimitLabel')

    def searchToken(self, token):
        self._printOverrideError('searchToken')

    def joinToChannel(self, index):
        self._printOverrideError('joinToChannel')

    def createChannel(self, name, usePassword, password, retype):
        self._printOverrideError('createChannel')

    def as_freezSearchButtonS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_freezSearchButton(isEnable)

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\channelsmanagementwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:14:53 St�edn� Evropa (letn� �as)
