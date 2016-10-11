# 2016.10.11 22:13:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/EFC2016Achievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement
from abstract.mixins import Quest

class EFC2016Achievement(Quest, SeriesAchievement):

    def __init__(self, dossier, value = None):
        SeriesAchievement.__init__(self, 'EFC2016', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'EFC2016WinSeries'), (_AB.TOTAL, 'maxEFC2016WinSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\efc2016achievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:13:50 Støední Evropa (letní èas)
