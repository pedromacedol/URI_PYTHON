a = float(input())
if 0 <= a <= 2000:
    print("Isento")
elif 2000 < a <= 3000:
    calc = ((a - 2000)/100)*8
    print("R$ %.2f" %calc)
elif 3000 < a <= 4500:
    calc = a - 3000
    x = (calc/100)* 18
    print("R$ %.2f" %(x+80))
else:
    calc = a - 4500
    x = (calc/100)* 28
    print("R$ %.2f" %(x+80+270))
