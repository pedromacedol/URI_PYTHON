N = int(input())
print(N)

#CEDULAS DE 100
n100 = N/100
r100 = (N%100) 
print("%d nota(s) de R$ 100,00" %n100)

#CEDULAS DE 50
n50 = r100/50
r50 = (r100%50)
print("%d nota(s) de R$ 50,00" %n50)

#CEDULAS DE 20
n20 = r50/20
r20 = (r50%20)
print("%d nota(s) de R$ 20,00" %n20)

#CEDULAS DE 20
n10 = r20/10
r10 = (r20%10)
print("%d nota(s) de R$ 10,00" %n10)

#CEDULAS DE 5
n5 = r10/5
r5 = (r10%5)
print("%d nota(s) de R$ 5,00" %n5)

#CEDULAS DE 2
n2 = r5/2
r2 = (r5%2)
print("%d nota(s) de R$ 2,00" %n2)

#CEDULAS DE 1
n1 = r2/1
r1 = (r2%1)
print("%d nota(s) de R$ 1,00" %n1)
