INPUT = [
    "R1",
    "L1"
]
X = 100
curr_pos = 50
answer = 0
total_input = 0
for rota in INPUT:
    rota_num = int(rota[1:])
    total_input += 1
    if rota[0].lower() == "l":
        rota_num *= -1;

    y = curr_pos + rota_num
    if y < 0 or y > X:
        curr_pos = y % X
    elif y == 0 or y == X:
        curr_pos = 0
    else:
        curr_pos = y
    
    if curr_pos == 0:
        answer += 1

print(f"The answer is: {answer} and the total input was {total_input}")
