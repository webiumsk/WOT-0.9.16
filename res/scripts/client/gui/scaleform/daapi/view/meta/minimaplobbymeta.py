# 2016.10.11 22:12:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapLobbyMeta.py
from gui.Scaleform.daapi.view.meta.MinimapEntityMeta import MinimapEntityMeta

class MinimapLobbyMeta(MinimapEntityMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends MinimapEntityMeta
    """

    def setMap(self, arenaID):
        self._printOverrideError('setMap')

    def setMinimapData(self, arenaID, playerTeam, size):
        self._printOverrideError('setMinimapData')

    def as_changeMapS(self, texture):
        if self._isDAAPIInited():
            return self.flashObject.as_changeMap(texture)

    def as_addPointS(self, x, y, type, color, id):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoint(x, y, type, color, id)

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\minimaplobbymeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:31 St�edn� Evropa (letn� �as)
