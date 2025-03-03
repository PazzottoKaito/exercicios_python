#Programa para conversão de temperaturas

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("-" * 100)
print(f"{celsius:.2f}° Celsius equivalem a {kelvin:.2f} Kelvins e "
      f"{fahrenheit:.2f}° Fahrenheit.")
