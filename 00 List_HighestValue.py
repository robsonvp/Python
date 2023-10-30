#algoritmo que encontre o maior elemento da lista

lista = [4, 1, 6, 2, 7, 2, 4, 9, 4]
maiorElemento = lista[0]

for elemento in lista:
    if elemento > maiorElemento:
        maiorElemento = elemento
print("O maior elemento é: " + str(maiorElemento))
