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
for i, line in enumerate(lines):
    parts = line.split(", ")
    particle = []
    for p in parts:
        r = [int(x) for x in re.findall(r"-?\d+", p)]
        particle.append(r)
    particles.append(particle)
    if sum([abs(x) for x in particle[2]])==1:
        tempmin = sum([particle[1][x] * particle[2][x] for x in range(3)])
        if tempmin < totmin:
            totmin = tempmin
            p1 = i    
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

t = 0
while True:
    collides = set()
    for p in particles:
        for n in range(3):
            p[1][n] += p[2][n]
            p[0][n] += p[1][n]
    R = len(particles)
    for p1 in range(R-1):
        for p2 in range(p1+1,R):
            if particles[p1][0] == particles[p2][0]:
                collides.add(p1)
                collides.add(p2)
    for p in sorted(collides, reverse=True):
        del particles[p]
    if len(collides)>0:
        t = 0
    p2 = len(particles)
    t += 1
    if len(particles) == 1 or t > 50:
        break

print (f"Part 2: {p2}, {str(timer)}") 







