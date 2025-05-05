#Programa para ver qual o maior e o menor número

numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))
numero_c = int(input("Digite o terceiro número: "))
lista = [numero_a, numero_b, numero_c]

print("-" * 100)

if min(lista) == max(lista):
      print(f"O menor e o maior número digitado são o mesmo, "
            f"sendo {min(lista)}.")
else:
      print(f"O menor número digitado é {min(lista)}."
            f"\nO maior número digitado é {max(lista)}.")
