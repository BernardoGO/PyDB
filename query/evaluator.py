__author__ = 'Bernardo'

##### THIS IS A PLACEHOLDER EVALUATOR #####

from query.commands.insert import *
from query.commands.select import *
from query.commands.update import *

"""
CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);
"""

"""
sel.selection("students2", [['phone', 'terce32441iro']])
"""
from catalog.core import catalogCore
import re
class evaluator:
    def execQuery(self, query):
        from query.parser.sqlparse import parser
        pt = parser()
        gentokens = pt.parse(query)
        print("tokens = ",        gentokens)
        print("tokens.command =", gentokens.command)
        print("tokens.columns =", gentokens.columns)
        print("tokens.tables =",  gentokens.tables)
        print("tokens.join =",  gentokens.join)
        print("tokens.where =", gentokens.where)
        print("tokens.values =", gentokens.insValues)

        if gentokens.command == "select":

            sel = select()

            print ( "select detected")
            conditions = []
            if gentokens.where[0] == "where":
                print("where detected")

            for cond in gentokens.where:
                print ( cond)
                if isinstance(cond, list):
                    print( "list detected in where")

            sel.selection(gentokens.tables[0], [['phone', 'terce32441iro']])
            #sel.selection("students2", [['phone', 'terce32441iro']])


    def execute(self, query):
        if ("create table") in query:
            createTbl = r"(?:\s*)create table(?:\s*)(.*?)(?:\s*)\((?:\s*)(.*?)\);"
            groups =  re.findall(createTbl, query, re.S)
            print ("----->" + str(groups))
            attribsre = r"((?:.*?) (?:.*?),(?:\s*))"
            attribs = re.findall(attribsre, groups[0][1], re.S)
            print ("----->" + str(attribs))
            ctrl = catalogCore()
            ctrl.newCatalog(groups[0][0])
            for x in attribs:
                attr = x.split(" ")
                ctrl.insertAttr(attr[0], attr[1].replace(",", "").replace("\n", ""))

            ctrl.commitCatalog()


        #select = r"select (.*?) from (.*?);"
        #groups =  re.findall(select, query, re.S)
