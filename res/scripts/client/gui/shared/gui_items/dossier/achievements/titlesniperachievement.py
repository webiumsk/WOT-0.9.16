# 2016.10.11 22:13:54 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/TitleSniperAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class TitleSniperAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(TitleSniperAchievement, self).__init__('titleSniper', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'sniperSeries'), (_AB.TOTAL, 'maxSniperSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\titlesniperachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:13:55 St�edn� Evropa (letn� �as)
