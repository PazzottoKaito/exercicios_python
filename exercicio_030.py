#Programa para ver se um número é par ou ímpar

numero = int(input("Digite um número: "))

if numero / 2 % 1:
    print(f"O número {numero} é ímpar!!")
else:
    print(f"O número {numero} é par!!")
