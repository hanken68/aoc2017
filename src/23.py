import aoc
from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/23s.txt" if test else "src/inputs/23.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

program = []
registers = dict()

for line in lines:
    lp = line.split()
    instr = []
    for i, p in enumerate(lp):
        if i == 0:
            instr.append(p)
        else:
            if len(p) == 1 and not(p.isdecimal()):
                registers[p] = 0
                instr.append(p)
            else:
                instr.append(int(p))
    program.append(instr)


# Part 1
backup = registers.copy()
pc = 0
mulcounter = 0
while True:
    il = program[pc]
    instr = il[0]
    if instr == "set":
        registers[il[1]] = registers[il[2]] if il[2] in registers else il[2]
    elif instr == "sub":
        registers[il[1]] -= registers[il[2]] if il[2] in registers else il[2]
    elif instr == "mul":
        registers[il[1]] *= registers[il[2]] if il[2] in registers else il[2]
        mulcounter += 1
    elif instr=="jnz":
        if registers[il[1]] if il[1] in registers else il[1] != 0:
            pc += registers[il[2]] if il[2] in registers else il[2]
            pc -= 1
    pc += 1

    if pc<0 or pc>= len(program):
        break
p1 = mulcounter
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
registers = backup
pc = 0
registers['a'] = 1
while True:
    il = program[pc]
    if pc in (31,24,23):
        print(pc, registers)
    instr = il[0]
    if instr == "set":
        registers[il[1]] = registers[il[2]] if il[2] in registers else il[2]
    elif instr == "sub":
        registers[il[1]] -= registers[il[2]] if il[2] in registers else il[2]
    elif instr == "mul":
        registers[il[1]] *= registers[il[2]] if il[2] in registers else il[2]
    elif instr=="jnz":
        if registers[il[1]] if il[1] in registers else il[1] != 0:
            pc += registers[il[2]] if il[2] in registers else il[2]
            pc -= 1
    pc += 1
    if pc<0 or pc>= len(program):
        break
p2 = registers['h']
print (f"Part 2: {p2}, {str(timer)}") 



# 997 is too high

