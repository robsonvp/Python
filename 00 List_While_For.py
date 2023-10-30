lista =["FELIPE", "ANA", "MARIA", "PENHA", "JOANA"]
listaAvaliacao = [0,1,2,3,4,5,6,7,8,9,10]
cozinheiro  = []
nota1 = []
nota2 = []
nota3 = []
nota10 = 0
sair = "S"


while (sair == "S"):
    cozinheiro.append(input("Digite o nome do cozinheiro: "))
    nota1.append(int(input("Digite a primeira nota do cozinheiro: ")))
    sair = input("Digite S para continuar ou N para sair: ").upper()
for elemento1 in nota1:
    if(elemento1 == 10):
        nota10 = nota10 + 1
print("Numero de notas 10: " + str(nota10))