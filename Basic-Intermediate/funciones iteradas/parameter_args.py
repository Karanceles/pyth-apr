# forma no óptima de sumar valores
# def suma(lista):
#     num_sumados = 0
#     for numero in lista:
#         num_sumados = num_sumados + numero
#     return num_sumados
#
# resultado = suma([5,3,9,4,7])


# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # 


# forma óptima de sumar valores --> can add more args in sum_tot(x)
def sum_tot(numeros): # 'cause (*numeros) cuts off the calling string
    return sum([*numeros])

resu0 = sum_tot([5,3,9,4,7])
print(f"La suma total del resultado 0 es {resu0}")

# same as above but using * operator as args (used in lists filling)
def suma(*numeros): # * equals a list --> several args (no defined type)
    return sum(numeros)

resu1 = suma(5,3,9,4,7) # el * lo convirtió en 1 solo parámetro
print("La suma del resultado 1 es {resu1}")


# # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # 


## también podemos retornar nombres asignados a numeros (from inside)
def suma(nombre,*numeros):
   sum_num = sum(numeros)
   return f"{nombre}, la suma es: {sum_num}"

res2 = suma("Aliénor",5,3,9,4,7)
print(res2)


