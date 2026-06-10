valor_livro = float(input("Qual foi o valor do livro comprado? "))
desconto = valor_livro*0.1
final = valor_livro-desconto

if valor_livro > 80:
    print(f"O valor total ficou {final} reais!")

else:
    print(f"O valor total ficou {valor_livro} reais!")
