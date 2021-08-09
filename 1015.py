A = input()
B = input()
a = A.split()
b = B.split()
x1 = float(a[0])
y1 = float(a[1])
x2 = float(b[0])
y2 = float(b[1])

Dis = (((x2-x1)**2)+((y2-y1)**2))**0.5
print("%.4f" %Dis)