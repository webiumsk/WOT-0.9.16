# 2016.10.11 22:10:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/fallout/full_stats.py
from gui.Scaleform.daapi.view.meta.FCStatsMeta import FCStatsMeta
from gui.Scaleform.daapi.view.meta.FMStatsMeta import FMStatsMeta
from gui.battle_control import g_sessionProvider

class FalloutClassicFullStats(FCStatsMeta):
    pass


class FalloutMultiTeamFullStats(FMStatsMeta):

    def _populate(self):
        super(FalloutMultiTeamFullStats, self)._populate()
        self.as_setSubTypeS(g_sessionProvider.getArenaDP().getMultiTeamsType())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\fallout\full_stats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:36 Støední Evropa (letní èas)
