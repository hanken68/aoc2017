import aoc
import re
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/20s.txt" if test else "src/inputs/20.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])
particles = []
# Part 1
totmin = 1e9
pcount = 0
for line in lines:
    parts = line.split(", ")
    particle = []
    for p in parts:
        r = tuple([int(x) for x in re.findall(r"-?\d+", p)])
        particle.append(r)
    particles.append(particle)
    aminmax = max([abs(x) for x in particle[2]])
    if aminmax <= totmin:
        print (aminmax, particle, pcount)
        totmin = aminmax
        p1 = pcount
    pcount += 1

#print (particles)

# 279 is too low
# 426 is too high
    
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







