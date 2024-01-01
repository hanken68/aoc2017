import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/05s.txt" if test else "src/inputs/05.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

# Part 1
jumps = [int(x) for x in lines]
pc = 0
stepcounter = 0
while pc>=0 and pc < len(jumps):
    jump = jumps[pc]
    jumps[pc] += 1
    pc += jump
    stepcounter += 1

p1 = stepcounter
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
jumps = [int(x) for x in lines]
pc = 0
stepcounter = 0
while pc>=0 and pc < len(jumps):
    jump = jumps[pc]
    modifier = -1 if jump >=3 else 1
    jumps[pc] = jumps[pc] + modifier
    pc += jump
    stepcounter += 1

p2 = stepcounter
print (f"Part 2: {p2}, {str(timer)}") 







