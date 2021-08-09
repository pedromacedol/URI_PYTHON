import os
os.system('clear')

import math
import sys

valores = input()

A,B,C = valores.split()

x = ((float(B)**2)-(4*float(A)*float(C)))
 
if x <= 0 or float(A) == 0:
	print("Impossivel calcular")
	sys.exit()	
else:
	x=math.sqrt(x)
	x1=(-(float(B))+x)/(2*float(A))
	x2=(-(float(B))-x)/(2*float(A))

print("R1 = %.5f" % x1)
print("R2 = %.5f" % x2)
