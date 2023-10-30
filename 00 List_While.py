lista =["FELIPE", "ANA", "MARIA", "PENHA", "JOANA"]
listaAvaliacao = [0,1,2,3,4,5,6,7,8,9,10]
cozinheiro  = []
nota1 = []
nota2 = []
nota3 = []
sair = "S"

while (sair == "S"):
    cozinheiro.append(input("Digite o nome do cozinheiro: ").upper())
    nota1.append(int(input("Digite a primeira nota do cozinheiro: ")))
    nota2.append(int(input("Digite a segunda nota do cozinheiro: ")))
    sair = input("Digite S para continuar ou N para sair: ").upper()

print("Cozinheiro: " + str(cozinheiro))
print("1ª Nota: " + str(nota1))
print("2ª Nota: " + str(nota2))
