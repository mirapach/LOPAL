bolsa = float(input("Qual o valor da bolsa do seu estágio? "))
aumento = bolsa*0.15
maior_igual = bolsa*0.10

if bolsa < 1000:
    print(f"O valor final da sua bolsa é de {bolsa+aumento} reais!")

elif bolsa >= 1000:
    print(f"O valor final da sua bolsa é de {bolsa+maior_igual} reais!")

else:
    print("O valor da sua bolsa de estágio mantém-se o mesmo.")
