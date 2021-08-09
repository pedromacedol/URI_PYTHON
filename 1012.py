P = input()
a = P.split()
A = float(a[0])
B = float(a[1])
C = float(a[2])
Tri = (A*C)/2
Cir = 3.14159*(C**2)
Tra = ((A+B)*C)/2
Qua = B**2
Ret = A*B
print("TRIANGULO: %.3f" %Tri)
print("CIRCULO: %.3f" %Cir)
print("TRAPEZIO: %.3f" %Tra)
print("QUADRADO: %.3f" %Qua)
print("RETANGULO: %.3f" % Ret)