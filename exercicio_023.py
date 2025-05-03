#Programa para separar números inteiros

numero = int(input("Digite um número com quatro algarismos: "))

print("-" * 100)

print(f"O número digitado, {numero}, é composto por:"
      f"\n{numero // 1000 % 10} unidade(s) de milhar."
      f"\n{numero // 100 % 10} centena(s)."
      f"\n{numero // 10 % 10} dezena(s)."
      f"\n{numero % 10} unidade(s).")
