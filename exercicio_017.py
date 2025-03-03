#Programa para calcular o valor da hipotenusa
import math

cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
hipotenusa = math.hypot(cateto_adjacente,
                        cateto_oposto)

print("-" * 100)
print(f"A hipotenusa deste triângulo retângulo equivale a "
      f"{hipotenusa:.2f}.")
