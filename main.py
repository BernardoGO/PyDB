__author__ = 'Bernardo Augusto Godinho de Oliveira - @bernardogo'

from storage.io import general
from query.evaluator import evaluator
from catalog.core import catalogCore
from storage.tablemgr import manager
from buffer.bufmgr import buffer_pool

main_pool = buffer_pool()

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
from query.commands.update import *
ins = insert()

#ins.insertRecord("students2", ["26", "terce32441iro"])

#for x in range(25, 82):
#    ins.insertRecord("students2", [str(x), "terce32441iro" + str(x)])

sel = select()
upd = update()
#sel.selection("students2", [])
upd.update("students2", [['phone', 'terce32441iro']], [['phone', 'terceiro2221see']])
#sel.selection("students2", [['phone', 'terce32441iro']])
print("321-----")
sel.selection("students2", [])
main_pool.forceBuffer()
print(main_pool.pool)