# Programa para a comparação de números inteiros

numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))

print("-" * 100)

if numero_a > numero_b:
    print(f"O número {numero_a} é o maior entre os dois números.")
elif numero_b > numero_a:
    print(f"O número {numero_b} é o maior entre os dois números.")
else:
    print(f"Os números digitados são iguais, ambos sendo {numero_a}.")
