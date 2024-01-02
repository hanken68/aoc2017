import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
#directions = ((-1,0),(1,0),(0,-1),(0,1))
directions = {"n": (1,0,0),
              "s": (-1,0,0),
              "ne": (0,1,0),
              "sw": (0,-1,0),
              "nw": (0,0,1),
              "se": (0,0,-1)}

inFile = "src/inputs/11s.txt" if test else "src/inputs/11.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

x,y,z = (0,0,0)
# Part 1
for dir in lines[0].split(","):
    dd = directions[dir]
    x += dd[0]
    y += dd[1]
    z += dd[2]

print(x,y,z)

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







