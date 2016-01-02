__author__ = 'Bernardo'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
import calendar
import time

__MAX_SIZE__ = 2

class buffer:
    def __init__(self):
        self.pid = None
        self.page = None
        self.timestamp = None
        self.pinCount = 0
        self.dirty = False


class buffer_pool:
    pool = []
    def __init__(self):

        for x in range(0, __MAX_SIZE__):
            self.addToPool(None)

    def findPage(self, pid):
        pos = -1
        for x in range(len(buffer_pool.pool)):
            if buffer_pool.pool[x].pid == pid:
                pos = x
                break
        return pos

    def addToPool(self, pid):
        ios = general()
        newb = buffer()
        newb.pid = pid
        newb.timestamp = calendar.timegm(time.gmtime())
        if pid is not None:
            newb.page = ios.readPage(pid)
        buffer_pool.pool.append(newb)

    def findVictimPage(self):
        victim = 0
        for x in range(len(buffer_pool.pool)):
            if buffer_pool.pool[x].timestamp < victim.timestamp and buffer_pool.pool[x].pincount == 0:
                victim = x
        return victim

    def replacePage(self, pid):
        ios = general()
        newb = buffer()
        newb.pid = pid
        newb.timestamp = calendar.timegm(time.gmtime())
        newb.page = ios.readPage(pid)
        victim = self.findVictimPage()
        buffer_pool.pool[victim] = newb


