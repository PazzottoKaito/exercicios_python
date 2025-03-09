#Programa para aumento de salário com condições

salario = float(input("Digite o valor do salário: R$"))
aumento = 0

print("-" * 100)

if 0 < salario <= 1250:
    aumento = 0.15 * salario
    print(f"Com 15% de aumento, o novo valor do salário é de "
          f"R${salario + aumento:.2f}.")
elif salario > 1250:
    aumento = 0.10 * salario
    print(f"Com 10% de aumento, o novo valor do salário é de "
          f"R${salario + aumento:.2f}.")
else:
    print("Digite um valor de salário válido.")
