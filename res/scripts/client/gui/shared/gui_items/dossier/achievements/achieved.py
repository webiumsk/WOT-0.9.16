# 2016.10.11 22:13:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/Achieved.py
from abstract import RegularAchievement
from gui.shared.gui_items.dossier.achievements import validators

class Achieved(RegularAchievement):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.alreadyAchieved(cls, name, block, dossier)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\achieved.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:13:49 St�edn� Evropa (letn� �as)
