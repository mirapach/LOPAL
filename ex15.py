texto = input("Digite uma frase: ")

vogais = "aeiou"
quantidade = 0

for caractere in texto:
    if caractere in vogais:
        quantidade += 1

print(f"O total de vogais no texto é: {quantidade}")
