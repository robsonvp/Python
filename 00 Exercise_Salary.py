codigo = int(input("Insira código do funcionário: "))
numero = int(input("Insira qt de horas trabalhadas: "))

salario = 10*numero
if numero>50:
    excesso = (numero-50)*20
else: 
    excesso = 0 

print("O salário total do funcionário "+str(codigo) +" é de R$"+ str(salario)+ " e as horas extras são R$"+str(excesso))

