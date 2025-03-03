#Programa para sortear ordem de apresentação de alunos
import random

aluno_a = str(input("Digite o nome do primeiro aluno: "))
aluno_b = str(input("Digite o nome do segundo aluno: "))
aluno_c = str(input("Digite o nome do terceiro aluno: "))
aluno_d = str(input("Digite o nome do quarto aluno: "))
lista = [aluno_a, aluno_b, aluno_c, aluno_d]
random.shuffle(lista)

print("-" * 100)
print(f"A ordem de apresentação será a seguinte: "
      f"\n{lista}.")
