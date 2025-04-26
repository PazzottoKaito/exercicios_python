#Programa para contagem regressiva da virada do ano
import time
import datetime

for numeros in range(10, 0, -1):
    print(f"{numeros}...", end=" ")
    time.sleep(1)

print("")
print("-" * 100)
print(f"Um feliz Ano Novo de {datetime.datetime.today().year + 1} "
      f"para você e a sua família!!")
