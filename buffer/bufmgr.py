__author__ = 'Bernardo'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
from storage.pageManager import pageManager
import calendar
import time

__MAX_SIZE__ = 2

class buffer:
    def __init__(self):
        self.pid = None
        self.page = None
        self.timestamp = None


class buffer_pool:
    def __init__(self):
        self.pool = []
        for x in range(0, __MAX_SIZE__):
            self.addToPool(None)


    def addToPool(self, pid):
        pgmg = pageManager()
        ios = general()
        newb = buffer()
        newb.pid = pid
        newb.timestamp = calendar.timegm(time.gmtime())
        if pid is not None:
            newb.page = ios.readPage(pid)
        self.pool.append(newb)

