# creando f(x) que devuelva numeros primos (entre 0 y x num)

# usar una expresión de bucle anidado (solo a nivel de funcionamiento)
def num_primo(num): # recorre para el término num
    # verifying bucle for divisible numbers
    for i in range(2,num): # n 'cause can't divide by itself
        # if the number is multiple of one another
        if num%i==0: return False # return F, isn't prime
    return True # if not, is a prime number

# def rango de num para recorrer
def primos_hasta(num):
    # create a void list
    primos = []
    # bucle for a defined range + the last number requested
    for i in range(3,num+1): # -> desde 2 a num
        # calling for the function (num_primo) already defined
        result = num_primo(i)
        # return only True values and piles them at the bottom
        if result == True: primos.append(i)
    return primos
        
result = primos_hasta(21)
print(result)


