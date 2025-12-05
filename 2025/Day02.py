
#Part One
 sum = 0
answer = 0
for item in INPUT:
    x = item.split(sep="-")
    bottom = int(x[0])
    top = int(x[1])

    while bottom <= top:
        digits = math.floor(math.log10(bottom)) + 1
        if digits % 2 == 0:
            y = str(bottom)
            z = y[len(y)//2:]
            a = y[:len(y)//2]
            if z == a:
                answer += bottom
                print(f"Invalid id: {bottom}")
        bottom +=1

print(f"The answer is: {answer}")

#Part Two
sum = 0
answer = 0
for item in TESTINPUT:
    x = item.split(sep="-")
    bottom = int(x[0])
    top = int(x[1])
    
    while bottom <= top:
        digits = math.floor(math.log10(bottom)) + 1
        y = str(bottom)

        for i in range(digits):



            for j in range(digits):
                if i == 0 and y[i] != y[j]: break;
                


        if digits % 2 == 0:
            z = y[len(y)//2:]
            a = y[:len(y)//2]
            if z == a:
                answer += bottom
                print(f"Invalid id: {bottom}")
        bottom +=1

print(f"The answer is: {answer}")

