# 2016.10.11 22:12:20 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileFortificationInfoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileFortificationInfoViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_setFortDataS(self, data):
        """
        :param data: Represented by ClanProfileFortificationViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFortData(data)

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanProfileFortificationViewInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\clanprofilefortificationinfoviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:20 Støední Evropa (letní èas)
