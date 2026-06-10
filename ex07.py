ip = int(input("Insira o primeiro octeto do endereço IP: "))

if ip <= 126:
    print("Classe A!")

elif ip >= 127 and ip <= 191:
    print("Classe B!")

elif ip >= 192 and ip <= 223:
    print("Classe C!")

else:
    print("Valor inválido.")
