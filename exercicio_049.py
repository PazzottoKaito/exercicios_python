#Programa de tabuada de um número escolhido pelo usuário

numero = int(input("Digite um número inteiro para ser tabulado: "))

print("-" * 100)
print(f"A tabuada de multiplicação de 1 a 10 do número {numero}:")

for numeros in range(1, 11):
    print(f"{numero} X {numeros:02d} = {numero * numeros}")
