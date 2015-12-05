__author__ = 'Bernardo'

import re


class manager:
    def createTable(self, name, attrs):
        select = r"select (.*?) from (.*?);"
        groups =  re.findall(select, query)
        print (groups)