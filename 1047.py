x = input().split()
x,MI,y,MF = int(x[0]), int(x[1]),int(x[2]), int(x[3])
HI = x*60
HF = y*60
if HI > HF or MI > MF:
    if HI > HF and MI > MF or HI == HF and MI > MF:
        calc = ((1440 + HF + MF)-(HI + MI))//60
        calc2 =((60 + MF)- MI)
        print("O JOGO DUROU %d" %calc,"HORA(S) E",calc2,"MINUTO(S)")
    else:
        calc = ((HF + MF)-(HI + MI))//60
        calc2 = ((60 + MF) - MI)
        print("O JOGO DUROU",calc,"HORA(S) E",calc2,"MINUTO(S)")
elif HF == HI and MF == MI:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU %d" %((HF-HI)/60),"HORA(S) E",(MF-MI),"MINUTO(S)"
