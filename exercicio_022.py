#Programa para analisar um nome completo

nome_completo = str(input("Digite seu nome completo: ")).strip()

print("-" * 150)

print(f"O seu nome apenas com letras minúsculas: "
      f"{nome_completo.lower()}."
      f"\nO seu nome apenas com letras maiúsculas: "
      f"{nome_completo.upper()}."
      f"\nO seu nome completo possui {len(nome_completo) - 
                                      nome_completo.count(' ')} letras no total."
      f"\nO seu primeiro nome possui {nome_completo.find(' ')} "
      f"letras no total.")
