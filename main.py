__author__ = 'Bernardo Augusto Godinho de Oliveira - @bernardogo'

from storage.io import general
from query.evaluator import evaluator
from catalog.core import catalogCore
from storage.tablemgr import manager

def main():
    print ("dsad")

io = general()
#io.initPage(2)
io.write()

eval = evaluator()
eval.execute(
    """
    create table table_name
    (
    column_name1 data_type(size),
    column_name2 data_type(size),
    column_name3 data_type(size),
    );
    """


)

tblm = manager()
tblm.createTable("students2", [["id", "integer"], ["phone", "string"]])


ctlg2 = catalogCore()
ctlg2.loadCatalog("students2")
ctlg2.printCtlg()

from query.commands.insert import *
from query.commands.select import *

ins = insert()
#ins.insertRecord("students2", ["24", "terce321iro"])

sel = select()
sel.selection("students2", [])