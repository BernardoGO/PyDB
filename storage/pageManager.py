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

        self.catalog[table] = [self.catalog[table][0],self.catalog[table][1]+1]
        pageid = table + str(self.catalog[table][__numberOfPages_IDX__])

        if(self.catalog[table][__numberOfPages_IDX__] == 0):
            self.catalog[table][__numberOfPages_IDX__] += 1
            pageid = table + str(self.catalog[table][__numberOfPages_IDX__])
            io_s.initPage(pageid)



        self.commit()
        strToSVX = ""
        for x in values:
            strToSVX += x + "$"
        strToSVX = strToSVX[0:len(strToSVX)-1]

        while(True):
            if(io_s.hasEmptySpace(pageid)):
                io_s.writeValue(self.catalog[table][1], strToSVX, pageid)
                break
            else:
                self.catalog[table][__numberOfPages_IDX__] += 1
                self.commit()
                pageid = table + str(self.catalog[table][__numberOfPages_IDX__])
                io_s.initPage(pageid)
                print("Another page created")



    def readValues(self, table, cond = None):
        print("match")
        io_s = general()
        if(table not in self.catalog):
            print("Table does not exists -- attention")
        print (self.catalog[table][__numberOfPages_IDX__])
        values = []
        for x in range(1, self.catalog[table][__numberOfPages_IDX__]+1):
            readvals = io_s.readValues(table + str(x))
            for y in readvals:
                row = y.split(chr(0))[0].split("$")
                if len(row) == 1:
                    if len(row[0]) == 0:
                        continue
                if len(row) > 0:
                    if cond is None:
                        values.append(row)
                    else:
                        if len(cond) != len(row):
                            print("Length of values does not match table")
                        else:
                            valid = True
                            for x in range(len(cond)):
                                if cond[x] is None:
                                    continue
                                else:
                                    if cond[x] != row[x]:
                                        valid = False
                                        break

                            if valid:
                               values.append(row)

        print (values)


    def commit(self):
        pickle.dump(self.catalog,  open(__CATALOG_PREFIX__  + ".dat", 'wb'))

    def load(self):
        try:
            self.catalog = pickle.load(open(__CATALOG_PREFIX__ + ".dat", 'rb'))
        except:
            pass