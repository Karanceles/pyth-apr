diccionario = {
    "nombre" : 'Aliénor' ,
    "apellido" : 'Villalobos' ,
    "songs" : 200
    
}

## obtener un elemento con get()
# claves = diccionario.get("songs") # ---> diccionario["x"] crea una excepción
## .get("x") no crea el error, solo no esta definido --> el programa continua

## devuelve un objeto dict_item
claves = diccionario.keys()

valor_dkjf = diccionario.get("dkjf")
print("El mambo sigue")

## elimina todo parametro del diccionario
# diccionario.clear() # dict limpio

# eliminando solo un elemento
diccionario.pop("songs")

dic_iterar = diccionario.items() # recorre los elementos



print(dic_iterar)





