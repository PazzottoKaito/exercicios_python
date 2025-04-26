#Programa para somar os números ímpares múltiplos de três entre 1 e 500

soma = 0
multiplos = 0

for numeros in range(1, 500, 2):
    if numeros % 3 == 0:
        multiplos += 1
        soma += numeros

print(f"A soma dos {multiplos} primeiros números ímpares múltiplos "
      f"de três resulta em {soma}.")
