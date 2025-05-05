#Programa para ver se um número é par ou ímpar

numero = int(input("Digite um número: "))

print("-" * 50)

if numero % 2 != 0:
    print(f"O número {numero} é ímpar!!")
else:
    print(f"O número {numero} é par!!")
