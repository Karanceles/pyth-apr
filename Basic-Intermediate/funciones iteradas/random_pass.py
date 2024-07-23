# # # # # # # # # # # # # # # # # # # # # # # # 

# crear una función que nos retorne valores // sin que se vea en pantalla
def crea_pass_random(num): # para uso seguro
    chars = "defghijklm" # 10 characters as 0~9 digits
    num_int = str(num) # transformado a str (recorre el valor por el 1er digito)
    num = int(num_int[0]) # se queda con el primer dígito // valor del índice
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña # == print(contraseña)-> asi no se ve en screen
# el return nos devuelve el dato -> para usuar fuera de la función
# podemos retornar tuplas tmbn -> return contraseña,num -> con o sin ()

password = crea_pass_random(1)
frase = f"Tu contraseña nueva es: {password}"
print(frase)

