lista = []

while True:
    mercado = input("Digite itens para comprar no supermercado: ")
    if mercado == "sair":
        break
    lista.append(mercado)
print(lista)
