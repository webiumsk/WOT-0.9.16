# 2016.10.11 22:12:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleParametersMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleParametersMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onParamClick(self, paramID):
        self._printOverrideError('onParamClick')

    def onListScroll(self):
        self._printOverrideError('onListScroll')

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_setRendererLnkS(self, rendererLnk):
        if self._isDAAPIInited():
            return self.flashObject.as_setRendererLnk(rendererLnk)

    def as_setIsParamsAnimatedS(self, isParamsAnimated):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsParamsAnimated(isParamsAnimated)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\vehicleparametersmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:40 Støední Evropa (letní èas)
