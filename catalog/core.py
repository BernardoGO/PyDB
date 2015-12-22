__author__ = 'Bernardo'

__CATALOG_PREFIX__ = "ctl"

import pickle

class catalogCore:
    def __init__(self):
        self.catalog = []
        self.tableName = "tst"

    def insertAttr(self, attr, type):
        self.catalog.append([attr, type])

    def newCatalog(self, t_name):
        self.tableName = t_name
        self.catalog = []

    def commitCatalog(self):
        pickle.dump(self.catalog,  open(__CATALOG_PREFIX__ + self.tableName + ".dat", 'wb'))

    def loadCatalog(self, table):
        self.tableName = table
        self.catalog = pickle.load(open(__CATALOG_PREFIX__ + self.tableName + ".dat", 'rb'))

    def printCtlg(self):
        print(self.catalog)
