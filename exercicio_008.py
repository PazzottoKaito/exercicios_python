#Programa de conversão de medidas de distância

medida = float(input("Digite uma medida, em metros: "))

print("-" * 100)

print(f"A medida digitada é equivalente a: "
      f"\n{medida * 1000:.2f} milímetros (mm)."
      f"\n{medida * 100:.2f} centímetros (cm)."
      f"\n{medida * 10:.2f} decímetros (dm)."
      f"\n{medida} metros (m)."
      f"\n{medida / 10} decâmetros (dam)."
      f"\n{medida / 100} hectômetros (hm)."
      f"\n{medida / 1000} quilômetros (km).")
