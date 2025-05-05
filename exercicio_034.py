#Programa para aumento de salário com condições

salario = float(input("Digite o valor do salário: R$"))

print("-" * 150)

if 0 < salario <= 1250:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Com 15% de aumento, o salário aumentou R${aumento:.2f} "
          f"e passou a ser R${novo_salario:.2f}.")
elif salario > 1250:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"Com 10% de aumento, o salário aumentou R${aumento:.2f} "
          f"e passou a ser R${novo_salario:.2f}.")
else:
    print("Digite um valor de salário válido.")
