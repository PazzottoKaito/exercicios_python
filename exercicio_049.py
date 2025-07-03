#Programa de tabuada de um número específico

numero = int(input("Digite um número inteiro para ser tabulado: "))

print("-" * 100)

print(f"A tabuada de multiplicação do número {numero}")

print("-" * 100)

for numeros in range(1, 11):
    print(f"{numero} X {numeros:02d} = {numero * numeros}")
