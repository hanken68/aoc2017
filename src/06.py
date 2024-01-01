import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/06s.txt" if test else "src/inputs/06.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

blocks = list(map(int, lines[0].split("\t")))
bnum = len(blocks)

# Part 1
seen = set()
seen.add(tuple(blocks))
cyclenum = 0
while True:
    cyclenum += 1
    maxnum = max(blocks)
    indx = blocks.index(maxnum)
    blocks[indx] = 0
    for i in range(maxnum): # Redistribute
        indx += 1
        if indx>= bnum:
            indx = 0
        blocks[indx] += 1
    tblock = tuple(blocks)
    if p1 == 0:
        if tblock in seen:
            p1 = cyclenum
            p2block = tblock
            print (f"Part 1: {p1}, {str(timer)}") 
        else:
            seen.add(tblock)
    else:
        if p2block == tblock:
            p2 = cyclenum - p1
            break

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







