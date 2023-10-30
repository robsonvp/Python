n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira outro número inteiro: "))
n3 = int(input("Insira outro número inteiro: "))

produto = (n1*2)*(n2/2)
print("A) O produto do dobro do primeiro número com a metade do segundo número é "+ str(produto))
soma = (n1*3)+n2
print("B) A soma do triplo do primeiro número com o segundo número é: "+ str(soma))

maior = n1
if n2>=maior:
    maior=n2
if n3>=maior:
    maior=n3
print("C.1) O maior número é " + str(maior))

menor = n1
if n2<=menor:
    menor=n2
if n3<=menor:
    menor=n3
print("C.2) O menor número é " + str(menor))