a, b= input().split()
A, B= int(a), int(b)
if A%B == 0 or B%A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
