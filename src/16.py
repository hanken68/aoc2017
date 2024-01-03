import aoc
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/16s.txt" if test else "src/inputs/16.txt"
p1 = p2 = 0

line = open(inFile, "r").read()
dance = line.split(",")
programs = [chr(x+97) for x in range(16) ]
startprogram = programs.copy()
l = len(programs)


def spin(x):
    global programs
    programs = programs[-x:] + programs[:l-x]
    return

def exchange(x, y):
    px = programs[x]
    programs[x] = programs[y]
    programs[y] = px
    return

def partner(p1, p2):
    x = programs.index(p1)
    y = programs.index(p2)
    exchange(x,y)
    return
def dothedance():
    for dm in dance:
        d = dm[0]
        instr = dm[1:]
        if d == "s":
            spin(int(instr))
        elif d == "x":
            exchange(*[int(x) for x in instr.split("/")])
        elif d == "p":
            partner(*instr.split("/"))

# Part 1
# Part 2
lastx = 0
breakx = 1000000000
combinations = []

repeat = False
for x in range(0, 1000000000):
    if programs == startprogram and x > 0:
        repeat = True
        breakx = 1000000000%x
    if not(repeat):
        combinations.append("".join(programs))
    dothedance()
    if x == 0:
        p1 = "".join(programs)
        print (f"Part 1: {p1}, {str(timer)}") 
    if x> breakx+1:
        break


p2 = combinations[breakx]

print (f"Part 2: {p2}, {str(timer)}") 
