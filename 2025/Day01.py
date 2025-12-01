import math
INPUT = ["L10", "R50", "R4500", "L0", "R99", "R100"]
X = 100
curr_pos = 50
answer = 0
for rota in INPUT:
    rotaNum = int(rota[:1])

    if rota[0].lower() == "l":
        rotaNum *-1;

    answer += math.floor(rotaNum / x)

    modulo = rotaNum % x
    y = curr_pos + rotaNum
    if curr_pos + rotaNum < 0:
        
