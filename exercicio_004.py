#Programa para mostrar informações de uma variável

texto = str(input("Digite algo: "))

print("-" * 100)

print(f"O tipo primitivo desse dado é: {type(texto)}.")
print(f"O dado é um espaço vazio: {texto.isspace()}.")

print("-" * 100)

print(f"O dado é apenas alfabético: {texto.isalpha()}.")
print(f"O dado é apenas numérico: {texto.isnumeric()}.")
print(f"O dado é alfanumérico: {texto.isalnum()}.")

print("-" * 100)

print(f"O dado está em letras minúsculas: {texto.islower()}.")
print(f"O dado está em letras maiúsculas: {texto.isupper()}.")
print(f"O dado está capitalizado: {texto.istitle()}.")
