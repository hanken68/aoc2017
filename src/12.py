import aoc
import sys
sys.setrecursionlimit(10000)
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

def followtox(p, x):
    if p == x:
        linktotarget.add(p)
        return True
    if p in linktotarget:
        return True
    for pp in programs[p][0]:
        if x == pp:
            linktotarget.add(p)
            return True
        if followtox(pp, x):
            return True
    return False


linktotarget = set()
programs=dict()
# Part 1
for line in lines:
    pp = line.split(" <-> ")
    addprogram(int(pp[0]),[int(x) for x in pp[1].split(", ")])

for p in programs:
    followtox(p,0)
p1 = len(linktotarget)
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







