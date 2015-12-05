__author__ = 'Bernardo Augusto Godinho de Oliveira - @bernardogo'

from storage.io import general
from query.evaluator import evaluator
from catalog.core import catalogCore

def main():
    print ("dsad")

io = general()
#io.initPage(2)
io.write()

eval = evaluator()
eval.execute("select db_id from table; from tables2;")


ctlg = catalogCore()
ctlg.newCatalog("students")
ctlg.insertAttr("sid", "integer")
ctlg.insertAttr("name", "string")
ctlg.commitCatalog()

ctlg2 = catalogCore()
ctlg2.loadCatalog("students")
print(ctlg2.catalog)
ctlg2.printCtlg()