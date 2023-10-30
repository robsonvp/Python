##pode pedir achar o PC MAIS BARATO etc
##prova WHILE, FOR, LISTA E PRINCIPALMENTE EXERCICIO ABAIXO


codigo  = []
equipamento = []
valor = []
departamento = []
continuar = "C"
while (continuar == "C"):
    codigo.append(input("Digite o codigo do equipamento = "))
    equipamento.append(input("Digite o nome do equipamento = "))
    valor.append(int(input("Digite o valor do equipamento = ")))
    departamento.append(input("Digite o departamento do equipamento = "))
    continuar = input("Digite C para continuar ou outra tecla para sair.").upper()
print("codigos = " + str(codigo))
print("equipamentos = " + str(equipamento))
print("valor = " + str(valor))
print("departamento = " + str(departamento))
maisCaro = valor[0]
for elemento in valor:
    if(elemento > maisCaro):
        maisCaro = elemento
posicao = valor.index(maisCaro)
print("O produto mais caro = " + str(equipamento[posicao]))