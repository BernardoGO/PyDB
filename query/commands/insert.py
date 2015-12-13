__author__ = 'Bernardo'

from catalog.core import catalogCore
from storage.io import io
from storage.tablemgr import manager

class insert:
    def __init__(self):
        pass

    def insertRecord(self, table, values):
        ctlg = catalogCore()
        ctlg.loadCatalog(table)
        print("Values not verified.")
        if len(ctlg.catalog) == len(values):

