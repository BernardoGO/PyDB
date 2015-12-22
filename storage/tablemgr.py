__author__ = 'Bernardo'

import re

from catalog.core import catalogCore


class manager:
    def createTable(self, name, attrs):
        ctlg = catalogCore()
        ctlg.tableName = name
        for x in attrs:
            ctlg.insertAttr(x[0], x[1])
        ctlg.commitCatalog()

