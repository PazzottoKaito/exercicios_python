#Programa para adivinhar o número sorteado
import random

numero = int(input("Digite um número de 0 a 5: "))
sorteado = random.randint(0, 5)

print("-" * 100)

if 5>= numero >= 0:
    if numero == sorteado:
        print(f"Eu escolhi o número {sorteado} e você também."
              f"\nParabéns!!")
    else:
        print(f"Eu escolhi o número {sorteado} e você escolheu "
              f"o número {numero}."
              f"\nMais sorte na próxima vez...")
else:
    print("Você deve escolher um número entre 0 e 5.")
