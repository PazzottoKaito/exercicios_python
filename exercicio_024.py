#Programa para analisar o nome de uma cidade

cidade = str(input("Digite o nome de uma cidade: ")).strip().lower()

print("-" * 100)
print(f"A cidade digitada começa com a palavra 'Santo' ou "
      f"'Santos': {cidade[0:5] == 'santo'}.")
