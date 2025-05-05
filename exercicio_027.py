#Programa para achar o nome e o último sobrenome

nome_completo = str(input("Digite seu nome completo: ")).strip()

print("-" * 100)

print(f"Seu primeiro nome é {nome_completo[0:nome_completo.
      find(' ')].title()}."
      f"\nSeu último sobrenome é {nome_completo[nome_completo.
      rfind(' ') + 1:].title()}.")
