# 2016.10.11 22:13:55 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/WinnerLaurelsAchievement.py
from abstract import ClassProgressAchievement
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract.mixins import Deprecated, NoProgressBar

class WinnerLaurelsAchievement(Deprecated, NoProgressBar, ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        super(WinnerLaurelsAchievement, self).__init__('winnerLaurels', _AB.FALLOUT, dossier, value)

    def getNextLevelInfo(self):
        return ('winPointsLeft', self._lvlUpValue)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.FALLOUT, 'winnerLaurels')

    def _readCurrentProgressValue(self, dossier):
        return dossier.getFalloutStats().getVictoryPoints()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\winnerlaurelsachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:13:55 Støední Evropa (letní èas)
