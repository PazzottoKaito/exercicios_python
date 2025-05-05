#Programa para adivinhar o número sorteado
import random

numero = int(input("Digite um número de 1 a 5: "))
sorteado = random.randint(1, 5)

print("-" * 100)

if 1 <= numero <= 5:
    if numero == sorteado:
        print(f"Eu escolhi o número {sorteado} e você também."
              f"\nParabéns, você adivinhou meu número!!")
    else:
        print(f"Eu escolhi o número {sorteado} e você escolheu "
              f"o número {numero}."
              f"\nMais sorte na próxima vez adivinhando meu número...")
else:
    print("Escolha um número entre 1 e 5.")
