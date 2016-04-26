__author__ = 'Bernardo Augusto Godinho de Oliveira - @bernardogo'

from query.evaluator import evaluator
from storage.io import general
from catalog.core import catalogCore
from storage.tablemgr import manager
from buffer.bufmgr import buffer_pool
from query.commands.insert import *
from query.commands.select import *
from query.commands.update import *

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
    #tblm.createTable("students3", [["id", "integer"], ["phone", "string"]])


    ctlg2 = catalogCore()
    ctlg2.loadCatalog("students2")
    ctlg2.printCtlg()


    ins = insert()

    ins.insertRecord("students2", ["26", "terce32441iro"])
    #for x in range(25, 82):
    #    ins.insertRecord("students3", [str(x), "terce3PG32323o" + str(x)])

    sel = select()
    upd = update()
    #sel.selection("students2", [])
    upd.update("students2", [['phone', 'terceiro2221see']], [['phone', 'terceiro2221seesss']])
    sel.selection("students2", [['phone', 'terce32441iro']])
    print("321-----")
    #sel.selection("students2", [])
    #sel.selection("students3", [])
    #sel.join("students2", "students3", sel.selection("students2", []), sel.selection("students3", []), "id")
    main_pool.forceBuffer()
    print(main_pool.pool)

    from query.parser.sqlparse import parser
    pt = parser()
    #pt.parse("select * from x where x = 3 and y < 2")
    eval.exec("select * from students2 where phone = terce32441iro")

main()
