#Programa para mostrar os números pares em um intervalo específico

inicio = int(input("Digite o primeiro número do intervalo crescente: "))
fim = int(input("Digite o último número do intervalo crescente: "))
contador = 0

print("-" * 150)

if inicio > fim:
    print("Insira um número final maior que o número inicial.")
else:
    print(f"Entre {inicio} e {fim}, os números pares encontrados são:")
    for numeros in range(inicio, fim + 1):
        if numeros % 2 == 0:
            if numeros == fim or numeros == fim - 1:
                print(f"{numeros}.")
            else:
                print(f"{numeros}, ", end="")
                contador += 1
                if contador % 20 == 0:
                    print()
