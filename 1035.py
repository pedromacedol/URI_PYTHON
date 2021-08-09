a= input()
L = a.split()
A = int(L[0])
B = int(L[1])
C = int(L[2])
D = int(L[3])

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
