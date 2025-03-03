#Programa para calcular aluguel de carros

dias = int(input("Digite o total de dias de aluguel do carro: "))
quilometros = int(input("Digite quantos quilômetros foram "
                        "percorridos com o carro: "))
valor = (dias * 60) + (quilometros * 0.15)

print("-" * 100)
print(f"O valor total a ser pago é de R${valor:.2f}.")
