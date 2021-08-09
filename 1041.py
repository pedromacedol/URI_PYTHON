x, y = input().split()
X = float(x)
Y = float(y)
if X == 0 and Y == 0:
  print("Origem")
elif Y > 0 and X > 0:
  print("Q1")
elif Y > 0 and X < 0:
  print("Q2")
elif Y < 0 and X < 0:
  print("Q3")
elif Y < 0 and X > 0:
  print("Q4")
elif X != 0 and Y == 0:
    print("Eixo X")
else:
    print("Eixo Y")
