# 2016.10.11 22:12:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsContentTabsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsContentTabsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onSelectTab(self, id):
        self._printOverrideError('onSelectTab')

    def as_selectTabS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_selectTab(index)

    def as_setTabsS(self, data):
        """
        :param data: Represented by TabsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabs(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\questscontenttabsmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:33 Støední Evropa (letní èas)
