__author__ = 'Bernardo'

import pickle
from storage.io import general
from buffer.bufmgr import buffer_pool
import storage.io

__CATALOG_FOLDER__ = "data/"
__CATALOG_PREFIX__ = __CATALOG_FOLDER__+ "pagemgr"

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

    def buildRow(self, row):
        newPg = ""
        for i in range(len(row)):   ########################### THIS IS NOT THE BEST WAY TO DO THIS, CHANGE THE BUFFER FILE
            newPg += row[i] + "$"
        return newPg[0:len(newPg)-1]


    def writeValue(self, table, values):
        io_s = general()
        bfm = buffer_pool()
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
            strToSVX += x.replace('""', '') + "$"
        strToSVX = strToSVX[0:len(strToSVX)-1]

        while(True):
            if(io_s.hasEmptySpace(pageid)):

                #io_s.writeValue(self.catalog[table][1], strToSVX, pageid)
                #victim = bfm.replacePage(pageid)

                readvals = bfm.findPage(pageid)
                if readvals == -1:
                    readvals = bfm.replacePage(pageid)

                for rec in range(len(bfm.pool[readvals].rids)):
                    if bfm.pool[readvals].rids[rec] == storage.io.__CONS_EMPTY_SLOT__:
                        bfm.pool[readvals].rids[rec] = self.catalog[table][1]
                        bfm.pool[readvals].page[rec] =strToSVX
                        bfm.pool[readvals].dirty = True
                        break

                print("Values written")
                break
            else:
                self.catalog[table][__numberOfPages_IDX__] += 1
                self.commit()
                pageid = table + str(self.catalog[table][__numberOfPages_IDX__])
                io_s.initPage(pageid)
                print("Another page created")


    def updateValues(self, row, xx, yy, newValues):
        bfm = buffer_pool()
        for xxs in range(len(newValues)):
            if newValues[xxs] is None:
                continue
            else:
                row[xxs] = newValues[xxs]
                bfm.pool[xx].page[yy] = self.buildRow(row)
                bfm.pool[xx].dirty = True

    def deleteValues(self, row, xx, yy, newValues):
        bfm = buffer_pool()
        for xxs in range(len(newValues)):
            if newValues[xxs] is None:
                continue
            else:
                bfm.pool[xx].page[yy] = self.buildRow(row)
                bfm.pool[xx].dirty = True
                bfm.pool[xx].rids[yy] = storage.io.__CONS_EMPTY_SLOT__

    def replaceControl(self, page):
        bfm = buffer_pool()
        readvals = bfm.findPage(page)
        if readvals == -1:
            bfm.replacePage(page)
        return bfm.findPage(page)

    def readValues(self, table, cond = None, function = None, newValues = None):
        bfm = buffer_pool()
        print("match")
        io_s = general()
        if(len(self.catalog) == 0):
            print("WARNING: IT SHOULD BE LOADED HERE")
            self.load()

        if(table not in self.catalog):
            print("Table does not exists -- attention")


        print(self.catalog)
        print (self.catalog[table][__numberOfPages_IDX__])
        values = []
        for x in range(1, self.catalog[table][__numberOfPages_IDX__]+1):
            #readvals = io_s.readValues(table + str(x))
            page = table + str(x)
            victimPage = self.replaceControl(page)

            for victimRecord in range(len(bfm.pool[victimPage].page)):
                y = bfm.pool[victimPage].page[victimRecord]

                row = y.split(chr(0))[0].split("$")

                if len(row) == 1 and len(row[0]) == 0: continue#empty row
                elif len(row) > 0:

                    if cond is None: #not a filtered selection
                        values.append([bfm.pool[victimPage].rids[victimRecord], row])
                    else:
                        if len(cond) != len(row):
                            print("Length of values does not match table")
                        else:
                            valid = True
                            for x in range(len(cond)):
                                if cond[x] is None:
                                    continue
                                else:
                                    if str(cond[x]) != str(row[x]):
                                        #print ( str(cond[x]) +"-VER-"+ str(row[x]))
                                        valid = False
                                        break

                            if valid and bfm.pool[victimPage].rids[victimRecord] != storage.io.__CONS_EMPTY_SLOT__:
                                if newValues is not None:
                                    function(row, victimPage, victimRecord, newValues)
                                values.append([bfm.pool[victimPage].rids[victimRecord], row])
        print (values)
        return values


    def commit(self):
        pickle.dump(self.catalog,  open(__CATALOG_PREFIX__  + ".dat", 'wb'), protocol=2)

    def load(self):
        try:
            self.catalog = pickle.load(open(__CATALOG_PREFIX__ + ".dat", 'rb'))
        except Exception as e:
            print("FAILED TO LOAD CATALOG" + str(e))
            pass
