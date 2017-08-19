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
        dest = split_eq[0]
        rhs = split_eq[1]
        split_semi = rhs.split(';')
        comp = split_semi[0]
        jump = split_semi[1]
        parsed = {'Dest': dest, 'Comp': comp, 'Jump': jump}
        return parsed
