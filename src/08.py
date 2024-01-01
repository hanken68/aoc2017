import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/08s.txt" if test else "src/inputs/08.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

registers = dict()
operators = {"inc": "+",
             "dec": "-"}
# Part 1
for line in lines:
    i1, op, val, _, i2, comp, cval = line.split()
    op = operators[op]
    if i1 not in registers:
        registers[i1] = 0
    if i2 not in registers:
        registers[i2] = 0
    if eval(str(registers[i2]) + comp + cval):
        evalnum  = eval(str(registers[i1]) + op + val)
        registers[i1] = evalnum
        p2 = max(p2, evalnum)

            
p1 = max(registers.values())

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







