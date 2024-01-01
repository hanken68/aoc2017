import aoc
import math
test = False
timer = aoc.executionTime()
directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
#directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/03s.txt" if test else "src/inputs/03.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])
input = int (lines[0])

# Part 1
print(input)

sqnf = math.sqrt(input-1)
sqni = math.floor(sqnf)
it = sqni - 1 if sqni%2 ==0 else sqni
start = int(math.pow(it,2)) + 1

sidelength = it + 2
x = it//2 + 1 
y = (x-1) * -1
omkrets =  sidelength * 4 - 4


rest = input-start
while True:
    if rest >= (sidelength - 2): #Opp høyre
        rest -= (sidelength-2)
        y += (sidelength-2)
    else:
        y += rest
        break
    if rest >= (sidelength -1): # tilbake topp
        rest -= (sidelength - 1)
        x -= (sidelength-1)
    else:
        x -= rest
        break
    if rest >= (sidelength -1):  # ned venstre
        rest -= (sidelength -1)
        y -= (sidelength-1)
    else:
        x += rest
        break
    x += rest
    break
p1 = abs(x) + abs (y)
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
def getnextxy(x,y,d, xmax, xmin, ymax, ymin):
    xx = x + d[0]
    yy = y + d[1]
    if xx > xmax +1:
        d = nextdirs[d]
        xx = x + d[0]
        yy = y + d[1]
        xmax += 1
    if xx < xmin -1:
        d = nextdirs[d]
        xx = x + d[0]
        yy = y + d[1]
        xmin -= 1
    if yy > ymax +1 :
        d = nextdirs[d]
        xx = x + d[0]
        yy = y + d[1]
        ymax += 1
    if yy < ymin -1:
        d = nextdirs[d]
        xx = x + d[0]
        yy = y + d[1]
        ymin -= 1
    return xx,yy, d, xmax,xmin,ymax, ymin


values = dict()
x = y = 0 
curval = 0
values[(0,0)] = 1
xmax = xmin = ymax = ymin = 0

nextdirs={(1,0): (0,1),
          (0,1): (-1,0),
          (-1,0): (0,-1),
          (0,-1): (1,0)}

movedir = (1,0)

while True:
    x, y, movedir, xmax, xmin, ymax, ymin = getnextxy(x,y, movedir, xmax, xmin, ymax, ymin)
    curval = 0
    for d in directions:
        xx = x + d[0]
        yy = y + d[1]
        if (xx,yy) in values:
            curval += values[(xx,yy)]
        if curval > input:
            p2 = curval
            break
    values[(x,y)] = curval
    if p2 != 0:
        break

print (f"Part 2: {p2}, {str(timer)}") 


#444119 to high
#438563 to high




