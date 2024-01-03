import aoc
from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/18s.txt" if test else "src/inputs/18.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

program = []
registers = dict()
regp2 = [dict(), dict()]
buffer = [deque(), deque()]
rcvcounter = [0,0]
sendcounter = [0,0]
lastsound = -1

for line in lines:
    lp = line.split()
    instr = []
    for i, p in enumerate(lp):
        if i == 0:
            instr.append(p)
        else:
            if len(p) == 1 and not(p.isdecimal()):
                registers[p] = 0
                regp2[0][p] = 0
                regp2[1][p] = 0
                instr.append(p)
            else:
                instr.append(int(p))
    program.append(instr)

def excecuteprogram(pnum):
    buf = buffer[pnum]
    il = program[pc[pnum]]
    instr = il[0]
    registers = regp2[pnum]
    if instr == "snd":
        buf.append(registers[il[1]] if il[1] in registers else il[1])
        sendcounter[pnum] += 1
    elif instr == "set":
        registers[il[1]] = registers[il[2]] if il[2] in registers else il[2]
    elif instr == "add":
        registers[il[1]] += registers[il[2]] if il[2] in registers else il[2]
    elif instr == "mul":
        registers[il[1]] *= registers[il[2]] if il[2] in registers else il[2]
    elif instr == "mod":
        registers[il[1]] = registers[il[1]] % (registers[il[2]] if il[2] in registers else il[2])
    elif instr == "rcv":
        if buf:
            registers[il[1]] = buf.popleft()
        else:
            rcvcounter[pnum] += 1
            return rcvcounter[pnum] <= 4
    elif instr=="jgz":
        if (registers[il[1]] if il[1] in registers else il[1]) > 0:
            pc[pnum] += registers[il[2]] if il[2] in registers else il[2]
            pc[pnum] -= 1
    pc[pnum] += 1

    if pc[pnum]<0 or pc[pnum]>= len(program):
        return False
    return True

# Part 1
# pc = 0
# while True:
#     il = program[pc]
#     instr = il[0]
#     if instr == "snd":
#         lastsound = registers[il[1]]
#     elif instr == "set":
#         registers[il[1]] = registers[il[2]] if il[2] in registers else il[2]
#     elif instr == "add":
#         registers[il[1]] += registers[il[2]] if il[2] in registers else il[2]
#     elif instr == "mul":
#         registers[il[1]] *= registers[il[2]] if il[2] in registers else il[2]
#     elif instr == "mod":
#         registers[il[1]] = registers[il[1]] % (registers[il[2]] if il[2] in registers else il[2])
#     elif instr == "rcv":
#         if registers[il[1]] != 0:
#             p1 = lastsound
#             break
#     elif instr=="jgz":
#         if registers[il[1]] > 0:
#             pc += registers[il[2]] if il[2] in registers else il[2]
#             pc -= 1
#     pc += 1

#     if pc<0 or pc>= len(program):
#         break

# print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
pc = [0,0]
running = [True, True]
while sum(running)>0:
    for p in [0,1]:
        if running[p]:
            running[p] = excecuteprogram(p)

p2 = sendcounter[1]

print (f"Part 2: {p2}, {str(timer)}") 


# 14986 is too high




