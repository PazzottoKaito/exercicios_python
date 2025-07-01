#Programa para cálculo de IMC

altura = int(input("Digite sua altura, em centímetros: ")) / 100
peso = int(input("Digite seu peso, em quilogramas: "))

print("-" * 100)

if altura <= 0 or peso <= 0:
    print("Digite valores válidos.")
else:
    formula = peso / (altura ** 2)
    if formula <= 18.5:
        avaliacao = "abaixo do peso"
    elif formula < 25:
        avaliacao = "peso ideal"
    elif formula < 30:
        avaliacao = "sobrepeso"
    elif formula < 40:
        avaliacao = "obesidade"
    else:
        avaliacao = "obesidade mórbida"
    print(f"Seu IMC é de {formula:.2f}, com avaliação de: "
          f"{avaliacao.capitalize()}.")
