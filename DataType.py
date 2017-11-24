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
        elif "enum" in line:
            d.add("enums")
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
        elif "deque" in line:
            d.add("deque")
            # print "vector"
        elif "istringstream" in line:
            d.add("istringstream")
            # print "vector"
        elif "stringstream" in line:
            d.add("stringstream")
            # print "vector"
        elif "ostringstream" in line:
            d.add("ostringstream")
            # print "vector"
        elif "sstream" in line:
            d.add("sstream")
            # print "vector"
        elif "istream" in line:
            d.add("istream")
            # print "vector"
        elif "iostream" in line:
            d.add("iostream")
            # print "vector"
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
        elif "array" in "line":
            d.add("array")
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
        elif "enum" in line:
            d.add("enums")
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

def getDataType(keylines, lang):
    if lang == "c++":
        d = cppDataTypes(keylines)
        print d
    elif lang == "java":
        d = javaDataTypes(keylines)
        print d
