#Programa para calcular média aritmética de notas escolares

nota_a = float(input("Digite a primeira nota: "))
nota_b = float(input("Digite a segunda nota: "))

print("-" * 100)

print(f"Com as notas {nota_a:.2f} e {nota_b:.2f}, a média final é "
      f"equivalente a {(nota_a + nota_b) / 2:.2f}.")
