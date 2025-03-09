#Programa para ver qual o maior e o menor número

numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))
numero_c = int(input("Digite o terceiro número: "))
lista = [numero_a, numero_b, numero_c]

print("-" * 100)
print(f"O menor número digitado é {min(lista)}."
      f"\nO maior número digitado é {max(lista)}.")
