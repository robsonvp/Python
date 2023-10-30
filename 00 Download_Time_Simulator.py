arquivo = float(input("Qual tamanho do arquivo em MB?\n"))
velocidade = float(input('Qual speed do link da net?\n'))
download = (arquivo/velocidade)/60 #em minutos

print(f'O tempo de download será de {download} minutos')
quit