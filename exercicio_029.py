#Programa de radar de velocidade

velocidade = int(input("Digite a velocidade do veículo, em km/h: "))

print("-" * 150)

if velocidade > 0:
    if velocidade <= 80:
        print("Fique atento ao limite de velocidade e boa viagem!!")
    else:
        multa = (velocidade - 80) * 7
        print(f"O veículo foi multado em R${multa:.2f}, pois estava "
              f"{velocidade - 80}km/h acima do permitido.")
else:
    print("Digite uma velocidade válida.")
