__author__ = 'Bernardo Augusto Godinho de Oliveira - @bernardogo'

from storage.io import general
from query.evaluator import evaluator

def main():
    print ("dsad")

io = general()
#io.initPage(2)
io.write()

eval = evaluator()
eval.execute("select db_id from table;")
