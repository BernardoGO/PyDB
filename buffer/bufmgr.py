__author__ = 'Bernardo'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
import calendar
import time

__MAX_SIZE__ = 3

class buffer:
    def __init__(self):
        self.pid = None
        self.page = None
        self.rids = None
        self.timestamp = None
        self.pinCount = 0
        self.dirty = False

    def forcePage(self):
        pass




class buffer_pool:
    pool = []
    def __init__(self):
        if len(buffer_pool.pool) == 0:
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
            if buffer_pool.pool[x].timestamp < buffer_pool.pool[victim].timestamp:
                victim = x
        return victim

    def replacePage(self, pid):
        ios = general()
        newb = buffer()
        newb.pid = pid

        page = ios.readValues(pid)
        print(page[0])
        newb.page = page[0]#.split(chr(0))[0].split("$")
        newb.rids = page[1]
        victim = self.findVictimPage()
        #time.sleep(1)
        newb.timestamp = time.time()

        print("Replacing Page: " + str(buffer_pool.pool[victim].pid) + " -> " + str(newb.pid) + " on slot " + str(victim))
        buffer_pool.pool[victim] = newb


