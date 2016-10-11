# 2016.10.11 22:10:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/battle_timer.py
from gui.Scaleform.daapi.view.battle.shared.battle_timers import BattleTimer
FALLOUT_ENDING_SOON_TIME = 120

class FalloutBattleTimer(BattleTimer):

    def __init__(self):
        super(FalloutBattleTimer, self).__init__()

    def _getEndingSoonTime(self):
        return FALLOUT_ENDING_SOON_TIME
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\fallout\battle_timer.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:36 Støední Evropa (letní èas)
