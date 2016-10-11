# 2016.10.11 22:11:44 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/VehicleCompareCartButton.py
from gui.Scaleform.daapi.view.meta.ButtonWithCounterMeta import ButtonWithCounterMeta
from gui.game_control import getVehicleComparisonBasketCtrl

class VehicleCompareCartButton(ButtonWithCounterMeta):

    def __init__(self):
        super(VehicleCompareCartButton, self).__init__()

    def _populate(self):
        super(VehicleCompareCartButton, self)._populate()
        comparisonBasketCtrl = getVehicleComparisonBasketCtrl()
        comparisonBasketCtrl.onChange += self.__onCountChanged
        comparisonBasketCtrl.onSwitchChange += self.destroy
        self.__changeCount(comparisonBasketCtrl.getVehiclesCount())

    def _dispose(self):
        comparisonBasketCtrl = getVehicleComparisonBasketCtrl()
        comparisonBasketCtrl.onChange -= self.__onCountChanged
        comparisonBasketCtrl.onSwitchChange -= self.destroy
        super(VehicleCompareCartButton, self)._dispose()

    def __onCountChanged(self, changedData):
        """
        gui.game_control.VehComparisonBasket.onChange event handler
        :param changedData: instance of gui.game_control.veh_comparison_basket._ChangedData
        """
        self.__changeCount(getVehicleComparisonBasketCtrl().getVehiclesCount())

    def __changeCount(self, count):
        self.as_setCountS(count)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\messengerbar\vehiclecomparecartbutton.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:11:44 Støední Evropa (letní èas)
