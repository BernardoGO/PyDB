__author__ = 'Bernardo'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
from storage.pageManager import pageManager

class select:
    def __init__(self):
        pass

    def selection(self, table, values):
        ctlg = catalogCore()
        ctlg.loadCatalog(table)
        pgmg = pageManager()
        io_s = general()
        print("Values not verified.")

        pgmg.readValues(table)


