# 2016.10.11 22:10:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/flag_nots.py
from gui.Scaleform.daapi.view.meta.FlagNotificationMeta import FlagNotificationMeta
from gui.Scaleform.genConsts.FLAG_NOTIFICATION_CONSTS import FLAG_NOTIFICATION_CONSTS
from gui.battle_control import g_sessionProvider
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as _STATE
from gui.battle_control.controllers.flag_nots_ctrl import IFlagNotificationView

class FlagNotification(FlagNotificationMeta, IFlagNotificationView):

    def showFlagDelivered(self):
        self.as_setStateS(FLAG_NOTIFICATION_CONSTS.STATE_FLAG_DELIVERED)

    def showFlagDropped(self):
        self.as_setStateS(FLAG_NOTIFICATION_CONSTS.STATE_FLAG_DROPPED)

    def showFlagAbsorbed(self):
        self.as_setStateS(FLAG_NOTIFICATION_CONSTS.STATE_FLAG_ABSORBED)

    def showFlagCaptured(self):
        self.as_setStateS(FLAG_NOTIFICATION_CONSTS.STATE_FLAG_CAPTURED)

    def _populate(self):
        super(FlagNotification, self)._populate()
        ctrl = g_sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleStateUpdated += self.__onVehicleStateUpdated
        return

    def _dispose(self):
        ctrl = g_sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleStateUpdated -= self.__onVehicleStateUpdated
        super(FlagNotification, self)._dispose()
        return

    def __onVehicleStateUpdated(self, state, value):
        if state == _STATE.FIRE:
            self.as_setActiveS(not value)
        elif state in (_STATE.SHOW_DESTROY_TIMER, _STATE.SHOW_DEATHZONE_TIMER):
            self.as_setActiveS(False)
        elif state in (_STATE.HIDE_DESTROY_TIMER, _STATE.HIDE_DEATHZONE_TIMER):
            self.as_setActiveS(True)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\fallout\flag_nots.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:36 St�edn� Evropa (letn� �as)
