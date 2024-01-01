import aoc
test = True
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
print(numbers)
for l in lengths:
    endpos = (curpos+l)
    if endpos > numbercount:
        ep = endpos%numbercount
        nums = numbers[curpos:] + numbers[:ep]
    else:
        nums = numbers[curpos:endpos]
    nums.reverse()
    if endpos>numbercount:
        print(nums[-ep:])
        numbers = nums[:-ep] + numbers[ep:curpos] + nums[:ep]
    else:
        numbers = numbers[:curpos] + nums + numbers[endpos:]
    curpos = (curpos + l + skipsize)%numbercount
    skipsize += 1
    print(curpos, skipsize, numbers, nums)

p1 = numbers[0] * numbers[1]
print (numbers)

print (f"Part 1: {p1}, {str(timer)}") 

# 32220 is too low

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







