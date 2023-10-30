lista =["FELIPE", "ANA", "MARIA", "PENHA", "JOANA"]
cozinheiro = input("O cozinheiro esta na lista? Insira o nome a ser pesquisado: ").upper()
achou = False

for elemento in lista:
    if(cozinheiro == elemento):
        achou = True
if achou:
    print("SIM")
else: print("NAO")