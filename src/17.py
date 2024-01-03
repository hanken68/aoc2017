import aoc
test = False
timer = aoc.executionTime()

forward = 3 if test else 343
p1 = p2 = 0


buffer = [0]
curpos = 0
# Part 1
print (forward)
for x in range(2017):
    curpos = (curpos + forward)%(len(buffer))+1
    buffer.insert(curpos,x+1)

p1 = buffer[curpos+1] # Value after newly inserted 2017

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
lenbuf = 1
for x in range(50000000):
    curpos = (curpos + forward)%(lenbuf)+1
    if curpos == 1:
        p2 = x+1
    lenbuf += 1

print (f"Part 2: {p2}, {str(timer)}") 







