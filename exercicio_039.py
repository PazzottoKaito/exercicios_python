# Programa de resultado de alistamento militar
import datetime

ano = int(input("Digite seu ano de nascimento: "))
hoje = datetime.date.today().year
idade = hoje - ano

print("-" * 150)

if ano < (hoje - 100):
    print("Digite um ano válido.")
elif idade < 18:
    print(f"Com {idade} anos, faltam ainda {18 - idade} ano(s) para o "
          f"seu alistamento militar obrigatório."
          f"\nVocê deverá se alistar no ano de {ano + 18}.")
elif idade == 18:
    print(f"Com {idade} anos, seu alistamento militar obrigatório é "
          f"neste ano de {hoje}.")
else:
    print(f"Com {idade} anos, já se passaram {idade - 18} ano(s) do "
          f"seu alistamento militar obrigatório."
          f"\nVocê deveria ter se alistado no ano de {ano + 18}.")
