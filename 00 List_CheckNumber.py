#faça um algoritmo que verifica se um elemento existe na lista. o usuario deve informar ql o numero 
# ele deseja verificar se existe na lista

lista = [4,1,6,2,7,2,4,9,4]
numero = int(input("Inserir numero: "))
achou = False

for elemento in lista:
    if(numero == elemento):
        achou = True
if achou:
    print("O elemento existe na lista")
else: print("O elemento nao existe")
