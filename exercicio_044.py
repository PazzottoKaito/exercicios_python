#Programa para pagamento de compras

valor = float(input("Digite o valor total da compra: R$"))

print("-" * 150)

print("Digite [1] para pagar com cheque ou dinheiro."
      "\nDigite [2] para pagar à vista no cartão."
      "\nDigite [3] para pagar em duas vezes no cartão."
      "\nDigite [4] para pagar em três vezes ou mais no cartão.")

print("-" * 150)

opcao = int(input("Digite uma opção: "))

print("-" * 150)

if opcao > 4 or opcao < 1:
    print("Digite uma opção válida.")
else:
    if opcao == 1:
        print(f"Você ganhou 10% de desconto!"
              f"\nO total da compra é de R${(valor * 0.90):.2f}.")
    elif opcao == 2:
        print(f"Você ganhou 5% de desconto!"
              f"\nO total da compra é de R${(valor * 0.95):.2f}.")
    elif opcao == 3:
        print(f"Você parcelou a compra em duas vezes de R${(valor / 2):.2f} "
              f"(sem juros)."
              f"\nO total da compra continua sendo R${valor:.2f}.")
    else:
        parcela = int(input("Digite o número desejado de parcelas: "))
        print("-" * 150)
        print(f"Você parcelou a compra em {parcela} vezes de R$"
              f"{(valor * 1.20) / parcela:.2f} (com juros de 20%)."
              f"\nO total da compra é de R${(valor * 1.20):.2f}.")
