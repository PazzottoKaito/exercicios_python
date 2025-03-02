#Programa de conversão de medidas de distância

medida = float(input("Digite uma medida, em metros: "))

print("-" * 100)
print(f"A medida digitada é equivalente a: "
      f"\n{medida * 1000:.0f} milímetros (mm)."
      f"\n{medida * 100:.0f} centímetros (cm)."
      f"\n{medida * 10:.0f} decímetros (dm)."
      f"\n{medida:.0f} metros (m)."
      f"\n{medida / 10} decâmetros (dam)."
      f"\n{medida / 100} hectômetros (hm)."
      f"\n{medida / 1000} quilômetros (km).")
