import sys
import Parser
import Code


# read argument
filename = sys.argv[1]
# open asm file
asm_file = open(filename, "r")
# open hack file
hackname = "out.hack"
open(hackname, 'w').close()  # clear old output file
hack_file = open(hackname, "a")
n = 0  # initialize instruction count
for line in asm_file:
    line = line.strip()
    if (len(line) == 0) or line.startswith('//') or line.startswith("("):
        continue

    n += 1
# get instruction type
    instruct_type = Parser.getInstrType(line)
# parse line
    parsed = Parser.parse(line, instruct_type)
# translate line
    binary = Code.translate(parsed, instruct_type)
# write line to hack file and newline
    hack_file.write(binary + "\n")
asm_file.close()
hack_file.close()
