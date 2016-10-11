# 2016.10.11 22:12:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StatsBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StatsBaseMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def acceptSquad(self, uid):
        self._printOverrideError('acceptSquad')

    def addToSquad(self, uid):
        self._printOverrideError('addToSquad')

    def as_setIsIntaractiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsIntaractive(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\statsbasemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:37 Støední Evropa (letní èas)
