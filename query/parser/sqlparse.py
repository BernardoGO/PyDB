from pyparsing import Literal, CaselessLiteral, Upcase, Word, delimitedList, Optional, \
    Combine, Group, alphas, nums, alphanums, ParseException, Forward, oneOf, quotedString, \
    ZeroOrMore, restOfLine, Keyword

from query.parser import tokens


class parser:

    realNum = Combine( Optional(tokens.arithSign) + ( Word( nums ) + "." + Optional( Word(nums) )  |
                                                             ( "." + Word(nums) ) ) +
                Optional( E + Optional(tokens.arithSign) + Word(nums) ) )
    intNum = Combine( Optional(tokens.arithSign) + Word( nums ) +
                Optional( E + Optional("+") + Word(nums) ) )

    columnRval = realNum | intNum | quotedString | tokens.columnName # need to add support for alg expressions
    whereCondition = Group(
        ( tokens.columnName + tokens.binop + columnRval ) |
        ( tokens.columnName + tokens.in_ + "(" + delimitedList( columnRval ) + ")" ) |
        ( tokens.columnName + tokens.in_ + "(" + tokens.selectStmt + ")" ) |
        ( "(" + tokens.whereExpression + ")" )
        )
    tokens.whereExpression << (whereCondition + ZeroOrMore( ( and_ | or_ ) + whereExpression ) )


    joinCondition = Group(
        ( tokens.tableName + tokens.on_ + tokens.whereExpression )
        )
    tokens.joinExpression << (joinCondition  )

    # define the grammar
    tokens.selectStmt      << ( tokens.selectToken +
                       ( '*' | tokens.columnNameList ).setResultsName( "columns" ) +

                       tokens.fromToken +
                       tokens.tableNameList.setResultsName( "tables" ) +
            Optional( Group( CaselessLiteral("join") + tokens.joinExpression ), "" ).setResultsName("join") +
                       Optional( Group( CaselessLiteral("where") + tokens.whereExpression ), "" ).setResultsName("where") )

    simpleSQL = tokens.selectStmt

    # define Oracle comment format, and ignore them
    oracleSqlComment = "--" + restOfLine
    simpleSQL.ignore( oracleSqlComment )