#Programa para procurar um sobrenome específico

nome_completo = (input("Digite seu nome completo: ").strip()
                 .lower())

print("-" * 100)

print(f"O seu nome completo contém 'Silva' em alguma parte: "
      f"{'silva' in nome_completo}.")
