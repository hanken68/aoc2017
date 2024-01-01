import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/02s.txt" if test else "src/inputs/02.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

# Part 1
sumdiff = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    largest = 0
    smallest = 1e9
    for n in nums:
        largest = max(largest, n)
        smallest = min(smallest, n)
    sumdiff += (largest - smallest)

p1 = sumdiff
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
sumdiv = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    found = False
    for i, n in enumerate(nums):
        for x in nums[i+1:]:
            if max(n,x)%min(n,x) == 0:
                found = True
                sumdiv += (max(n,x)//min(n,x))
                break
        if found:
            break
p2 = sumdiv

print (f"Part 2: {p2}, {str(timer)}") 







