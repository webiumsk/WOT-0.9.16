# 2016.10.11 22:12:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/GuiItemsManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class GuiItemsManagerMeta(BaseDAAPIModule):

    def _getItemAttribute(self, itemTypeIdx, id, attrName):
        self._printOverrideError('_getItemAttribute')

    def _callItemMethod(self, itemTypeIdx, id, methodName, kargs):
        self._printOverrideError('_callItemMethod')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\guiitemsmanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:45 St�edn� Evropa (letn� �as)
