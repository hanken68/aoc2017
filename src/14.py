import aoc
from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/14s.txt" if test else "src/inputs/14.txt"
p1 = p2 = 0

code = open(inFile, "r").read()

def knothash(instr):
    numbers = [x for x in range(256)]
    curpos = 0
    skipsize = 0
    lengths = [ord(x) for x in instr] + [17, 31, 73, 47, 23]
    for x in range(64):
        for l in lengths:
            endpos = (curpos+l)
            if endpos > 256:
                ep = endpos%256
                wrap = l - ep
                nums = numbers[curpos:] + numbers[:ep]
            else:
                nums = numbers[curpos:endpos]
            nums.reverse()
            if endpos>256:
                numbers = nums[wrap:] + numbers[ep:curpos] + nums[:wrap]
            else:
                numbers = numbers[:curpos] + nums + numbers[endpos:]
            curpos = (curpos + l + skipsize)%256
            skipsize += 1

    resstring = ""
    for x in range(0,256,16):
        xnum = numbers[x]
        for i in range(x+1,x+16):
            xnum = xnum ^ numbers[i]
        hx = ("0" + hex(xnum)[2:])[-2:]
        resstring += hx
    return resstring

# Part 1
p2grid = []
for i in range(128):
    cc = code+"-"+str(i)
    ss = knothash(cc)
    ssbin = format(int(ss,16), "0128b")
    p2grid.append(list(ssbin))
    p1 += ssbin.count('1')

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

def findfirstrange():
    for r in range(128):
        try:
            c = p2grid[r].index("1")
            if c >= 0:
                return (r, c)
        except:
            pass
    return (-1,-1)

groupcount = 0
while True:
    r,c = findfirstrange()
    if r < 0:
        break
    groupcount += 1
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        p2grid[r][c] = "0"
        for d in directions:
            rr = r + d[0]
            cc = c + d[1]
            if rr<0 or rr>127 or cc<0 or cc > 127:
                continue
            if p2grid[rr][cc] == "1":
                q.append((rr,cc))

p2 = groupcount
print (f"Part 2: {p2}, {str(timer)}") 







