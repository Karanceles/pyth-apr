
frutas = ["manzana", "durazno", "ciruela", "granada", "pera", "naranja", "plátano"]

# evitando que se coma una granada (pq es mia) -> 
for fruta in frutas:
    if fruta == 'granada':
        print(f"La {fruta} es mía")
        continue
    elif fruta == "naranja":
        print(f"{fruta} va a ser lo último que coma")
        break
    else:
        print(f"Me voy a comer una {fruta}")
else:
    print("bucle terminado")

# # # # # # # # # # # # # # # # # # # # # # # # 

cadena = "Hola Nora"
cuenta = [2,5,6,9,11,13,14,17]

# recorrer una cadena de texto
for letra in cadena:
    print(letra)

# FOR en una sola línea de código
nums_dupl = list()
for dig in cuenta:
    nums_dupl.append(dig*2) # duplicó los dígitos de la cuenta
print(nums_dupl)