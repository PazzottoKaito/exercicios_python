#Programa de progressão aritmética personalizada

inicio = int(input("Digite o primeiro termo da progressão aritmética: "))
razao = int(input("Digite a razão da progressão aritmética: "))

print("-" * 100)

print(f"Os 10 primeiros termos dessa progressão aritmética são: "
      f"\n{inicio}", end=", ")

for contador in range(1, 10):
    resultado = inicio + razao * contador
    if contador < 8:
        print(resultado, end=", ")
    elif contador < 9:
        print(resultado, end=" e ")
    else:
        print(resultado, end=".")
