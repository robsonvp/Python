lista = [4, 1, 6, 2, 7, 2, 4, 9, 4]
achou = False
numero = int(input("Digite um numero para ser pesquisado ="))
for elementoVetor in lista:
    if(numero == elementoVetor):
        achou = True
if achou:
    print("O elemento exite na lista")
else:
    print("O elemento não existe na lista")