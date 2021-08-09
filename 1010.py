valor1 = input().split(" ")
valor2 = input().split(" ")

cod1, quant1, valor1 = valor1 
cod2, quant2, valor2 = valor2

total = (int(quant1) * float(valor1)) + (int(quant2) * float(valor2))

print("VALOR A PAGAR: R$ %.2f" %total)