# 2016.10.11 22:13:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/DiehardAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class DiehardAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(DiehardAchievement, self).__init__('diehard', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'diehardSeries'), (_AB.TOTAL, 'maxDiehardSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\diehardachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:13:50 St�edn� Evropa (letn� �as)
