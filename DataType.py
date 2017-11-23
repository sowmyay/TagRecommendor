def cppDataTypes(keylines):
    d = set()
    for line in keylines.values():
        if "struct" in line and "*" in line:
            d.add("Linked List")
            # print "Linked List"
        elif "vector" in line:
            d.add("vector")
            # print "vector"
        elif "list" in line:
            d.add("list")
            # print "list"
        elif "map" in line:
            d.add("map")
            # print "map"
        elif "set" in line:
            d.add("set")
            # print "set"
        elif "stack" in line:
            d.add("stack")
            # print "stack"
        elif "queue" in line:
            d.add("queue")
            # print "queue"
        elif "priority_queue" in line:
            d.add("priority queue")
            # print "priority queue"
        elif "int" in line:
            d.add("int")
            # print "int"
        elif "char" in line:
            d.add("char")
            # print "char"
        elif "bool" in line:
            d.add("bool")
            # print "bool"
        elif "float" in line:
            d.add("float")
            # print "float"
        elif "double" in line:
            d.add("double")
            # print "double"
        elif "long" in line:
            d.add("long")
            # print "long"
        else:
            for str in line:
                if "[" in str and "]" in str:
                    d.add("array")

            for str in line:
                if "->" in str:
                    d.add("pointer")
                    # print "pointer"
    return d

def javaDataTypes(keylines):
    d = set()
    for line in keylines.values():
        if "LinkedList" in line:
            d.add("Linked List")
            # print "Linked List"
        elif "Enumeration" in line:
            d.add("Enumeration")
            # print "vector"
        elif "BitSet" in line:
            d.add("BitSet")
            # print "vector"
        elif "Vector" in line:
            d.add("vector")
            # print "vector"
        elif "Stack" in line:
            d.add("Stack")
            # print "stack"
        elif "HashTable" in line:
            d.add("Hashtable")
            # print "stack"
        elif "Map" in line:
            d.add("Hashmap")
            # print "list"
        elif "Set" in line:
            d.add("set")
            # print "set"
        elif "Queue" in line:
            d.add("queue")
            # print "queue"
        elif "PriorityQueue" in line:
            d.add("priority queue")
            # print "priority queue"
        elif "byte" in line:
            d.add("byte")
            # print "bool"
        elif "int" in line:
            d.add("int")
            # print "int"
        elif "char" in line:
            d.add("char")
            # print "char"
        elif "boolean" in line:
            d.add("boolean")
            # print "bool"
        elif "short" in line:
            d.add("short")
            # print "bool"
        elif "float" in line:
            d.add("float")
            # print "float"
        elif "double" in line:
            d.add("double")
            # print "double"
        elif "long" in line:
            d.add("long")
            # print "long"
        else:
            for str in line:
                if "[" in str and "]" in str:
                    d.add("array")
    return d

def getOperatorOnDT(keylines, dataType):
    if dataType == "vector":
        print "vector"
    elif dataType == "list":
        print "list"
    elif dataType == "map":
        print "map"
    elif dataType == "set":
        print "set"
    elif dataType == "stack":
        print "stack"
    elif dataType == "queue":
        print "queue"
    elif dataType == "priority_queue":
        print "priority queue"
    elif dataType == "int":
        print "int"
    elif dataType == "char":
        print "char"
    elif dataType == "bool":
        print "bool"
    elif dataType == "float":
        print "float"
    elif dataType == "double":
        print "double"
    elif dataType == "long":
        print "long"
    elif dataType == "array":
        print "array"
    elif dataType == "pointer":
        print "pointer"
    return

def getDataType(keylines, lang):
    if lang == "c++":
        d = cppDataTypes(keylines)
        print d
    elif lang == "java":
        d = javaDataTypes(keylines)
        print d
