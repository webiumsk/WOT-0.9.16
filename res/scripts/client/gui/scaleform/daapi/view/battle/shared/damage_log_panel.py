# 2016.10.11 22:10:40 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/damage_log_panel.py
import weakref
import BigWorld
import BattleReplay
from shared_utils import BitmaskHelper
from account_helpers.settings_core.SettingsCore import g_settingsCore
from account_helpers.settings_core.settings_constants import DAMAGE_LOG
from gui.shared import events, EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.BattleDamageLogPanelMeta import BattleDamageLogPanelMeta
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _ETYPE
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as _BET
from gui.Scaleform.genConsts.BATTLEDAMAGELOG_IMAGES import BATTLEDAMAGELOG_IMAGES as _IMAGES
from gui.battle_control import g_sessionProvider

class _DETAILS_LOG_VIEW_MODE(object):
    UNDEFINED = -1
    SHOW_ALWAYS = 0
    SHOW_BY_ALT_PRESS = 1
    HIDE = 2


_VEHICLE_CLASS_TAGS_ICONS = {'lightTank': _IMAGES.WHITE_ICON_LIGHTTANK_16X16,
 'mediumTank': _IMAGES.WHITE_ICON_MEDIUM_TANK_16X16,
 'heavyTank': _IMAGES.WHITE_ICON_HEAVYTANK_16X16,
 'SPG': _IMAGES.WHITE_ICON_SPG_16X16,
 'AT-SPG': _IMAGES.WHITE_ICON_AT_SPG_16X16}
_TEXT_COLOR_WHITE = 16777215

def _summaryDamageFormatter(value):
    return BigWorld.wg_getIntegralFormat(value)


def _logDamageFormatter(value):
    return BigWorld.wg_getIntegralFormat(value)


class DamageLogPanel(BattleDamageLogPanelMeta):

    def __init__(self):
        super(DamageLogPanel, self).__init__()
        self.__efficiencyCtrl = None
        self.__arenaDP = g_sessionProvider.getCtx().getArenaDP()
        self.__vehStateCtrl = g_sessionProvider.shared.vehicleState
        self.__logViewMode = _DETAILS_LOG_VIEW_MODE.UNDEFINED
        self.__contentMask = 0
        self.__isVisible = True
        return

    def _populate(self):
        super(DamageLogPanel, self)._populate()
        self.__efficiencyCtrl = g_sessionProvider.shared.personalEfficiencyCtrl
        settingGetter = g_settingsCore.getSetting
        self._invalidateComponentVisibility()
        if self.__efficiencyCtrl is not None:
            self._updateContent(settingGetter(DAMAGE_LOG.SHOW_DETAILS), settingGetter(DAMAGE_LOG.TOTAL_DAMAGE), settingGetter(DAMAGE_LOG.BLOCKED_DAMAGE), settingGetter(DAMAGE_LOG.ASSIST_DAMAGE))
            self.__efficiencyCtrl.onTotalEfficiencyUpdated += self._onTotalEfficiencyUpdated
            self.__efficiencyCtrl.onPersonalEfficiencyReceived += self._onEfficiencyReceived
        g_settingsCore.onSettingsChanged += self._onSettingsChanged
        if self.__vehStateCtrl is not None:
            self.__vehStateCtrl.onPostMortemSwitched += self._onPostMortemSwitched
            self.__vehStateCtrl.onVehicleControlling += self._onVehicleControlling
        self.addListener(events.GameEvent.SHOW_EXTENDED_INFO, self._handleShowExtendedInfo, scope=EVENT_BUS_SCOPE.BATTLE)
        self.addListener(events.GameEvent.SHOW_CURSOR, self._handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self._handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        return

    def _dispose(self):
        self.removeListener(events.GameEvent.SHOW_EXTENDED_INFO, self._handleShowExtendedInfo, EVENT_BUS_SCOPE.BATTLE)
        self.removeListener(events.GameEvent.SHOW_CURSOR, self._handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self._handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        if self.__vehStateCtrl is not None:
            self.__vehStateCtrl.onPostMortemSwitched -= self._onPostMortemSwitched
            self.__vehStateCtrl.onVehicleControlling -= self._onVehicleControlling
        g_settingsCore.onSettingsChanged -= self._onSettingsChanged
        if self.__efficiencyCtrl is not None:
            self.__efficiencyCtrl.onTotalEfficiencyUpdated -= self._onTotalEfficiencyUpdated
            self.__efficiencyCtrl.onPersonalEfficiencyReceived -= self._onEfficiencyReceived
            self.__efficiencyCtrl = None
        self.__vehStateCtrl = None
        self.__arenaDP = None
        super(DamageLogPanel, self)._dispose()
        return

    def _updateContent(self, mode, showDamage, showBlockedDamage, showAssistDamage):
        needUpdate = False
        if mode != self.__logViewMode:
            self.__logViewMode = mode
            needUpdate = True
        contentMask = 0
        if showDamage:
            contentMask |= _ETYPE.DAMAGE
        if showBlockedDamage:
            contentMask |= _ETYPE.BLOCKED_DAMAGE
        if showAssistDamage:
            contentMask |= _ETYPE.ASSIST_DAMAGE
        if contentMask != self.__contentMask:
            self.__contentMask = contentMask
            needUpdate = True
        if needUpdate:
            self._invalidateTotalDamages()
            if self.__logViewMode == _DETAILS_LOG_VIEW_MODE.SHOW_ALWAYS:
                isVisible = True
                messages = self._getLogMessages(self.__contentMask)
            elif self.__logViewMode == _DETAILS_LOG_VIEW_MODE.SHOW_BY_ALT_PRESS:
                isVisible = False
                messages = self._getLogMessages(self.__contentMask)
            else:
                isVisible = False
                messages = []
            self.as_detailStatsS(isVisible, messages)

    def _getLogMessages(self, contentMask):
        if self.__efficiencyCtrl is not None:
            records = self.__efficiencyCtrl.getLoogedEfficiency(contentMask)
            return [ self._buildLogMessageVO(r) for r in records ]
        else:
            return []

    def _getVehicleTypeInfoVO(self, arenaVehicleID):
        if self.__arenaDP is None:
            return
        else:
            return self.__arenaDP.getVehicleInfo(arenaVehicleID).vehicleType

    def _onTotalEfficiencyUpdated(self, diff):
        if _ETYPE.DAMAGE in diff:
            self.as_updateSummaryDamageValueS(self.__formatTotalDamage(_ETYPE.DAMAGE, diff[_ETYPE.DAMAGE]))
        if _ETYPE.BLOCKED_DAMAGE in diff:
            self.as_updateSummaryBlockedValueS(self.__formatTotalDamage(_ETYPE.BLOCKED_DAMAGE, diff[_ETYPE.BLOCKED_DAMAGE]))
        if _ETYPE.ASSIST_DAMAGE in diff:
            self.as_updateSummaryAssistValueS(self.__formatTotalDamage(_ETYPE.ASSIST_DAMAGE, diff[_ETYPE.ASSIST_DAMAGE]))

    def _onEfficiencyReceived(self, events):
        if self.__logViewMode == _DETAILS_LOG_VIEW_MODE.HIDE:
            return
        for e in events:
            if BitmaskHelper.hasAnyBitSet(self.__contentMask, e.getType()):
                vo = self._buildLogMessageVO(e)
                self.as_addDetailMessageS(**vo)

    def _invalidateTotalDamages(self):
        getter = self.__efficiencyCtrl.getTotalEfficiency
        self.as_summaryStatsS(self.__formatTotalDamage(_ETYPE.DAMAGE, getter(_ETYPE.DAMAGE)), self.__formatTotalDamage(_ETYPE.BLOCKED_DAMAGE, getter(_ETYPE.BLOCKED_DAMAGE)), self.__formatTotalDamage(_ETYPE.ASSIST_DAMAGE, getter(_ETYPE.ASSIST_DAMAGE)))

    def _invalidateComponentVisibility(self):
        isVisible = True
        if BattleReplay.g_replayCtrl.isPlaying:
            isVisible = False
        elif self.__vehStateCtrl is None:
            isVisible = self.__isVisible
        elif self.__vehStateCtrl.isInPostmortem:
            if self.__arenaDP is None:
                isVisible = self.__isVisible
            else:
                observedVehID = self.__vehStateCtrl.getControllingVehicleID()
                isVisible = self.__arenaDP.getPlayerVehicleID() == observedVehID
        if self.__isVisible != isVisible:
            self.__isVisible = isVisible
            self.as_showDamageLogComponentS(isVisible)
        return

    def _onSettingsChanged(self, diff):
        settingGetter = g_settingsCore.getSetting
        if DAMAGE_LOG.SHOW_DETAILS in diff or DAMAGE_LOG.TOTAL_DAMAGE in diff or DAMAGE_LOG.ASSIST_DAMAGE in diff or DAMAGE_LOG.BLOCKED_DAMAGE in diff:
            self._updateContent(settingGetter(DAMAGE_LOG.SHOW_DETAILS), settingGetter(DAMAGE_LOG.TOTAL_DAMAGE), settingGetter(DAMAGE_LOG.BLOCKED_DAMAGE), settingGetter(DAMAGE_LOG.ASSIST_DAMAGE))

    def _buildLogMessageVO(self, info):
        actionTypeImg = ''
        if info.getType() == _ETYPE.DAMAGE:
            if info.isShot():
                actionTypeImg = _IMAGES.DAMAGELOG_DAMAGE_16X16
            elif info.isFire():
                actionTypeImg = _IMAGES.DAMAGELOG_FIRE_16X16
            else:
                actionTypeImg = _IMAGES.DAMAGELOG_RAM_16X16
        elif info.getType() == _ETYPE.BLOCKED_DAMAGE:
            actionTypeImg = _IMAGES.DAMAGELOG_REFLECT_16X16
        elif info.getType() == _ETYPE.ASSIST_DAMAGE:
            if info.getBattleEventType() == _BET.TRACK_ASSIST:
                actionTypeImg = _IMAGES.DAMAGELOG_IMMOBILIZED_16X16
            elif info.getBattleEventType() == _BET.RADIO_ASSIST:
                actionTypeImg = _IMAGES.DAMAGELOG_COORDINATE_16X16
        vTypeInfoVO = self._getVehicleTypeInfoVO(info.getArenaVehicleID())
        if vTypeInfoVO is not None:
            vehicleTypeImg = _VEHICLE_CLASS_TAGS_ICONS.get(vTypeInfoVO.classTag, '')
            vehicleName = vTypeInfoVO.shortNameWithPrefix
        else:
            vehicleTypeImg = ''
            vehicleName = ''
        return {'valueColor': _TEXT_COLOR_WHITE,
         'value': _logDamageFormatter(info.getDamage()),
         'actionTypeImg': actionTypeImg,
         'vehicleTypeImg': vehicleTypeImg,
         'vehicleName': vehicleName}

    def _onPostMortemSwitched(self):
        self._invalidateComponentVisibility()

    def _onVehicleControlling(self, vehicle):
        self._invalidateComponentVisibility()

    def _handleShowExtendedInfo(self, event):
        """
        Callback on Alt button press event. Shows/hides detailed damage log.
        :param isVisible: Is Alt button is pressed.
        """
        if self.__logViewMode == _DETAILS_LOG_VIEW_MODE.SHOW_BY_ALT_PRESS:
            self.as_isDownAltButtonS(event.ctx['isDown'])

    def _handleShowCursor(self, _):
        """
        Callback on Ctrl button press event. Enables scrolling of detailed damage log.
        """
        self.as_isDownCtrlButtonS(True)

    def _handleHideCursor(self, _):
        """
        Callback on Ctrl button release event. Disables scrolling of detailed damage log.
        """
        self.as_isDownCtrlButtonS(False)

    def __formatTotalDamage(self, etype, value):
        if BitmaskHelper.hasAnyBitSet(self.__contentMask, etype):
            return _summaryDamageFormatter(value)
        else:
            return None
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\shared\damage_log_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:40 St�edn� Evropa (letn� �as)
