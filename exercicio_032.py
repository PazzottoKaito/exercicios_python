#Programa para saber se um ano é bissexto ou não

ano = int(input("Digite um ano: "))

print("-" * 100)

if ano > 0:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano de {ano} é bissexto!!")
    else:
        print(f"O ano de {ano} não é bissexto!!")
else:
    print("Digite um ano válido.")
