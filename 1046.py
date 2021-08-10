x = input().split()
HI,HF = int(x[0]), int(x[1])
if HI > HF:
    calc = (24-HI)+HF
    print("O JOGO DUROU",calc,"HORA(S)")
elif HI == HF:
    print("O JOGO DUROU 24 HORA(S)")
else:
    calc = HF - HI
    print("O JOGO DUROU",calc,"HORA(S)")
