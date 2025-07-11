#Programa para analisar idades de um grupo de pessoas
import datetime

hoje = datetime.date.today().year
maiores = 0

for contador in range(1, 8):
    ano = int(input(f"Insira o ano de nascimento da {contador}º "
                    f"pessoa: "))
    idade = hoje - ano
    if idade >= 18:
        maiores += 1

print("-" * 100)

print(f"Há {maiores} pessoas maiores de idade e {7 - maiores} "
      f"pessoas menores de idade.")
