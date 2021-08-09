X = input().split()
P1 = int(X[0])
C1 = int(X[1])
P2 = int(X[2])
C2 = int(X[3])

if (P1 * C1) == (P2 * C2):
    print("0")
elif (P1 * C1) > (P2 * C2):
    print("-1")
else:
    print("1")
