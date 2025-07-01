#Programa para jogar pedra, papel e tesoura
import random

print("-" * 100)

print("Digite [1] para jogar pedra."
      "\nDigite [2] para jogar papel."
      "\nDigite [3] para jogar tesoura.")

print("-" * 100)

opcao_jogador = int(input("Digite qual item você quer jogar: "))
itens = ("pedra", "papel", "tesoura")
opcao_maquina = random.randint(1, 3)

print("-" * 100)

if opcao_jogador < 1 or opcao_jogador > 3:
    print("Digite uma opção válida.")
else:
    if opcao_jogador == opcao_maquina:
        resposta = "Deu empate!!"
    elif (opcao_jogador == 1 and opcao_maquina == 3) or \
            (opcao_jogador == 2 and opcao_maquina == 1) or \
            (opcao_jogador == 3 and opcao_maquina == 2):
        resposta = "Você venceu!!"
    else:
        resposta = "Eu venci!!"
    print(f"Você jogou {itens[opcao_jogador - 1]}... "
          f"\nEu joguei {itens[opcao_maquina - 1]}... "
          f"\n{resposta}")
