IDADE = int(input())

ANO = IDADE/365
RA = (IDADE%365)
print("%d ano(s)" %ANO)

MES = RA/30
RM = (RA%30)
print("%d mes(es)" %MES)

DIA = RM/1
print("%d dia(s)" %DIA)
