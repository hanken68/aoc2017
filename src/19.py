import aoc
test = True
timer = aoc.executionTime()
#directions = ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))  # with diagonals
directions = ((-1,0),(1,0),(0,-1),(0,1))

inFile = "src/inputs/19s.txt" if test else "src/inputs/19.txt"
p1 = p2 = 0

grid = open(inFile, "r").read().splitlines()
R=len(grid)
C=len(grid[0])

c = grid[0].index("|")
r = 0
d = (1,0)
# Part 1
text = ""
while True:
    l = grid[r][c]
    print(r,c,l,d, text)
    if l == "+":
        for dr, dc in directions:
            rr = r + dr
            cc = c + dc
            if (dr,dc) == d or (dr == -d[0] and dc == -d[1]) or (rr < 0 or rr>=R or cc<0 or cc>=C): # only 90 degree allowed and inbounds
                continue
            if grid[rr][cc] != " ":
                d=(dr, dc)
                break
    elif not(l in "|-"):
        text += l
    elif l== " ":
        break
    r += d[0]
    c += d[1]

print (f"Part 1: {text}, {str(timer)}") 

# Part 2

print (f"Part 2: {p2}, {str(timer)}") 







