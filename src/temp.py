import math
numb = 265149
numb = 1024


sqnf = math.sqrt(numb-1)
sqni = math.floor(sqnf)
it = sqni - 1 if sqni%2 ==0 else sqni
start = int(math.pow(it,2)) + 1

sidelength = it + 2
x = it//2 + 1 
y = (x-1) * -1
omkrets =  sidelength * 4 - 4

print(numb, sidelength, start, x, y, omkrets, numb - start)
rest = numb-start
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

print (abs(x) + abs (y))
