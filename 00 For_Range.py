menorNumero = int(input("Digite o menor numero = "))
maiorNumero = int(input("Digite o maior numero = "))

soma = 0
for valor in range(menorNumero, maiorNumero + 1, 1):
   soma = soma + valor
   
print("soma= " + str(soma))


