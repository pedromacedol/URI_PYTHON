N = input()
l = N.split()
N1 = float(l[0])
N2 = float(l[1])
N3 = float(l[2])
N4 = float(l[3])
Media = (((N1 * 2)+(N2 * 3)+(N3 * 4)+(N4 * 1))/10)
if Media >= 7.0:
    print("Media: %.1f" %Media)
    print("Aluno aprovado.")

elif Media <= 6.9 and Media >= 5.0:
    h = float(input())
    print("Media: %.1f" %Media)
    print("Aluno em exame.")
    print("Nota do exame: %.1f" %h)
    Media = (((N1 * 2)+(N2 * 3)+(N3 * 4)+(N4 * 1))/10)
    A = ((Media + h)/ 2)
    if A >= 5.0:
        print("Aluno aprovado.")
    elif A <= 4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f" %A)
else:
    print("Media: %.1f" %Media)
    print("Aluno reprovado.")
