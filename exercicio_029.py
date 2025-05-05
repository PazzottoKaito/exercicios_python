#Programa de radar de velocidade

velocidade = int(input("Digite a velocidade do veículo, em km/h: "))

print("-" * 100)

if velocidade > 0:
    if velocidade <= 80:
        print("Velocidade dentro do limite. Boa viagem e dirija com "
              "segurança!!")
    else:
        multa = (velocidade - 80) * 7
        print(f"O veículo foi multado em R${multa:.2f}."
              f"\nEstava a {velocidade} km/h, ou seja, {velocidade - 80} "
              f"km/h acima do limite permitido.")
else:
    print("Digite uma velocidade válida.")
