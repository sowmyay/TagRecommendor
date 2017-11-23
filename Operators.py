class Operators:

    def tag(self, operators, lang):
        for item in operators:
            if item == "+":
                return ["add"]
            elif item == "-":
                return ["subtract"]
            elif item == "*":
                return ["multiplying"]
            elif item == "/":
                return ["divide"]
            elif item == "%":
                return ["modulo"]
            elif item == "=":
                return ["assignment"]
            elif item == "+=" or item == "-=" or item == "*=" or item == "/=" or \
                            item == "%=" or item == "&=" or item == "^=" or item == "~=" or item == "<<=" or item == ">>=":
                return ["compound-assignment", "compound-operator"]
            elif item == "=":
                return ["assignment"]
            elif item == "++":
                return ["increment"]
            elif item == "--":
                return ["decrement"]
            elif item == "==":
                return ["equals", "comparision"]
            elif item == "!=" or "<" or ">" or "<=" or ">=":
                return ["comparision", "relational"]
            elif item == "<":
                return ["comparision"]
            elif item == "||" or "!" or "&&":
                return ["logical-operators"]
            elif item == "&" or item == "|" or item == "~" or item == "^":
                return ["bit-manipulation", "bitwise-operators"]
            elif item == "<<" or item == ">>":
                return ["bit-shift", "bit-shift-operators"]
            elif item == "?":
                return ["conditional"]
            else:
                return ["operator"]

    # def getLine(self, line, dataType, lang):
    #     operators = set()
    #     if lang == "c++":
    #         if dataType == "vector":
    #             operators.add()
    #             # print "vector"
    #         elif "list" in line:
    #             d.add("list")
    #             # print "list"
    #         elif "map" in line:
    #             d.add("map")
    #             # print "map"
    #         elif "set" in line:
    #             d.add("set")
    #             # print "set"
    #         elif "stack" in line:
    #             d.add("stack")
    #             # print "stack"
    #         elif "queue" in line:
    #             d.add("queue")
    #             # print "queue"
    #         elif "priority_queue" in line:
    #             d.add("priority queue")
    #             # print "priority queue"
    #         elif "int" in line:
    #             d.add("int")
    #             # print "int"
    #         elif "char" in line:
    #             d.add("char")
    #             # print "char"
    #         elif "bool" in line:
    #             d.add("bool")
    #             # print "bool"
    #         elif "float" in line:
    #             d.add("float")
    #             # print "float"
    #         elif "double" in line:
    #             d.add("double")
    #             # print "double"
    #         elif "long" in line:
    #             d.add("long")
    #             # print "long"
    #         else:
    #             for str in line:
    #                 if "[" in str and "]" in str:
    #                     d.add("array")
    #
    #             for str in line:
    #                 if "->" in str:
    #                     d.add("pointer")
    #                     # print "pointer"




