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
    print(p, programs[p])
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
pq = deque()
pq.append(p1)
while pq:
    prog = pq.popleft()
    print (prog, programs[prog][1])


print (f"Part 2: {p2}, {str(timer)}") 







