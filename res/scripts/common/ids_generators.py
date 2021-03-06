# 2016.10.11 22:16:11 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/ids_generators.py
import time

class Int32IDGenerator(object):

    def __init__(self):
        self.__nextID = 0
        self.__currID = 0

    def next(self):
        self.__nextID += 1
        if self.__nextID > 65535:
            self.__nextID = 0
        currTime = int(time.time())
        self.__currID = ((currTime & 32767) << 16) + self.__nextID
        return self.__currID

    currSequenceID = property(lambda self: self.__currID)


class SequenceIDGenerator(object):

    def __init__(self, lowBound = 0, highBound = 32767):
        self.__lowBound = lowBound
        self.__highBound = highBound
        self.__sequenceID = lowBound

    def next(self):
        self.__sequenceID += 1
        if self.__sequenceID >= self.__highBound:
            self.__sequenceID = self.__lowBound
        return self.__sequenceID

    currSequenceID = property(lambda self: self.__sequenceID)
    nextSequenceID = property(lambda self: self.next())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\ids_generators.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:16:11 St�edn� Evropa (letn� �as)
