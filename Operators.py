def getOperatorTags(line):
    op = set()
    temp = getOperatorOnDT(line)
    op.update(temp)
    temp1 = basicOpTag(line)
    op.update(temp1)
    if len(op) == 0:
        op.add("operator")


def basicOpTag(line):
    op = set()
    if "+" in line:
        op.add("add")
    if "-" in line:
        op.add("subtract")
    if "*" in line:
        op.add("multiplying")
    if "/" in line:
        op.add("divide")
    if "%" in line:
        op.add("modulo")
    if "=" in line:
        op.add("assignment")
    if "+=" in line or "-=" in line or "*=" in line or "/=" in line or \
                    "%=" in line or "&=" in line or "^=" in line or "~=" in line or "<<=" in line or ">>=" in line:
        op.add("compound-assignment")
        op.add("compound-operator")
    if "++" in line:
        op.add("increment")
    if "--" in line:
        op.add("decrement")
    if "==" in line:
        op.add("equals")
        op.add("comparision")
    if "!=" in line or "<" in line or ">" in line or "<=" in line or ">=" in line:
        op.add("relational")
        op.add("comparision")
    if "||" in line or "!" in line or "&&" in line:
        op.add("logical-operators")
    if "&" in line or "|" in line or "~" in line or "^" in line:
        op.add("bit-manipulation")
        op.add("bitwise-operators")
    if "<<" in line or ">>" in line:
        op.add("bit-shift")
        op.add("bit-shift-operators")
    if "?" in line:
        op.add("conditional")

    return op


def getOperatorOnDT(line):
    temp = ["add", "get", "assign", "push", "pop", "insert", "erase", "delete", "swap", "resize", "clear", "splice",
            "contains",
            "unique", "merge", "reverse", "emplace", "peek", "search", "clone", "get"]
    ops = [x for x in temp if x in line]
    if "max_size" in line:
        ops += ["max-size"]
    if "push_back" in line:
        ops += ["push-back"]
    if "pop_back" in line:
        ops += ["pop"]
    if "emplace_back" in line:
        ops += ["emplace"]
    if "sort" in line:
        ops += ["sorting"]
    if "lower_bound" in line:
        ops += ["lower-bound"]
    if "upper_bound" in line:
        ops += ["upperbound"]
    if "lower_bound" in line:
        ops += ["lower-bound"]
    if "equal_range" in line:
        ops += ["equal-range"]
    if "indexOf" in line:
        ops += ["indexof"]
    if "valueOf" in line:
        ops += ["value-of"]
    if "toString" in line:
        ops += ["tostring"]

    return ops


