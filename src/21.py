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
     out = []
    # flip vertically
    for l in f:
        out.append(reversed(l))
    # flip horizontally
    out = []
    mapping[tuple(out)]= f
    for l in reversed(f):
        out.append(l)
    mapping[tuple(out)]= f
    
# Part 1
er = dict()
mapping = dict()
for line in lines:
    lp = line.split(" => ")
    f = lp[0].split("/")
    t = lp[1].split("/")
    er[tuple(f)] = tuple(t)
    generatemapping(f)


print (er)
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







