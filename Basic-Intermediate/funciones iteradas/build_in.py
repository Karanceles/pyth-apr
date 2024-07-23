numeros = [4,8,31,0,-2,49] # funca siendo tupla, set, lista, etc

# encontrando el numero mayor de una lista (de un iterable)
num_mas = max(numeros) # print(num_mas)

# encontrando el numero menor de una lista (de un iterable)
num_menos = min(numeros) # print(num_menos)

# FORMA CORRECTA // redondeando decimales -> round(y.x)
numero = round(12.345679, 3) # y == float; x = mantiene x dígitos
# print(numero)

# retorna False -> 0, vacío, None, False
# retorna True -> valor, no vacíos, cadena, True
dato_bool = [2,1]
res_bool = bool(dato_bool) # print(res_bool)

# retorna True = todos los valores son verdad (comprueba todo el iterable)
dato_all = ([23,77,1], "true", 33)
res_all = all(dato_all) # print(res_all)

# suma total valores de un iterable -> DEBEN ser número
suma_tot = sum(numeros) # de no ser numero, arroja excepción
print(suma_tot)