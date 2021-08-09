N = int(input())
H = N/3600
RH = (N%3600)
M = RH/60
S = (RH%60)
print("%d:%d:%d" %(H,M,S))
