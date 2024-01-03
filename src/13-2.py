import aoc
test = True
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

def progresscanners():
    for l in layers:
        progresslayer(l)
        


# Part 1
delay = 0
while True:
    layers = dict()
    numoflayers = 0
    for line in lines:
        l, d = [int(x) for x in line.split(": ")]
        layers[l]=[d, 0, 1]
        numoflayers = l+1

    cf = 0
    cc = 0
    ps = 0
    while ps-delay<numoflayers:
        if ps>=delay:
            pd = ps-delay
            if pd in layers and layers[pd][1]==0:
                cf += (layers[pd][0] * pd)
                cc += 1
        progresscanners()
        ps += 1

    if delay == 0:  
        p1 = cf
        print (f"Part 1: {p1}, {str(timer)}") 
        break
    if cc == 0:
        break
    delay += 1
    if delay%1000 == 0:
        print(delay, cc, str(timer))


# Part 2

#prepare layers
layers = dict()
numoflayers = 0
for line in lines:
    l, d = [int(x) for x in line.split(": ")]
    layers[l]=[d, 0, 1]
    numoflayers = l+1
for x in range(numoflayers,0,-1):
    if x in layers:
        for y in range(x,-1,-1):
            progresslayer(x)
    

p2 = delay
print (f"Part 2: {p2}, {str(timer)}") 







