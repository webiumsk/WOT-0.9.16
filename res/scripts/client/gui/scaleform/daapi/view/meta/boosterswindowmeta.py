# 2016.10.11 22:12:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BoostersWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BoostersWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def requestBoostersArray(self, tabIndex):
        self._printOverrideError('requestBoostersArray')

    def onBoosterActionBtnClick(self, boosterID, questID):
        self._printOverrideError('onBoosterActionBtnClick')

    def onFiltersChange(self, filters):
        self._printOverrideError('onFiltersChange')

    def onResetFilters(self):
        self._printOverrideError('onResetFilters')

    def as_setDataS(self, data):
        """
        :param data: Represented by BoostersWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by BoostersWindowStaticVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setListDataS(self, boosters, scrollToTop):
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(boosters, scrollToTop)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\boosterswindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:12:18 St�edn� Evropa (letn� �as)
