# creando lista con list()
# lista = list("aliénor","yo",1.7) ---> list takes the list as a parameter
lista = list(["aliénor","yo",1.7]) # ---> list as a list

# devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# agregando un elemento a la lista
# add_append = lista.append("Trans Lesbiana") ---> redundant
lista.append("Trans Lesbiana") # direct to the list

# agrega elemento a la lista ---> CON UN INDICE ESPECIFICO
lista.insert(0, "Moshi moshi")

# agrega varios elementos
lista.extend([False,2022]) # we need to give him a list instead a parameter

# elimina elemento con indice
lista.pop(0) # puede eliminar con -1 el último

# remove an element (we search the element by his value)
lista.remove(2022)

# clear elimina todo en la lista
lista.clear()

lista.extend([2030,True,False,False,43,1])

# ordena SOLO números, True y False
lista.sort() # False first, then True, then numbers
# lista.sort(reverse=True) == lista.reverse() ---> invierte la cosa esta
# ----> tuplas y sets(conjunto) son inmutables, no así las listas

# verifica si un elemento INTEGER se encuentra
found_elem = lista.index(1) # print(found_elem)

print(lista))


