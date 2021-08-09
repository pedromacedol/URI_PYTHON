P = input()
a = P.split()

A = int(a[0])
B = int(a[1])
C = int(a[2])

if A > B  and A > C:
 print("%d eh o maior" %A)
elif B > A and B > C:
 print("%d eh o maior" %B)
else :
 print("%d eh o maior" %C)