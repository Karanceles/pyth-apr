# FOR - IN (iterantes)


# listas
animales = ["gato","perro","loro","canario","pez"] # funciona igual con tuplas como con listas
numeros = [4,1,8,9] # same a lo de arriba


# range(x,y) itera -> recorre desde X hasta 1 antes de Y
for nume in range(1,3):
    print(nume)


# ZIP junta tuplas de "len(N)" y las recorre
for numero, animal in zip(animales,numeros): # numero y animal solo se recorre en esta línea de código
    print(f"Se puede recorrer la lista 1: {numero}") # se corre la lista 1 y 2 intercaladamente
    print(f"Se puede recorrer la lista 2: {animal}")


# forma NO ÓPTIMA listas == IMPOSIBLE para sets -> error de recorrido
for num in range(len(numeros)): # forma no óptima de recorrer una lista
    print(numeros[num])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# for num in range(len(numeros)):
#    print(numeros[num])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# FORMA CORRECTA
for num in enumerate(numeros): # forma correcta de recorrer una lista
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice} y el valor: {valor}")


# FORMA ELEGANTE Y ÓPTIMA
for i, num in enumerate(numeros): # -> primero el indice y luego el número
    print(f"el índice es {i} y el valor: {num}")


# usando el for/else -> similar a la FORMA CORRECTA, pero no igual
for numero in numeros:
    print(f"ejecutando el último bucle, valor actual: {numero}")
else:
    print("el bucle terminó")


# todo funca igual para tuplas y sets