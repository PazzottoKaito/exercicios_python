#Programa de identificação de palíndromos

frase = input("Digite uma frase: ").upper().strip()
palavras = frase.split()
frase_pronta = ''.join(palavras)
frase_invertida = frase_pronta[::-1]

print("-" * 100)

print(f"Frase digitada: {frase_pronta}."
      f"\nFrase invertida : {frase_invertida}.")

print("-" * 100)

if frase_pronta == frase_invertida:
    print("A frase digitada é um palíndromo!!")
else:
    print("A frase digitada não é um palíndromo!!")
