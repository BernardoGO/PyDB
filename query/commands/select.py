__author__ = 'BernardoGO'

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

    def join(self, table1, table2, selection1, selection2, cond):
        ctlg1 = catalogCore()
        ctlg1.loadCatalog(table1)
        ctlg2 = catalogCore()
        ctlg2.loadCatalog(table2)
        pgmg = pageManager()
        io_s = general()
        cond1pos = -1
        cond2pos = -1

        for x in range(len(ctlg1.catalog)):
            if ctlg1.catalog[x][0] == cond:
                cond1pos = x

        for x in range(len(ctlg2.catalog)):
            if ctlg2.catalog[x][0] == cond:
                cond2pos = x

        joinedVals = []
        for x in selection1:
            for y in selection2:
                if x[1][cond1pos] == y[1][cond2pos]:
                    newv = []
                    newv.extend(x[1])
                    newv.extend(y[1])
                    joinedVals.append(newv)
                    print(newv)
        return joinedVals

    def selection(self, table, values, function = None, newValues = None):
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


        x = pgmg.readValues(table, vals, function, newVals)
        return x
        print(len(x))
        #print(len(pgmg.readValues(table, vals)))



