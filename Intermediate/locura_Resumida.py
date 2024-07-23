# crear una serie de num primos independiente de todo

# lambda num funcion "flotante" no necesariamente definida que callea una lista
# crea la lista que filtra True y False booleanamente
# Función momentánea x que callea un booleano True y False para el rango (2,num) que llamamos con primo_hasta(num)
# verifica un n° y sus multiplos de un número de la serie
# (2, raíz del n° aprox al entero + 1) -> solo considera un par de numeros como rango de lambda calleado por el párametro x
# Retorna solo los valores True de la función lambda x, que a la vez está calleada por lambda hasta parametro num

primo_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), range(2, num)))
print(primo_hasta(15))



