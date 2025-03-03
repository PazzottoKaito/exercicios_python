#Programa para sortear um aluno
import random

aluno_a = str(input("Digite o nome do primeiro aluno: "))
aluno_b = str(input("Digite o nome do segundo aluno: "))
aluno_c = str(input("Digite o nome do terceiro aluno: "))
aluno_d = str(input("Digite o nome do quarto aluno: "))
lista = [aluno_a, aluno_b, aluno_c, aluno_d]

print("-" * 100)
print(f"O aluno sorteado foi o {random.choice(lista)}.")
