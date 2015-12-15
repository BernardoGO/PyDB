__author__ = 'Bernardo'

import pickle
from storage.io import general
__CATALOG_PREFIX__ = "pagemgr"

__numberOfPages_IDX__ = 0

class pageManager:
    def __init__(self):
        self.catalog = {}
        if(len(self.catalog) == 0):
            self.load()

    def updateInfo(self, table, value):


        #numberOfPages|AutoIncrNumber
        self.catalog[table] = value
        self.commit()

    def writeValue(self, table, values):
        io_s = general()
        if(table not in self.catalog):
            print("not in")
            self.catalog[table] = [0,0]
        if(self.catalog[table][__numberOfPages_IDX__] == 0):
            self.catalog[table][__numberOfPages_IDX__] += 1
            io_s.initPage(table + str(self.catalog[table][__numberOfPages_IDX__]))

            self.commit()
        strToSVX = ""
        for x in values:
            strToSVX += x + "$"
        io_s.writeValue(0, strToSVX, table + str(self.catalog[table][__numberOfPages_IDX__]))




    def commit(self):
        pickle.dump(self.catalog,  open(__CATALOG_PREFIX__  + ".dat", 'wb'))

    def load(self):
        try:
            self.catalog = pickle.load(open(__CATALOG_PREFIX__ + ".dat", 'rb'))
        except:
            pass