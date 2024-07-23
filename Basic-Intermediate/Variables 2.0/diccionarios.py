# creando dict con dict()
diccionario = dict(nombre="Aliénor",apellido="Villalobos")
## RECORDAR -> crear DATOS VACÍOS usar la función, no su nomenclatura de signo
## () o {} o [] no -> tuple() o dict{} o list[]

# las listas no pueden ser claves -> usamos frozenset para meter conjuntos
diccionario = {frozenset(["Dalto", "rancio" ]): "kjhfd"}

# creando diccionarios con dict.fromkeys() -> con valores sin asignar/definir
diccionario = dict.fromkeys(["Nombre","Apellido"]) # dict es un tipo de dato // itera el primer elemento
# diccionario = dict.fromkeys("ABCDE","X") -> le asigna X al abecedario
diccionario = dict.fromkeys(["Nombre","Apellido"], "Ni puta idea")


print(diccionario)

