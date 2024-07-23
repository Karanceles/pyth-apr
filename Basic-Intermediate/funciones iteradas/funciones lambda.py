numeros = [1,2,3,4,5,6,7,8,9]

multiplicar_dos = lambda x : x*2 # crear una f(x) anónima sin nombre

# crear f(x) que diga par o no
def es_par(num):
    if (num%2==0):
        return True

# usando filter con una f(x) común => los va a agrupar
num_par = filter(es_par,numeros)

# crear lo mismo que antes pero con LAMBDA

numero_par = filter(lambda numero:numero%2 == 0,numeros) # : calls

print(list(num_par))