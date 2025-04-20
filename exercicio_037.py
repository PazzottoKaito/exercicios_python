#Programa para conversão de bases numéricas

numero = int(input("Digite um número inteiro: "))

print("-" * 100)
print("Digite [1] para converter em binário."
      "\nDigite [2] para converter em octal."
      "\nDigite [3] para converter em hexadecimal.")
print("-" * 100)

opcao = int(input("Digite uma opção: "))
print("-" * 100)

if opcao == 1:
    print(f"O número {numero} em base binária é: {bin(numero)}.")
elif opcao == 2:
    print(f"O número {numero} em base octal é: {oct(numero)}.")
elif opcao == 3:
    print(f"O número {numero} em base hexadecimal é: {hex(numero)}.")
else:
    print("Opção inválida.")
