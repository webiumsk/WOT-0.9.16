# 2016.10.11 22:12:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/LoaderManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class LoaderManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def viewLoaded(self, name, view):
        """
        :param view: Represented by IView (AS)
        """
        self._printOverrideError('viewLoaded')

    def viewLoadError(self, alias, name, text):
        self._printOverrideError('viewLoadError')

    def viewInitializationError(self, alias, name):
        self._printOverrideError('viewInitializationError')

    def as_loadViewS(self, data):
        """
        :param data: Represented by LoadViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\loadermanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:45 Støední Evropa (letní èas)
