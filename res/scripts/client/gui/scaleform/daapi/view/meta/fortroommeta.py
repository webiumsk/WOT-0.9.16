# 2016.10.11 22:12:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortRoomMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class FortRoomMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    """

    def showChangeDivisionWindow(self):
        self._printOverrideError('showChangeDivisionWindow')

    def as_showLegionariesCountS(self, isShow, msg, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_showLegionariesCount(isShow, msg, tooltip)

    def as_showLegionariesToolTipS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_showLegionariesToolTip(isShow)

    def as_showOrdersBgS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_showOrdersBg(isShow)

    def as_setChangeDivisionButtonEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeDivisionButtonEnabled(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortroommeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:28 St�edn� Evropa (letn� �as)
