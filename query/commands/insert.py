__author__ = 'BernardoGO'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
from storage.pageManager import pageManager

class insert:
    def __init__(self):
        pass

    def insertRecord(self, table, values):
        ctlg = catalogCore()
        ctlg.loadCatalog(table)
        io_s = general()
        print("Values not verified.")
        if len(ctlg.catalog) == len(values):
            pgmg = pageManager()
            pgmg.writeValue(table, values)
        else:
            print("Number of values does not match table columns")

