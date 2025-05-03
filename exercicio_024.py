#Programa para verificar o nome de uma cidade

cidade = input("Digite o nome de uma cidade: ").strip().lower()

print("-" * 100)

print(f"A cidade digitada começa com a palavra 'Santo' ou 'Santos': "
      f"{cidade[:5] == 'santo' or cidade[:6] == 'santos'}.")
