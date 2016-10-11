# 2016.10.11 22:09:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/hit_direction_ctrl.py
from functools import partial
import weakref
import BigWorld
from account_helpers.settings_core.settings_constants import DAMAGE_INDICATOR, GRAPHICS
from account_helpers.settings_core.SettingsCore import g_settingsCore
from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN, BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import GameEvent
from gui.battle_control.battle_constants import HIT_FLAGS
from shared_utils import CONST_CONTAINER
_AGGREGATED_HIT_BITS = HIT_FLAGS.IS_BLOCKED | HIT_FLAGS.HP_DAMAGE | HIT_FLAGS.IS_CRITICAL
_VISUAL_DAMAGE_INDICATOR_SETTINGS = (DAMAGE_INDICATOR.TYPE,
 DAMAGE_INDICATOR.VEHICLE_INFO,
 DAMAGE_INDICATOR.DAMAGE_VALUE,
 DAMAGE_INDICATOR.ANIMATION,
 GRAPHICS.COLOR_BLIND)

class DAMAGE_INDICATOR_PRESETS(CONST_CONTAINER):
    ALL = (0,)
    WITHOUT_CRITS = 1


class IHitIndicator(object):

    def destroy(self):
        raise NotImplementedError

    def getDuration(self):
        raise NotImplementedError

    def getBeginAnimationDuration(self):
        raise NotImplementedError

    def setVisible(self, flag):
        raise NotImplementedError

    def showHitDirection(self, idx, hitData, timeLeft):
        raise NotImplementedError

    def hideHitDirection(self, idx):
        raise NotImplementedError


class _HitDirection(object):
    __slots__ = ('__idx', '__hitData', '__isDamage', '__startTime', '__isShown', '__isVisible', '__offset', '__indicator')

    def __init__(self, idx):
        super(_HitDirection, self).__init__()
        self.__idx = idx
        self.__hitData = None
        self.__startTime = 0
        self.__isShown = False
        self.__indicator = None
        return

    def __repr__(self):
        return '_HitDirection(idx={0}, hitData={1}, startTime={2}, isShown={3}, hasUI={4})'.format(self.__idx, self.__hitData, self.__startTime, self.__isShown, self.__indicator is not None)

    def clear(self):
        self.__hitData = None
        self.__startTime = 0
        self.__isShown = False
        self.__indicator = None
        return

    def getIndex(self):
        return self.__idx

    def getHitData(self):
        return self.__hitData

    def isShown(self):
        return self.__isShown

    def getIndicator(self):
        return self.__indicator

    def getTimeLeft(self):
        if self.__isShown:
            timeLeft = BigWorld.time() - self.__startTime
        else:
            timeLeft = 0
        return timeLeft

    def getStartTime(self):
        return self.__startTime

    def setIndicator(self, indicator):
        self.__indicator = indicator
        return self.redraw()

    def redraw(self):
        """
        Redraw indicator if it is visible.
        
        :return: Animation duration.
        """
        duration = 0
        if self.__isShown and self.__hitData is not None and self.__indicator is not None:
            timeLeft = BigWorld.time() - self.__startTime
            duration = self.__indicator.getDuration()
            if timeLeft < duration:
                self.__indicator.showHitDirection(self.__idx, self.__hitData, timeLeft)
            else:
                duration = 0
        return duration

    def show(self, hitData, extend = False):
        """
        Show indicator with the given hit data.
        
        :param hitData: An instance of HitData
        :param extend: If True, current hit data will be extended with the given one.
        :return: Animation duration
        """
        self.__isShown = True
        self.__startTime = BigWorld.time()
        extend = extend and self.__hitData is not None
        if extend:
            self.__hitData.extend(hitData)
        else:
            self.__hitData = hitData
        duration = self.__indicator and self.__indicator.getDuration()
        timeLeft = self.__indicator.getBeginAnimationDuration() if extend else 0
        if not duration:
            raise AssertionError('Duration should be more than 0')
            self.__indicator.showHitDirection(self.__idx, self.__hitData, timeLeft)
        else:
            duration = 0
        return duration

    def hide(self):
        if not self.__isShown:
            return
        self.__isShown = False
        if self.__indicator:
            self.__indicator.hideHitDirection(self.__idx)


class HitDirectionController(IViewComponentsController):
    __slots__ = ('__pull', '__ui', '__isVisible', '__callbackIDs', '__damageIndicatorPreset', '__weakref__')

    def __init__(self):
        super(HitDirectionController, self).__init__()
        raise HIT_INDICATOR_MAX_ON_SCREEN or AssertionError('Can not be zero')
        self.__pull = [ _HitDirection(idx_) for idx_ in xrange(HIT_INDICATOR_MAX_ON_SCREEN) ]
        self.__ui = None
        self.__isVisible = True
        self.__callbackIDs = {}
        self.__damageIndicatorPreset = DAMAGE_INDICATOR_PRESETS.ALL
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.HIT_DIRECTION

    def startControl(self):
        g_eventBus.addListener(GameEvent.GUI_VISIBILITY, self.__handleGUIVisibility, scope=EVENT_BUS_SCOPE.BATTLE)
        self.__damageIndicatorPreset = g_settingsCore.getSetting(DAMAGE_INDICATOR.PRESETS)
        g_settingsCore.onSettingsChanged += self.__onSettingsChanged

    def stopControl(self):
        g_settingsCore.onSettingsChanged -= self.__onSettingsChanged
        g_eventBus.removeListener(GameEvent.GUI_VISIBILITY, self.__handleGUIVisibility, scope=EVENT_BUS_SCOPE.BATTLE)
        self.__clearHideCallbacks()

    def getHit(self, idx):
        if idx < len(self.__pull):
            hit = self.__pull[idx]
        else:
            hit = None
        return hit

    def isVisible(self):
        return self.__isVisible

    def setVisible(self, flag):
        self.__isVisible = flag
        if self.__ui:
            self.__ui.setVisible(flag)

    def setViewComponents(self, component):
        self.__ui = component
        self.__ui.invalidateSettings()
        self.__ui.setVisible(self.__isVisible)
        proxy = weakref.proxy(self.__ui)
        for hit in self.__pull:
            idx = hit.getIndex()
            duration = hit.setIndicator(proxy)
            if duration:
                self.__callbackIDs[idx] = BigWorld.callback(duration, partial(self.__tickToHideHit, idx))

    def clearViewComponents(self):
        for hit in self.__pull:
            hit.clear()

        if self.__ui:
            self.__ui.destroy()
        self.__ui = None
        return

    def addHit(self, hitData):
        """
        Add a new hit to control.
        
        :param hitData: An instance of HitData
        """
        if not self._isValidHit(hitData):
            return
        else:
            hit = self.__findHit(hitData)
            if hit is None:
                extendHitData = False
                hit = self.__getNextHit()
            else:
                extendHitData = hit.isShown()
            idx = hit.getIndex()
            self.__clearHideCallback(idx)
            duration = hit.show(hitData, extend=extendHitData)
            if duration:
                self.__callbackIDs[idx] = BigWorld.callback(duration, partial(self.__tickToHideHit, idx))
            return hit

    def _isValidHit(self, hitData):
        """
        Validates that hit with the given data should be displayed to the user.
        Do not show damage indicator if:
        1. it is caused by battle consumables.
        2. it is critical hit without damage and crits are disabled in user's preferences
        
        :param hitData: An instance of HitData
        :return: True if hit is valid and should be shown, otherwise False.
        """
        if hitData.isBattleConsumables():
            return False
        if self.__damageIndicatorPreset == DAMAGE_INDICATOR_PRESETS.WITHOUT_CRITS and hitData.isCritical() and hitData.getDamage() == 0:
            return False
        return True

    def __getNextHit(self):
        find = self.__pull[0]
        for hit in self.__pull:
            if not hit.isShown():
                return hit
            if hit.getStartTime() < find.getStartTime():
                find = hit

        return find

    def __findHit(self, hitData):
        """
        Finds an appropriate damage indicator according to the following aggregation rules:
        1. Hits are aggregated by target ID.
        2. Blocked hit can be aggregated only with another blocked hit (aggregated value - damage).
        3. Critical hit without HP damage can be aggregated only with another critical hit
           without HP damage (aggregated value - crits count).
        4. Any not blocked hit with HP damage (including with crits) can be aggregated with
           another not blocked hit with HP damage (aggregated value - damage and crits count)
        
        :param hitData: An instance of HitData
        :return: _HitDirection instance corresponding to the rules listed above or None.
        """
        for hit in self.__pull:
            data = hit.getHitData()
            if data is not None:
                if hitData.getAttackerID() == data.getAttackerID():
                    currentMask = data.getHitFlags() & _AGGREGATED_HIT_BITS
                    newMask = hitData.getHitFlags() & _AGGREGATED_HIT_BITS
                    if currentMask > 0:
                        if currentMask == newMask:
                            return hit
                        if currentMask == HIT_FLAGS.HP_DAMAGE and newMask == HIT_FLAGS.HP_DAMAGE | HIT_FLAGS.IS_CRITICAL:
                            return hit
                        if currentMask == HIT_FLAGS.HP_DAMAGE | HIT_FLAGS.IS_CRITICAL and newMask == HIT_FLAGS.HP_DAMAGE:
                            return hit

        return

    def __tickToHideHit(self, idx):
        self.__callbackIDs.pop(idx, None)
        self.__pull[idx].hide()
        return

    def __clearHideCallback(self, idx):
        callbackID = self.__callbackIDs.pop(idx, None)
        if callbackID is not None:
            BigWorld.cancelCallback(callbackID)
        return

    def __clearHideCallbacks(self):
        for _, callbackID in self.__callbackIDs.items():
            if callbackID is not None:
                BigWorld.cancelCallback(callbackID)

        self.__callbackIDs.clear()
        return

    def __handleGUIVisibility(self, event):
        self.setVisible(event.ctx['visible'])

    def __onSettingsChanged(self, diff):
        if DAMAGE_INDICATOR.PRESETS in diff:
            self.__damageIndicatorPreset = diff[DAMAGE_INDICATOR.PRESETS]
        if self.__ui is not None:
            for key in _VISUAL_DAMAGE_INDICATOR_SETTINGS:
                if key in diff:
                    self.__ui.invalidateSettings()
                    for hit in self.__pull:
                        hit.redraw()

                    break

        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\battle_control\controllers\hit_direction_ctrl.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:09:34 St�edn� Evropa (letn� �as)
