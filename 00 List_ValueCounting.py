## um algoritmo que verifica quantas vezes o numero aparece na lista
#o usuario deve informar qual o numero

lista = [4, 1, 6, 2, 7, 2, 4, 9, 4, 1]
numero = int(input("Digite um numero para ser pesquisado: "))
vezes = 0

for elementoVetor in lista:
    if(numero == elementoVetor):
        vezes = vezes + 1
print("Num de vezes que apareceu: " + str(vezes))