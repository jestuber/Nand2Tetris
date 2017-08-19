import sys
import Parser
import Code


SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576,
}

# read argument
filename = sys.argv[1]
# open asm file
asm_file = open(filename, "r")
# open hack file
hackname = "out.hack"
open(hackname, 'w').close()  # clear old output file
hack_file = open(hackname, "a")
n = 0  # initialize instruction count
# first pass to get instruction count of each label into symbol table
for line in asm_file:
    line = line.strip()
    if (len(line) == 0) or line.startswith('//'):
        continue
    if line.startswith("("):
        label = line[line.find("(") + 1:line.find(")")]
        SYMBOLS[label] = n
        continue
    n += 1
asm_file.close()
asm_file = open(filename, "r")
n = 16
for line in asm_file:
    line = line.strip()
    if (len(line) == 0) or line.startswith('//') or line.startswith("("):
        continue
# get instruction type
    instruct_type = Parser.getInstrType(line)
# parse line
    parsed = Parser.parse(line, instruct_type)
# convert @symbol to actual address
    if instruct_type == "A":
        try:
            int(parsed['Address'])
        except:  # address is a symbol
            try:
                parsed['Address'] = SYMBOLS[parsed['Address']]
            except:  # address is not already in symbols
                SYMBOLS[parsed['Address']] = n
                parsed['Address'] = n
                n += 1
# translate line
    binary = Code.translate(parsed, instruct_type)
# write line to hack file and newline
    hack_file.write(binary + "\n")

asm_file.close()
hack_file.close()
