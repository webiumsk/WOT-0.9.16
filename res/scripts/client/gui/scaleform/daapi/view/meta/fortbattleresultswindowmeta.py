# 2016.10.11 22:12:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleResultsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortBattleResultsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def getMoreInfo(self, battleID):
        self._printOverrideError('getMoreInfo')

    def getClanEmblem(self):
        self._printOverrideError('getClanEmblem')

    def as_setDataS(self, data):
        """
        :param data: Represented by BattleResultsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_notAvailableInfoS(self, battleID):
        if self._isDAAPIInited():
            return self.flashObject.as_notAvailableInfo(battleID)

    def as_setClanEmblemS(self, iconTag):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(iconTag)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortbattleresultswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:25 Støední Evropa (letní èas)
