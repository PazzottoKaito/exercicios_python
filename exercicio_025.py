#Programa para procurar um sobrenome específico

nome_completo = (str(input("Digite seu nome completo: ")).strip()
                 .lower())

print("-" * 100)
print(f"O seu nome completo possui o nome ou sobrenome 'Silva': "
      f"{'silva' in nome_completo}.")
