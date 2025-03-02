#Programa para mostrar informações de um número inteiro
import math

numero = int(input("Digite um número: "))

print("-" * 100)
print(f"Seu dobro equivale a {numero * 2}."
      f"\nSeu triplo equivale a {numero * 3}."
      f"\nSua raiz quadrada equivale a {math.sqrt(numero):.2f}.")
