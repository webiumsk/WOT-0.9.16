# 2016.10.11 22:17:03 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/FX/ClientCompatibility.py
import BigWorld
if BigWorld.component == 'editor':

    def addMat(a, b):
        return 0


    def delMat(a):
        return 0


    BigWorld.addMat = addMat
    BigWorld.delMat = delMat

    def player():
        return None


    BigWorld.player = player
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\fx\clientcompatibility.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:17:03 St�edn� Evropa (letn� �as)
