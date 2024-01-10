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

components = dict()
c2 = set()
# Part 1
for line in lines:
    comp = [int(x) for x in line.split("/")]
    if comp[0] in components:
        components[comp[0]].append(comp[1])
    else: 
        components[comp[0]] =[comp[1]]
    c2.add(tuple(comp))

print(components)
print (len(c2), len(components))
q = deque()
q.append((0,set()))
used = set()
while q:
    c, u = q.pop()
    for nc in components[c]:
        q.append(nc,)
    
    

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







