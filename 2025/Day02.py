import math
sum = 0
for item in INPUT:
    x = item.split(sep="-")
    bottom = int(x[0])
    top = int(x[1])
    b_digits = math.floor(math.log10(bottom)) + 1
    t_digits = math.floor(math.log10(top)) + 1

    if b_digits == t_digits and t_digits % 2 != 0:
        print(bottom)



    if abs(b_digits - t_digits) >= 2: print(bottom)
""" 
    if b_digits % 2 == 0 or t_digits % 2 == 0:
        if b_digits % 2 != 0: 
   
    if math.log10(bottom) + math.log10(top) + 2 % 2 == 0:
        while bottom <= top:
            print(bottom)
            bottom += 1 """

