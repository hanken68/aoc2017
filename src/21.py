import aoc
import numpy
test = True
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
        m = numpy.array(f)
        for n in range(3): # rotate 3 times
            numpy.transpose(m)
            reversed(m)
            mapping[tuple(m)] = tuple(f)
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

for n in range(2 if test else 5):
    #expand grid
    newgrid = []
    R = C = len(grid)
    s = 2 if R%2 == 0 else 3
    for r in range(0, R, s):
        for rr in range(s):
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
            for rr in t:
                newgrid[r+rr] += t[rr]
    grid = newgrid.copy()



print (f"Part 1: {p1}, {str(timer)}") 



# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







