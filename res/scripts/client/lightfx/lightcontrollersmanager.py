# 2016.10.11 22:14:38 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/LightFx/LightControllersManager.py
from Controllers.HealthController import HealthController
import LightManager

class LightControllersManager:

    def __init__(self, vehicle):
        self.__healthController = HealthController(vehicle.health, vehicle.typeDescriptor.maxHealth)

    def destroy(self):
        LightManager.g_instance.setStartupLights()

    def executeShotLight(self):
        LightManager.g_instance.startLightEffect('Shot')

    def executeHitLight(self):
        LightManager.g_instance.startLightEffect('Hit')

    def update(self, vehicle):
        self.__healthController.updateHealth(vehicle.health)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\lightfx\lightcontrollersmanager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:14:38 St�edn� Evropa (letn� �as)
