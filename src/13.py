import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/13s.txt" if test else "src/inputs/13.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

def progresslayer(l):
        d,s,dir = layers[l]
        if s+dir <0 or s+dir >=d:
            layers[l][2] = -layers[l][2]
        layers[l][1] = layers[l][1] + layers[l][2]
        if layers[l][1] == 0:
            return False
        else:
            return True

def progresscanners():
    allnonzero = True
    for l in layers:
        if not(progresslayer(l)):
            allnonzero = False
    return allnonzero


# Part 1

layers = dict()
numoflayers = 0
for line in lines:
    l, d = [int(x) for x in line.split(": ")]
    layers[l]=[d, 0, 1]
    numoflayers = l+1

cf = 0
ps = 0
while ps<numoflayers:
    if ps in layers and layers[ps][1]==0:
        cf += (layers[ps][0] * ps)
    progresscanners()
    ps += 1

p1 = cf
print (f"Part 1: {p1}, {str(timer)}") 



# Part 2

#prepare layers
layers = dict()
numoflayers = 0
for line in lines:
    l, d = [int(x) for x in line.split(": ")]
    layers[l]=[d, 0, 1]
    numoflayers = l+1
for x in range(1,numoflayers):
    if x in layers:
        for y in range(1,x+1):
            progresslayer(x)

delay = 0
while True:
    if progresscanners():
        break
    delay += 1
p2 = delay +1
print (f"Part 2: {p2}, {str(timer)}") 







