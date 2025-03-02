# Programa de conversão de moedas

reais = float(input("Digite quantos reais você possui: R$"))

print("-" * 100)
print(f"Em 02/03/2025, esse valor equivale aproximadamente a: "
      f"\n${reais / 5.88:.2f} - Dólares americanos (USD)."
      f"\n£{reais / 7.41:.2f} - Libras esterlinas (GBP)."
      f"\n€{reais / 6.13:.2f} - Euros (EUR)."
      f"\n¥{reais / 0.81:.2f} - Yuans chineses (CNY)."
      f"\n¥{reais / 0.04:.2f} - Yenes japoneses (JPY).")
