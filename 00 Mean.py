n1=float(input("Insira nota C1: "))
n2=float(input("insira nota C2: "))
n3=float(input("Insira nota C3: "))
media=(n1+n2+n3/3.0)
if (media>=7.0):
    print("Aprovado, nerd. Nota: "+ str(media))
else:
    print("Reprovado")