lista =["FELIPE", "ANA", "MARIA", "PENHA", "JOANA"]
listaAvaliacao = [0,1,2,3,4,5,6,7,8,9,10]
cozinheiro  = []
nota1 = []
nota2 = []
nota3 = []
nota10 = 0
achou = False
sair = "S"


while (sair == "S"):
    cozinheiro.append(input("Digite o nome do cozinheiro: "))
    nota1.append(int(input("Digite a primeira nota do cozinheiro: ")))
    nota2.append(int(input("Digite a segunda nota do cozinheiro: ")))
    nota3.append(int(input("Digite a terceira nota do cozinheiro: ")))
    sair = input("Digite S para continuar ou N para sair: ").upper()


for elemento in nota1:
    if(elemento == 10):
        achou = True
        if achou == True:
            nota10 = nota10 + 1

for elemento in nota2:
    if(elemento == 10):
        achou = True
        if achou == True:
            nota10 = nota10 + 1

for elemento in nota3:
    if(elemento == 10):
        achou = True
        if achou == True:
            nota10 = nota10 + 1

print("Numero de cozinheiros com nota 10: " + str(nota10))
