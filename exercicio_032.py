#Programa para saber se um ano é bissexto ou não

ano = int(input("Digite um ano: "))
resposta = ""

if ano % 4 == 0:
    resposta = "é um ano bissexto"
else:
    resposta = "não é um ano bissexto"

print(f"O ano de {ano} {resposta}!!")
