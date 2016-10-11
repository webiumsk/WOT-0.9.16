# 2016.10.11 22:08:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/SoundZoneTrigger.py
import BigWorld
import Math

class SoundZoneTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        import bwpydevd
        bwpydevd.startDebug()
        width = self.Size[0]
        height = self.Size[0]
        position = Math.Vector2(self.position.x, self.position.z) - self.Size
        alpha = self.direction.z

    def destroy(self):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\soundzonetrigger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:08:47 Støední Evropa (letní èas)
