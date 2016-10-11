# 2016.10.11 22:10:52 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/deserter_dialog.py
from gui.Scaleform.daapi.view.meta.DeserterDialogMeta import DeserterDialogMeta

class IngameDeserterDialog(DeserterDialogMeta):

    def __init__(self, meta, handler):
        super(IngameDeserterDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self.__imagePath = meta.getImagePath()
        self.__offsetY = meta.getOffsetY()

    def _populate(self):
        super(IngameDeserterDialog, self)._populate()
        self.as_setDataS(self.__imagePath, self.__offsetY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\dialogs\deserter_dialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:10:52 Støední Evropa (letní èas)
