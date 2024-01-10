import aoc
test = False
timer = aoc.executionTime()

inFile = "src/inputs/25s.txt" if test else "src/inputs/25.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

dirdict = {'right': 1, 'left': -1}
# Part 1
startstate = lines[0][-2:-1]
numsteps = int(lines[1].split()[5])
print (startstate, numsteps)
states = dict()

for l in range(3, R, 10):
    state = lines[l][-2:-1]
    w1 = int(lines[l+2][-2:-1])
    m1 = dirdict[lines[l+3].split()[-1][:-1]]
    n1 = lines[l+4][-2:-1]
    w2 = int(lines[l+6][-2:-1])
    m2 = dirdict[lines[l+7].split()[-1][:-1]]
    n2 = lines[l+8][-2:-1]
    states[state]={0: (w1,m1,n1), 1: (w2,m2,n2)}

for s in states:
    print (s, states[s])

tape = [0]
pos = 0
state = startstate
for s in range(numsteps):
    val = states[state][tape[pos]][0]
    dir = states[state][tape[pos]][1]
    nextstate = states[state][tape[pos]][2]
    tape[pos] = val
    pos += dir
    if pos<0:
        tape.insert(0,0)
        pos+=1
    elif pos==len(tape):
        tape.append(0)
    state = nextstate
p1 = tape.count(1)

print (f"Part 1: {p1}, {str(timer)}") 







