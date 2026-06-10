tamanho = int(input("Insira o tamanho do arquivo em Megabytes: "))
velocidade = int(input("Insira a velocidade do link de interant em Megabits por segundo: "))
download = tamanho*8
tempo = download/velocidade
print(f"O tempo aproximado do download é de {tempo} segundos.")
