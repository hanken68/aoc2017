import aoc

from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/12s.txt" if test else "src/inputs/12.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

def addprogram(p, nodes):
    for n in nodes:
        if n not in programs:
            programs[n] = [set(), set()]
    if p not in programs:
        programs[p] = [set(), set()] # nodes to, nodes from
  
    [programs[p][0].add(x) for x in nodes]
    for n in nodes:
        programs[n][1].add(p)
    return

programs=dict()
vissited=set()
# Part 1
for line in lines:
    pp = line.split(" <-> ")
    addprogram(int(pp[0]),[int(x) for x in pp[1].split(", ")])

groups = 0
for x in programs:
    ispart1 = False
    if x not in vissited:
        groups+=1
        q = deque()
        q.append(x)
        linktotarget = set()

        while q:
            c = q.popleft()
            linktotarget.add(c)
            vissited.add(c)
            if c==0:
                ispart1 = True
            for cc in programs[c][1]:
                if cc not in linktotarget:
                    q.append(cc)
    if ispart1:
        p1 = len(linktotarget)

p2 = groups

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







