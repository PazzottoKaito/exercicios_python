#Programa para realizar descontos em produtos

valor = float(input("Digite o valor do produto: R$"))
desconto = valor * 0.05

print("-" * 100)
print(f"Com 5% de desconto, o novo valor do produto é de "
      f"R${valor - desconto:.2f}.")
