import aoc
from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/07s.txt" if test else "src/inputs/07.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

programs = dict()
# Part 1

for line in lines:
    p = line.split(" -> ")
    pp = p[0].split(" (")
    programs[pp[0]] = [int(pp[1][:-1]), [], [], 0] # number, supports, supported by, weight of supports
    if len(p)>1:
        for s in p[1].split(", "):
            programs[pp[0]][1].append(s)

for p in programs:
    if len(programs[p][1])>0:
        for x in programs[p][1]:
            programs[x][2].append(p)

for p in programs:
    if programs[p][2] == []:
        p1 = p

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
def getWeight(prog):
    w = programs[prog][0]
    supports = programs[prog][1]
    sw = 0
    for s in supports:
        ssw = getWeight(s)
        sw += ssw
        programs[s][3] = ssw
    return w + sw

w = getWeight(p1)
print(w)

print(programs[p1])
nums= dict()
for p in programs[p1][1]:
    w = programs[p][3]
    print(p, programs[p])
    if w in nums:
        nums[w].append(p)
    else:
        nums[w] = [p]
for w in nums:
    if len(nums[w]) == 1:
        weight = w
    else:
        refweight = w
candidate = nums[weight][0]
cw = programs[candidate][0]
for x in programs['yruivis'][1]: # Manual hacky solution
    print(x, programs[x])S
print (weight, refweight, candidate, cw, (weight- refweight) )
print (f"Part 2: {p2}, {str(timer)}") 

# 2751 is to high 







