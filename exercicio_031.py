#Programa para calcular preço de passagens de carro

quilometros = int(input("Digite quantos quilômetros foram "
                        "percorridos na viagem: "))
taxa = 0

print("-" * 100)

if 0 < quilometros <= 200:
    taxa = 0.50
elif quilometros > 200:
    taxa = 0.45
else:
    print("Digite uma quilometragem válida.")

print(f"O total a ser pago por essa viagem é R${quilometros * taxa:.2f}.")
