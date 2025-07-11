#Programa para classificar pesos de um grupo de pessoas

pesos = []

for contador in range(1, 6):
    pesos.append(float(input(f"Insira o peso da {contador}º pessoa: ")))

print("-" * 100)

print(f"O maior peso identificado foi {max(pesos)} Kg."
      f"\nO menor peso identificado foi {min(pesos)} Kg.")
