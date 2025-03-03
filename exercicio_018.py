#Programa para calcular seno, cosseno e tangente
import math

angulo = int(input("Digite um ângulo: "))
radiano = math.radians(angulo)

print("-" * 100)
print(f"O seno do ângulo de {angulo}° é {math.sin(radiano):.2f}."
      f"\nO cosseno do ângulo de {angulo}° é {math.cos(radiano):.2f}."
      f"\nA tangente do ângulo de {angulo}° é {math.tan(radiano):.2f}.")
