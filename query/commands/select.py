__author__ = 'Bernardo'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
from storage.pageManager import pageManager

class select:
    def __init__(self):
        pass

    def buildValues(self, ctlg):
        builtVal = []
        for x in ctlg.catalog:
            builtVal.append(None)
        return builtVal

    def selection(self, table, values, newValues = None):
        ctlg = catalogCore()
        ctlg.loadCatalog(table)

        pgmg = pageManager()
        io_s = general()
        print("Values not verified.")

        vals = self.buildValues(ctlg)
        newVals = None
        if newValues is not None:
            newVals = self.buildValues(ctlg)
            for x in range(len(newValues)):
                for y in range(len(ctlg.catalog)):
                    val1 = newValues[x][0]
                    val2 = ctlg.catalog[y][0]
                    if val1 == val2:
                        newVals[y] = newValues[x][1]

        for x in range(len(values)):
            for y in range(len(ctlg.catalog)):
                val1 = values[x][0]
                val2 = ctlg.catalog[y][0]
                if val1 == val2:
                    vals[y] = values[x][1]


        x = pgmg.readValues(table, vals, newVals)
        print(len(x))
        #print(len(pgmg.readValues(table, vals)))



