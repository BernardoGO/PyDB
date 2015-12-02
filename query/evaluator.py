__author__ = 'Bernardo'


import re
class evaluator:
    def execute(self, query):
        select = r"select (.*?) from (.*?);"
        groups =  re.findall(select, query)
        print (groups)