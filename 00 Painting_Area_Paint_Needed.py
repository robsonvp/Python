import math


mt = float(input('Insira qt m² da area a ser pintada: \n'))
mt = mt * 1.1 #mais 10% de tinta a ser comprada adicionada a área.
litro = 6 #um litro pintam 6m²
lata = 18 #uma lata tem 18 litros
precoLata = 80 #uma lata custa 80 pau
galao = 3.6
precoGalao = 25
litrosUsados = mt/litro
qtGalao = math.ceil(litrosUsados/3.6)
qtLatas = math.ceil(litrosUsados/18)
precoTotal = qtLatas*80
precoTotalGalao = qtGalao*25

qtLataFloor = math.floor(litrosUsados/18)
valorLataFloor = qtLataFloor*80
litrosFaltantes = litrosUsados % 18
qtGalaoFaltante = math.ceil(litrosFaltantes/3.6)
valorGalao = qtGalaoFaltante*25
valorTotal = valorGalao + valorLataFloor


print(f'litros usados para a area {litrosUsados}')

print(f'a) Serão necessárias {qtLatas}. O preço total é R${precoTotal}.') #apenas latas de 18 litros

print(f'b) Serão necessárias {qtGalao}. O preço total é R${precoTotalGalao}.') #apenas galões de 3.6 litros

print(f'c) Serão necessárias {qtLataFloor} de latas e {qtGalaoFaltante} galões. O preço total é R${valorTotal}.')




