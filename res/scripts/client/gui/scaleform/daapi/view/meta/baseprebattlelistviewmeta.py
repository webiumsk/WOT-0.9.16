# 2016.10.11 22:12:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BasePrebattleListViewMeta.py
from gui.Scaleform.daapi.view.lobby.rally.AbstractRallyView import AbstractRallyView

class BasePrebattleListViewMeta(AbstractRallyView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractRallyView
    """

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\baseprebattlelistviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:16 St�edn� Evropa (letn� �as)
