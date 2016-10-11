# 2016.10.11 22:12:31 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationsListMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NotificationsListMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def onGroupChange(self, groupIdx):
        self._printOverrideError('onGroupChange')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by NotificationViewInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setMessagesListS(self, data):
        """
        :param data: Represented by NotificationMessagesListVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagesList(data)

    def as_appendMessageS(self, data):
        """
        :param data: Represented by NotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(data)

    def as_updateMessageS(self, data):
        """
        :param data: Represented by NotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(data)

    def as_updateCountersS(self, counts):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounters(counts)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\notificationslistmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:31 Støední Evropa (letní èas)
