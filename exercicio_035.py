#Programa para verificar a montagem de um triângulo

lado_a = int(input("Digite a primeira medida: "))
lado_b = int(input("Digite a segunda medida: "))
lado_c = int(input("Digite a terceira medida: "))

print("-" * 100)

if (lado_a + lado_b > lado_c and
        lado_c + lado_a > lado_b and
        lado_b + lado_c > lado_a):
    print(f"Com essas medidas, é possível montar um triângulo.")
else:
    print(f"Com essas medidas, não é possível montar um triângulo.")
