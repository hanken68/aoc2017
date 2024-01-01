import aoc
from collections import Counter
test = False
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/04s.txt" if test else "src/inputs/04.txt"
p1 = p2 = 0

lines = open(inFile, "r").read().splitlines()
R=len(lines)
C=len(lines[0])

# Part 1
numofvalidpassphrases = 0
for line in lines:
    wordsonline = line.split(" ")
    wordscount = Counter(wordsonline)
    if len(wordscount) == len(wordsonline):
        numofvalidpassphrases += 1

p1 = numofvalidpassphrases

print (f"Part 1: {p1}, {str(timer)}") 

# Part 2
numofvalidpassphrases = 0
for line in lines:
    wordsonline = line.split(" ")
    sortedwords = []
    for word in wordsonline:
        sortedwords.append("".join(sorted(word)))
    wordscount = Counter(sortedwords)
    if len(wordscount) == len(wordsonline):
        numofvalidpassphrases += 1

p2 = numofvalidpassphrases


print (f"Part 2: {p2}, {str(timer)}") 







