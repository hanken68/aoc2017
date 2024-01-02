import aoc
from collections import deque
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
#directions = ((-1,0),(1,0),(0,-1),(0,1))
# directions = {"n": (1,0,0),
#               "s": (-1,0,0),
#               "ne": (0,1,0),
#               "sw": (0,-1,0),
#               "nw": (0,0,1),
#               "se": (0,0,-1)}
directions = {"n": (0,1),
              "s": (0,-1),
              "ne": (1,0),
              "sw": (-1,0),
              "nw": (-1,1),
              "se": (1,-1)}

inFile = "src/inputs/11s.txt" if test else "src/inputs/11.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])
maxx = maxy = 0
x,y = (0,0)
# Part 1
for dir in lines[0].split(","):
    dd = directions[dir]
    x += dd[0]
    y += dd[1]
    if abs(x) > abs(maxx):
        maxx = x 
    if abs(y) > abs(maxy):
        maxy = y


# visited = set()
# q = deque()

target = (x,y)

p1 = max(abs(x), abs(y))
p2 = max(abs(maxx), abs(maxy))
# q.append((0,0,0))
# stepcount = 0
# found = False
# while q and not(found):
#     x, y, sc = q.popleft()
#     # print (x,y,sc)
#     for d in directions:
#         dd = directions[d]
#         xx, yy = x+dd[0], y+dd[1]
#         if (xx,yy) in visited:
#             continue
#         if (xx,yy) == target:
#             found = True
#             # print(sc)
#             p1 = sc +1
#             break
#         q.append((xx,yy,sc+1))
#         visited.add((xx,yy))


print (f"Part 1: {p1}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







