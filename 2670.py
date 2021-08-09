a1 = int(input())
a2 = int(input())
a3 = int(input())
calc1 = (a2*2)+(a3*4)
calc2 = (a1*2)+(a3*2)
calc3 = (a1*4)+(a2*2)
if calc1 <= calc2 and calc1 <= calc3:
    print(calc1)
elif calc2 <= calc1 and calc2 <= calc3:
    print(calc2)
else:
    print(calc3)
