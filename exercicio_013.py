#Programa de reajuste salarial

salario = float(input("Digite o valor do salário: R$"))
aumento = salario * 0.15

print("-" * 100)
print(f"Com 15% de aumento, o novo valor do salário é de "
      f"R${salario + aumento:.2f}.")
