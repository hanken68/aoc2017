import aoc
import math
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/23s.txt" if test else "src/inputs/23.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

def primeCheck(x):
    sta = 1
    for i in range(2,int(math.sqrt(x))+1): # range[2,sqrt(num)]
        if(x%i==0):
            sta=0
            break
        else:
            continue
    return sta



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
<<<<<<< HEAD
registers = backup
pc = 0
registers['a'] = 1
while True:
    il = program[pc]
    if pc in (20,31,24,23):
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



# 983 is too high
# 964 is wrong
# 966 is wrong
# 483 is wrong
# 968 is wrong
# 949 is wrong

=======
# Analyced code and found out that it was a loop that incremented h if b was not a prime number
b = 106500
c = 123500
h = 0
for x in range(b, c+1, 17):
    if not(primeCheck(x)):
        h += 1
p2 = h
print (f"Part 2: {p2}, {str(timer)}") 
>>>>>>> e1ee929 (Year 2017 completed)
