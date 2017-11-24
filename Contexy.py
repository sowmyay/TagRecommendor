import sys

import DataType
import Operators


def ParseCode(line,delimiters):
    word = ''
    operator = ''
    final_line = []
    final_word = []
    final_operator = []
    printBrackets = 0
    for i in range(0,len(line)):
        printword = True
        printoperator = True

        if ( line[i] == '[' ):
            printBrackets += 1

        if( printBrackets > 0 ):
            word += line[i]
            if( line[i] != ']' ):
                continue

        if ( line[i] == ']' ):
            printBrackets -= 1
            continue

        if(line[i] not in delimiters):
            if(line[i].isalnum() or line[i] == '_'):
                word += line[i]
                printword = False
                if(operator == ''):
                    continue
            else:
                operator += line[i]
                printoperator = False
                if(word == ''):
                    continue
        if(word != '' and printword):
            final_line.append(word)
            final_word.append(word)
            # print word
            word = ''
        if(operator != '' and printoperator):
            final_line.append(operator)
            final_operator.append(operator)
            # print operator
            operator = ''
    return final_line,final_word,final_operator


num_args = len(sys.argv)
if num_args < 3:
    print "error: not enough input arguments"
    exit(1)

input_file = sys.argv[1]
cursor = int(sys.argv[2])
delimiters = ['\n', ' ', '.', ')', '(', ';','{','}']
cursor_words = []
cursor_operators = []
cursor_line = []
# line = "int rev[10] "
# cursor_line, cursor_words, cursor_operators = ParseCode(line,delimiters)
# print cursor_words
# print cursor_operators
# print cursor_line

with open(input_file, 'r') as interest_data:
    for i in range(1,cursor):
        interest_data.readline()
    line = interest_data.readline()
    cursor_line, cursor_words, cursor_operators = ParseCode(line,delimiters)

print cursor_words

keylines = dict()

data = []
with open(input_file, 'r') as interest_data:
    found = False
    for line in interest_data:
        line, words, operators = ParseCode(line,delimiters)
        for w in cursor_words:
            if(w in words):
                keylines[w] = line
                cursor_words = filter(lambda a: a != w, cursor_words)
                # print "cursor_words", cursor_words
                data += [line]
        if (not cursor_words ):
            break
# print data
print keylines
DataType.getDataType(keylines, "c++")
print Operators.getOperatorTags(cursor_words)

