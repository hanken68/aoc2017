import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/01s.txt" if test else "src/inputs/01.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

input = lines[0]

for part in [1,2]:
    # Part 1
    c=0  # Start at first position
    capcha = 0
    step = 1 if part == 1 else C//2
    while True:
        next = c + step
        if next >= C:
            next = 0 if part == 1 else next - C
        if input[c] == input[next]:
            capcha += int(input[c])
        c += 1
        if c >= C:
            break
    
    print (f"Part {part}: {capcha}, {str(timer)}") 



