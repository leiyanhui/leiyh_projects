# -*- coding: utf-8 -*-

from atexit import register
from random import randrange
from threading import Lock, currentThread, Thread
from time import ctime, sleep

from cffi.backend_ctypes import xrange


class CleanOutpurSet(set):
    def __str__(self):
        return ','.join(x for x in self)


lock = Lock()

loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))

remainig = CleanOutpurSet()


def loop(nesc):
    myname = currentThread().name
    lock.acquire()
    remainig.add(myname)
    print('[%s] Started %s' % (ctime(), myname))

    lock.release()
    sleep(nesc)
    lock.acquire()
    remainig.remove(myname)

    print('[%s] Completed: %s(%d: secs)' % (ctime(), myname, nesc))

    print('(remining : %s)' % (remainig or 'None'))

    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    _main()
