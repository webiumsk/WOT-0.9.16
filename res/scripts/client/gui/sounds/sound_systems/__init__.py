# 2016.10.11 22:14:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/sounds/sound_systems/__init__.py
import WWISE
from gui.sounds.sound_systems import wwise_system, no_system
__all__ = ('getCurrentSoundSystem',)

def getCurrentSoundSystem():
    if WWISE.enabled:
        return wwise_system.WWISESoundSystem()
    return no_system.NoSoundSystem()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\sounds\sound_systems\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:14:23 St�edn� Evropa (letn� �as)
