#Programa para identificar números primos

numero = int(input("Digite um número que seja maior que 1: "))
divisores = []

print("-" * 100)

if numero <= 1:
    print("Insira um número válido.")
else:
    for contador in range(1, numero + 1):
        if numero % contador == 0:
            divisores.append(contador)
    print(f"Este número possui {len(divisores)} divisores, sendo eles: "
          f"{divisores}.")
    if len(divisores) > 2:
        print(f"Ou seja, o número {numero} não é um número primo!!")
    else:
        print(f"Ou seja, o número {numero} é um número primo!!")
