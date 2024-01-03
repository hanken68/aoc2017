import aoc
import re
test = False 
timer = aoc.executionTime()

inFile = "src/inputs/15s.txt" if test else "src/inputs/15.txt"
iterations = 5 if test else 40000000
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])
gastart = int(re.findall(r"\d+", lines[0])[0])
gbstart = int(re.findall(r"\d+", lines[1])[0])
div=2147483647
gfa = 16807
gfb = 48271

# Part 1
comp = 0
ga = gastart
gb = gbstart
for x in range(iterations):
    ga = (ga * gfa)%div
    gb = (gb * gfb)%div
    comp += (ga & 65535) == (gb & 65535)

p1 = comp
print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
comp = 0
ga = gastart
gb = gbstart
for x in range(5000000):
    while True:
        ga = (ga * gfa)%div
        if ga%4 == 0:
            break
    while True:
        gb = (gb * gfb)%div
        if gb%8 == 0:
            break
    comp += ((ga & 65535) == (gb & 65535))

p2 = comp
print (f"Part 2: {p2}, {str(timer)}")

