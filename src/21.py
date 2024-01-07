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
    conversions = 0
    out = []
    # flip vertically
    for l in f:
        out.append("".join(reversed(l)))
    t = tuple(out)
    if out != f:
        mapping[t]= tuple(f)
        conversions += 1
    # flip horizontally
    out = []
    for l in reversed(f):
        out.append(l)
        conversions += 1
    if out != f:
        mapping[tuple(out)]= tuple(f)
    if conversions > 0:
        m = f
        for n in range(3): # rotate 3 times
            m = list(zip(*m))
            m = list(["".join(l[::-1]) for l in m])
            t = tuple(m)
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
for m in mapping:
    print(m, mapping[m])

grid = [".#.","..#", "###"]

for n in range(2 if test else 5):
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

nums = 0
for x in grid:
    nums += x.count("#")

p1 = nums
print (f"Part 1: {p1}, {str(timer)}") 



# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







