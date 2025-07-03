#Programa para somar apenas os números pares entre os seis digitados

pares = []
soma = 0

for contador in range(1, 7):
    numero = int(input(f"Digite o {contador}° número: "))
    if numero % 2 == 0:
        pares.append(numero)
        soma += numero

print("-" * 100)

print(f"A soma entre os números pares {sorted(pares)} resulta "
      f"em {soma}.")
