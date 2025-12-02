INPUT = [
    "R1",
    "L1"
]
X = 100
curr_pos = 50
answer = 0
for rota in INPUT:
    rotaNum = int(rota[1:])

    if rota[0].lower() == "l":
        rotaNum *= -1;

    y = curr_pos + rotaNum
    if y < 0:
        curr_pos = y % X
    elif y > X:
        curr_pos = y % X
    elif y == 0 or y == X:
        answer += 1
        curr_pos = 0
    else:
        curr_pos = y

print(f"The answer is: {answer}")
