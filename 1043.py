a, b, c = input().split()
A, B, C = float(a), float(b), float(c)
if A + B > C and B + C > A and C + A > B:
    print("Perimetro = %.1f" %(A+B+C))
else:
        print("Area = %.1f" % ((A + B) * C / 2))
