#Programa para aprovação de alunos

nota_a = float(input("Digite a nota do primeiro bimestre: "))
nota_b = float(input("Digite a nota do segundo bimestre: "))
nota_c = float(input("Digite a nota do terceiro bimestre: "))
nota_d = float(input("Digite a nota do quarto bimestre: "))
media = (nota_a + nota_b + nota_c + nota_d) / 4

print("-" * 100)

if (nota_a < 0 or nota_a > 10 or nota_b < 0 or nota_b > 10 or
        nota_c < 0 or nota_c > 10 or nota_d < 0 or nota_d > 10):
    print("Digite apenas notas válidas, entre os números 0 e 10.")
else:
    if media < 5:
        print(f"Com média {media:.2f}, o estudante está reprovado.")
    elif media < 7:
        print(f"Com média {media:.2f}, o estudante está de recuperação.")
    else:
        print(f"Com média {media:.2f}, o estudante está aprovado.")
