# 2016.10.11 22:10:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/score_panel.py
from gui.Scaleform.daapi.view.meta.FalloutBaseScorePanelMeta import FalloutBaseScorePanelMeta
from gui.battle_control import g_sessionProvider
_WARNING_RATIO = 0.8

class FalloutScorePanel(FalloutBaseScorePanelMeta):

    def _populate(self):
        super(FalloutScorePanel, self)._populate()
        visitor = g_sessionProvider.arenaVisitor
        maxWinPoints = visitor.type.getWinPointsCAP()
        self.as_initS(maxWinPoints, maxWinPoints * _WARNING_RATIO)
        ctrl = g_sessionProvider.dynamic.gasAttack
        if ctrl is not None:
            ctrl.onPreparing += self.__onGasAttackPreparing
            ctrl.onStarted += self.__onGasAttackStarted
        return

    def _dispose(self):
        ctrl = g_sessionProvider.dynamic.gasAttack
        if ctrl is not None:
            ctrl.onPreparing -= self.__onGasAttackPreparing
            ctrl.onStarted -= self.__onGasAttackStarted
        super(FalloutScorePanel, self)._dispose()
        return

    def __onGasAttackPreparing(self, _):
        self.as_playScoreHighlightAnimS()

    def __onGasAttackStarted(self, _):
        self.as_stopScoreHighlightAnimS()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\fallout\score_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:38 Støední Evropa (letní èas)
