X = input().split()
C = int(X[0])
Q = int(X[1])

if C == 1:
    print("Total: R$ %.2f" %(4.00 * Q))
if C == 2:
    print("Total: R$ %.2f" %(4.50 * Q))
if C == 3:
    print("Total: R$ %.2f" %(5.00 * Q))
if C == 4:
    print("Total: R$ %.2f" %(2.00 * Q))
if C == 5:
    print("Total: R$ %.2f" %(1.50 * Q))
