import aoc
import numpy
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/21s.txt" if test else "src/inputs/21.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])
def generatemapping(f):
    m = f
    for n in range(3): # rotate 3 times
        m = list(zip(*m))
        m = list(["".join(l[::-1]) for l in m])
        t = tuple(m)
        if t != f:
            mapping[t] = tuple(f)
    out = []
    # flip vertically
    for l in f:
        out.append("".join(reversed(l)))
    t = tuple(out)
    if out != f:
        mapping[t]= tuple(f)
    m = out
    for n in range(3): # rotate 3 times
        m = list(zip(*m))
        m = list(["".join(l[::-1]) for l in m])
        t = tuple(m)
        if t != f:
            mapping[t] = tuple(f)
    return
# Part 1
er = dict()
mapping = dict()
for line in lines:
    lp = line.split(" => ")
    f = lp[0].split("/")
    t = lp[1].split("/")
    er[tuple(f)] = tuple(t)
    generatemapping(f)

grid = [".#.","..#", "###"]

for numiter in range(2 if test else 18):
    #expand grid
    newgrid = []
    R = C = len(grid)
    s = 2 if R%2 == 0 else 3
    rc = 0
    for r in range(0, R, s):
        for rr in range(s+1):
            newgrid.append("")
        for c in range(0,C,s):
            arr = []
            for n in range(s):
                arr.append(grid[r+n][c:c+s])
            c = tuple(arr)
            if c in er:
                t = er[c]
            else:
                t = er[mapping[c]]
            for rr, newrow in enumerate(t):
                newgrid[rc+rr] += newrow
        rc += (s+1)
    grid = newgrid.copy()
    if numiter == 4:
        for x in grid:
            p1 += x.count("#")
        print (f"Part 1: {p1}, {str(timer)}") 
    

for x in grid:
    p2 += x.count("#")

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







