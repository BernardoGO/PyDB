__author__ = 'Bernardogo'

from catalog.core import catalogCore
from storage.io import general
from storage.tablemgr import manager
from storage.pageManager import pageManager
from query.commands.select import select

class delete:
    def __init__(self):
        pass


    def delete(self, table, values, newvalues):
        sel = select()
        pgmg = pageManager()
        sel.selection(table, values, pgmg.deleteValues, newvalues)



