#Programa para categorizar atletas de acordo a idade
import datetime

ano = int(input("Digite seu ano de nascimento: "))
hoje = datetime.date.today().year
idade = hoje - ano
categoria = ""

print("-" * 100)

if ano < (hoje - 100) or ano >= hoje:
    print("Digite um ano válido.")
else:
    if idade <= 9:
        categoria = "mirim"
    elif idade <= 14:
        categoria = "infantil"
    elif idade <= 19:
        categoria = "júnior"
    elif idade <= 25:
        categoria = "sênior"
    else:
        categoria = "master"
    print(f"Com {idade} ano(s) de idade, sua classificação é: "
          f"{categoria.capitalize()}.")
