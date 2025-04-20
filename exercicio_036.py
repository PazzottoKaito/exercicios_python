#Programa para análise de financiamento imobiliário

valor = float(input("Digite o valor do imóvel: R$"))
salario = float(input("Digite o salário mensal do comprador: R$"))
anos = int(input("Digite em quantos anos se pretende quitar o "
                 "financiamento: "))

print("-" * 150)

print(f"Para quitar o financiamento em {anos} anos, é necessária "
          f"uma parcela mensal de R${valor / (anos * 12):.2f}.")

if valor / (anos * 12) > salario * 0.30:
    print("Diante disso, o financiamento foi negado!!")
else:
    print("Diante disso, o financiamento foi aprovado e concedido!!")
