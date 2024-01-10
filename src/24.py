import aoc
from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/24s.txt" if test else "src/inputs/24.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

compdict = dict()
components = dict()


for cnum, line in enumerate(lines):
    comp = [int(x) for x in line.split("/")]
    components[cnum] = tuple(comp)
    if comp[0] in compdict:
        compdict[comp[0]].append((cnum, comp[1]))
    else: 
        compdict[comp[0]] =[(cnum, comp[1])]
    if comp[1] in compdict:
        compdict[comp[1]].append((cnum, comp[0]))
    else: 
        compdict[comp[1]] =[(cnum, comp[0])]


# Part 1
q = deque()
q.append((0,0,set())) # node, sum, setused
p1 = 0
longest = 0
p2 = 0
while q:
    c, s, u = q.pop()
    p1 = max(p1, s)
    if len(u)>longest:
        longest = len(u)
        p2 = s
    elif len(u) == longest:
        p2 = max(p2,s)
    if c in compdict:
        for comp, nc in compdict[c]:
            if comp not in u:
                u1 = u.copy()
                u1.add((comp))
                q.append((nc, s+c+nc, u1))

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
print (f"Part 2: {p2}, {str(timer)}") 







