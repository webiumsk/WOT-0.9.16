# 2016.10.11 22:21:29 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/multiprocessing/dummy/connection.py
__all__ = ['Client', 'Listener', 'Pipe']
from Queue import Queue
families = [None]

class Listener(object):

    def __init__(self, address = None, family = None, backlog = 1):
        self._backlog_queue = Queue(backlog)

    def accept(self):
        return Connection(*self._backlog_queue.get())

    def close(self):
        self._backlog_queue = None
        return

    address = property(lambda self: self._backlog_queue)


def Client(address):
    _in, _out = Queue(), Queue()
    address.put((_out, _in))
    return Connection(_in, _out)


def Pipe(duplex = True):
    a, b = Queue(), Queue()
    return (Connection(a, b), Connection(b, a))


class Connection(object):

    def __init__(self, _in, _out):
        self._out = _out
        self._in = _in
        self.send = self.send_bytes = _out.put
        self.recv = self.recv_bytes = _in.get

    def poll(self, timeout = 0.0):
        if self._in.qsize() > 0:
            return True
        if timeout <= 0.0:
            return False
        self._in.not_empty.acquire()
        self._in.not_empty.wait(timeout)
        self._in.not_empty.release()
        return self._in.qsize() > 0

    def close(self):
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\multiprocessing\dummy\connection.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.10.11 22:21:29 St�edn� Evropa (letn� �as)
