from pyparsing import Literal, CaselessLiteral, Word, delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
    ZeroOrMore, restOfLine, Keyword

from query.parser import tokens


class parser:
    def __init__(self):
        self.realNum = Combine( Optional(tokens.arithSign) + ( Word( nums ) + "." + Optional( Word(nums) )  |
                                                                 ( "." + Word(nums) ) ) +
                    Optional( tokens.E + Optional(tokens.arithSign) + Word(nums) ) )
        self.intNum = Combine( Optional(tokens.arithSign) + Word( nums ) +
                    Optional( tokens.E + Optional("+") + Word(nums) ) )

        self.columnRval = self.realNum | self.intNum | quotedString | tokens.columnName # need to add support for alg expressions
        self.whereCondition = Group(
            ( tokens.columnName + tokens.binop + self.columnRval ) |
            ( tokens.columnName + tokens.in_ + tokens.LPAREN + delimitedList( self.columnRval ) + tokens.RPAREN ) |
            ( tokens.columnName + tokens.in_ + tokens.LPAREN + tokens.selectStmt + tokens.RPAREN ) |
            ( tokens.LPAREN + tokens.whereExpression + tokens.RPAREN )
            )
        tokens.whereExpression << (self.whereCondition + ZeroOrMore(   tokens.and_ | tokens.or_ ) + tokens.whereExpression )


        self.joinCondition = Group(
            ( tokens.tableName + tokens.on_ + tokens.whereExpression )
            )
        tokens.joinExpression << (self.joinCondition  )


        # define the grammar
        tokens.selectStmt      << ( tokens.selectToken.setResultsName("command") +
                           ( '*' | tokens.columnNameList ).setResultsName( "columns" ) +

                           tokens.fromToken +
                           tokens.tableNameList.setResultsName( "tables" ) +
                Optional( Group( CaselessLiteral("join") + tokens.joinExpression ), "" ).setResultsName("join") +
                           Optional( Group( CaselessLiteral("where") + tokens.whereExpression ), "" ).setResultsName("where") )

        #self.valuesIter = ( self.columnRval | "," + self.columnRval)

        tokens.insertStmt << (tokens.insertToken.setResultsName("command") +
                                tokens.intoToken.setResultsName("middle") +
                                tokens.columnNameList.setResultsName( "tables" ) +
                                tokens.valuesToken.setResultsName("val") +
                                tokens.LPAREN + Group(delimitedList(self.columnRval, delim=r', ')).setResultsName("insValues") + tokens.RPAREN



                                )

        self.simpleSQL =  tokens.selectStmt | tokens.insertStmt

        # define Oracle comment format, and ignore them
        self.oracleSqlComment = "--" + restOfLine
        self.simpleSQL.ignore( self.oracleSqlComment )

    def parse(self, str):
        gentokens = None
        try:
            gentokens = self.simpleSQL.parseString( str )
        except ParseException as err:
            print(" "*err.loc + "^\n" + err.msg)
            print(err)
        return gentokens

    def test(self, str ):
        print(str,"->")
        try:
            gentokens = self.simpleSQL.parseString( str )
            print("tokens = ",        gentokens)
            print("tokens.command =", gentokens.command)
            print("tokens.columns =", gentokens.columns)
            print("tokens.tables =",  gentokens.tables)
            print("tokens.join =",  gentokens.join)
            print("tokens.where =", gentokens.where)
        except ParseException as err:
            print(" "*err.loc + "^\n" + err.msg)
            print(err)
        print()
