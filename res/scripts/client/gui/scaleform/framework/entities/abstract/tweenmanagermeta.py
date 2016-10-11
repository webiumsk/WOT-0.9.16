# 2016.10.11 22:12:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/TweenManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class TweenManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def createTween(self, tween):
        """
        :param tween: Represented by ITween (AS)
        """
        self._printOverrideError('createTween')

    def disposeTween(self, tween):
        """
        :param tween: Represented by ITween (AS)
        """
        self._printOverrideError('disposeTween')

    def disposeAll(self):
        self._printOverrideError('disposeAll')

    def as_setDataFromXmlS(self, data):
        """
        :param data: Represented by TweenConstraintsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataFromXml(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\tweenmanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:46 Støední Evropa (letní èas)
