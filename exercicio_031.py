#Programa para calcular preço de passagens de carro

quilometros = int(input("Digite quantos quilômetros foram "
                        "percorridos na viagem: "))

print("-" * 100)

if quilometros > 0:
    if quilometros <= 200:
        print(f"O total a ser pago é R${quilometros * 0.50:.2f}."
              f"\nCada quilômetro custou R$0,50.")
    else:
        print(f"O total a ser pago é R${quilometros * 0.45:.2f}."
              f"\nCada quilômetro custou R$0,45.")
else:
    print("Digite uma quilometragem válida.")
