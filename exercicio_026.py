#Programa para analisar frases

frase = str(input("Digite uma frase: ")).strip().lower()

print("-" * 100)
print(f"A frase digitada possui {frase.count("a")} letras 'A'."
      f"\nA primeira letra 'A' está na posição {frase.find("a") + 1}."
      f"\nA última letra 'A' está na posição {frase.rfind("a") + 1}.")
