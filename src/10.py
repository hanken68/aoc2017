import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/10s.txt" if test else "src/inputs/10.txt"
numbercount = 5 if test else 256
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])


numbers = [x for x in range(numbercount)]
curpos = 0
skipsize = 0

# Part 1
lengths = [int(x) for x in lines[0].split(",")]

for l in lengths:
    endpos = (curpos+l)
    if endpos > numbercount:
        ep = endpos%numbercount
        wrap = l - ep
        nums = numbers[curpos:] + numbers[:ep]
    else:
        nums = numbers[curpos:endpos]
    nums.reverse()
    if endpos>numbercount:
        numbers = nums[wrap:] + numbers[ep:curpos] + nums[:wrap]
    else:
        numbers = numbers[:curpos] + nums + numbers[endpos:]
    curpos = (curpos + l + skipsize)%numbercount
    skipsize += 1


p1 = numbers[0] * numbers[1]


print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
numbers = [x for x in range(numbercount)]
curpos = 0
skipsize = 0
lengths = [ord(x) for x in lines[0]] + [17, 31, 73, 47, 23]
for x in range(64):
    for l in lengths:
        endpos = (curpos+l)
        if endpos > numbercount:
            ep = endpos%numbercount
            wrap = l - ep
            nums = numbers[curpos:] + numbers[:ep]
        else:
            nums = numbers[curpos:endpos]
        nums.reverse()
        if endpos>numbercount:
            numbers = nums[wrap:] + numbers[ep:curpos] + nums[:wrap]
        else:
            numbers = numbers[:curpos] + nums + numbers[endpos:]
        curpos = (curpos + l + skipsize)%numbercount
        skipsize += 1

resstring = ""
for x in range(0,256,16):
    xnum = numbers[x]
    for i in range(x+1,x+16):
        xnum = xnum ^ numbers[i]
    hx = ("0" + hex(xnum)[2:])[-2:]
    resstring += hx
p2 = resstring

print (f"Part 2: {p2}, {str(timer)}") 







