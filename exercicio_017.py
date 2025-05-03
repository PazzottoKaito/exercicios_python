#Programa para calcular o valor da hipotenusa
import math

cateto_adjacente = float(input("Digite o valor do cateto adjacente "
                               "em centímetros: "))
cateto_oposto = float(input("Digite o valor do cateto oposto em "
                            "centímetros: "))
hipotenusa = math.hypot(cateto_adjacente,
                        cateto_oposto)

print("-" * 150)

print(f"A hipotenusa deste triângulo retângulo equivale a "
      f"{hipotenusa:.2f} centímetros.")
