import aoc
test = False
timer = aoc.executionTime()

inFile = "src/inputs/09s.txt" if test else "src/inputs/09.txt"
p1 = p2 = 0

stream = open(inFile, "r").read()
C=len(stream)

# Part 1
groups = []
nums = []
state = 0 # search for group
level = 1
cancelnum = 0
for c in stream:
    if state == 0:
        if c =="{":
            groups.append(level)
            level += 1
        elif c=="}":
            nums.append(groups.pop())
            level -= 1
        if c == "<":
            state = 1 # Garbage
    elif state == 1:
        if c == "!":
            state = 2
        elif c == ">":
            state = 0
        else:
            cancelnum += 1
    elif state == 2:
        state = 1

#print(nums)
        
p1 = sum(nums)
p2 = cancelnum
    



print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







