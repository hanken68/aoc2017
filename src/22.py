import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/22s.txt" if test else "src/inputs/22.txt"
p1 = p2 = 0

grid = open(inFile, "r").read().splitlines()
R=len(grid)
C=len(grid[0])

# Part 1
for line in grid:
    print(line)

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







