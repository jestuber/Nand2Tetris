def getInstrType(line):
    if line.startswith("@"):
        return "A"
    else:
        return "C"


def parse(line, type):
    if type == "A":
        # get number after @
        address = line[1:]
        parsed = {'Address': address}
        return parsed
    if type == "C":
        # split into dest, comp, jump
        split_eq = line.split('=')
        if len(split_eq) == 1:
            dest = None
            rhs = split_eq[0]
        else:
            dest = split_eq[0]
            rhs = split_eq[1]
        split_semi = rhs.split(';')
        if len(split_semi) == 1:
            comp = split_semi[0]
            jump = None
        else:
            comp = split_semi[0]
            jump = split_semi[1]
        parsed = {'Dest': dest, 'Comp': comp, 'Jump': jump}
        return parsed
