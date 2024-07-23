# creando un conjunto con set
conjunto = set(["Dato1"]) # no se puede ingresar list/dict en un set
# si se puede poner tupla en set -> ("dato_tupla", "dato_tupla2")

# metiendo un conjunto en otro conjunto
conjunto1 = frozenset(["dato1", "dato2"]) # sin frozenset == error
conjunto2 = {conjunto1, "dato3"}
# el conjunto1 se congela y se vuelve inmutable, permitiendo meter otro conjunto
print(conjunto2)


# teo de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# verificacióon subset
resultado = conjunto2.issubset(conjunto1) # X. is a sub set of (Y) ? -> True/False
# issubset se comporta como verificación --> resultado = conjunto1 <= conjunto2

# verificación superset
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 >= conjunto2

# verificar si hay algún elemento común entre conjuntos
resultado = conjunto2.isdisjoint(conjunto1) # basta 1 solo elemento coincidir -> True


print(resultado)