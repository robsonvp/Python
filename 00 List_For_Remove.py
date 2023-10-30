lista =["FELIPE", "ANA", "MARIA", "PENHA", "JOANA"]
listaAvaliacao = [0,1,2,3,4,5,6,7,8,9,10]
cozinheiro  = input("Insira nome do cozinheiro a ser retirado: ").upper()
nota1 = []
nota2 = []
nota3 = []

for elemento in lista:
    if(cozinheiro == elemento):
        lista.remove(elemento)
    if nota1 == True:
        nota1.remove()
    if nota2 == True:
        nota2.remove()
    if nota3 == True:
        nota3.remove()

    
print("A lista atualizada é  " + str(lista) + " e as notas foram removidas.")