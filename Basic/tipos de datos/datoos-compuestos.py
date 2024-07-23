
#crear lista (se puede modificar)
lista = ["Leonora", "Yomisma", "Pythons", True, 1.7]

#crear una tupla no se puede modificar
tupla = ("Leonora", "Yomisma", "Pythons", True, 1.7)

#valido
lista[3] = "Maquinola"
#esto no
#tupla[3] = ["Maquinola"]


# conjunto (set) [no se puede acceder; borra lo repetido]
conjunto = {"Leonora", "Yomisma", "Pythons", True, 1.7}
#esto no
#print(conjunto[3])
#esto si
#print(conjunto)

diccionario = { ##decimos como queremos definirlo
               ## la lista lo hace solo 0 , 1 , 2 , 3
    'Nombre' : "Leonora" ,
    'Yo' : "Yo misma" ,
    'Programa' : "Pythons" ,
    'te_gusta' : True ,
    'altura' : 1.7 ,
    'duplicado' : "Leonora"
} ## numero de comas igual a numero datos - 1

print(diccionario['altura'])
print(lista[3])


