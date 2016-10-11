# 2016.10.11 22:10:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/classic/battle_end_warning_panel.py
import WWISE
from gui.battle_control import g_sessionProvider
from gui.Scaleform.daapi.view.meta.BattleEndWarningPanelMeta import BattleEndWarningPanelMeta
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE

class _WWISE_EVENTS:
    APPEAR = 'time_buzzer_01'


_WARNING_TEXT_KEY = '#ingame_gui:battleEndWarning/text'
_SWF_FILE_NAME = 'BattleEndWarningPanel.swf'
_CALLBACK_NAME = 'battle.onLoadEndWarningPanel'

class BattleEndWarningPanel(BattleEndWarningPanelMeta):

    def __init__(self):
        super(BattleEndWarningPanel, self).__init__()
        self.__arenaVisitor = self._getArenaVisitor()
        arenaType = self.__arenaVisitor.type
        self.__duration = arenaType.getBattleEndWarningDuration()
        self.__appearTime = arenaType.getBattleEndWarningAppearTime()
        self.__roundLength = arenaType.getRoundLength()
        self.__isShown = False
        self.__warningIsValid = self.__validateWarningTime()

    def isLoaded(self):
        return True

    def setCurrentTimeLeft(self, totalTime):
        minutes, seconds = divmod(int(totalTime), ONE_MINUTE)
        minutesStr = '{:02d}'.format(minutes)
        secondsStr = '{:02d}'.format(seconds)
        if self.__isShown:
            self.as_setTotalTimeS(minutesStr, secondsStr)
        if totalTime == self.__appearTime and self.__warningIsValid:
            self._callWWISE(_WWISE_EVENTS.APPEAR)
            self.as_setTotalTimeS(minutesStr, secondsStr)
            self.as_setTextInfoS(_ms(_WARNING_TEXT_KEY))
            self.as_setStateS(True)
            self.__isShown = True
        if totalTime <= self.__appearTime - self.__duration and self.__isShown:
            self.as_setStateS(False)
            self.__isShown = False

    def _getArenaVisitor(self):
        return g_sessionProvider.arenaVisitor

    def _callWWISE(self, wwiseEventName):
        """
        Method is used to play or stop sounds.
        
        Pretected for testing purposes.
        """
        WWISE.WW_eventGlobal(wwiseEventName)

    def __validateWarningTime(self):
        if self.__appearTime < self.__duration or self.__appearTime <= 0 or self.__duration <= 0 or self.__appearTime > self.__roundLength or self.__duration > self.__roundLength and self.__arenaVisitor.isBattleEndWarningEnabled():
            return False
        return True
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\classic\battle_end_warning_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:34 St�edn� Evropa (letn� �as)
