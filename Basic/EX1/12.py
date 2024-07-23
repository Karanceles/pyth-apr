frase = input("Dime una frase y te digo cuanto tardarías en decirla: ")
separar_palabras = frase.split(" ")
cantidad_palabras = len(separar_palabras)
print(f"Dijiste {cantidad_palabras} palabras, demorarías {cantidad_palabras * 0.5} segundos en decirlo")
print(f"Leonora demoraría {cantidad_palabras * 100 // 2*0.7 / 100} segundos en decirlo")

if cantidad_palabras > 120:
    print("Pará flaco, mucho texto")