#Programa para calcular litragem de tinta necessária

altura = float(input("Digite a altura da parede, em metros: "))
largura = float(input("Digite a largura da parede, em metros: "))
area = altura * largura

print("-" * 100)
print(f"A parede escolhida possui uma área de {area:.2f}m²."
      f"\nÉ recomendado utilizar {area / 2:.2f} litros de tinta "
      f"para pinta-la.")
