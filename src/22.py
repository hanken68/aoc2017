import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))
left = {(-1,0): (0,-1),
        (1,0): (0,1),
        (0,-1): (1,0),
        (0,1): (-1,0)}
right = {(-1,0): (0,1),
        (1,0): (0,-1),
        (0,-1): (-1,0),
        (0,1): (1,0)}
inFile = "src/inputs/22s.txt" if test else "src/inputs/22.txt"
p1 = p2 = 0

grid = open(inFile, "r").read().splitlines()
R=len(grid)
C=len(grid[0])


viruses = set()
for r, line in enumerate(grid):
    for c, l in enumerate(line):
        if l == "#":
            viruses.add((r,c))

r = c = R//2 
dir = (-1,0)

backup = viruses.copy()
# Part 1
infections = 0
burst = 0
while True:
    burst += 1 
    if (r,c) in viruses:
        dir = right[dir]
        viruses.remove((r,c))
    else:
        dir = left[dir]
        viruses.add((r,c))
        infections += 1
    r += dir[0]
    c += dir[1]   
    if burst == 10000:
        p1 = infections
        print (f"Part 1: {p1}, {str(timer)}") 
        break

# Part 2
r = c = R//2 
dir = (-1,0)
infected = backup
weakened=set()
flagged=set()

infections = 0
burst = 0
while True:
    burst += 1 
    if (r,c) in weakened:
        weakened.remove((r,c))
        infected.add((r,c))
        infections += 1
    elif (r,c) in infected:
        infected.remove((r,c))
        flagged.add((r,c))
        dir=right[dir]
    elif (r,c) in flagged:
        flagged.remove((r,c))
        dir = (-dir[0], -dir[1])
    else: #clean
        weakened.add((r,c))
        dir = left[dir]

    r += dir[0]
    c += dir[1]   
    if burst == 10000000:
        p2 = infections
        break
print (f"Part 2: {p2}, {str(timer)}") 




