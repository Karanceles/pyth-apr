# creando una función simple
def saludar(nombre,gender):
    gender = gender.lower() # lower == minus // upper == mayus
    if (gender == "mujer"): # -> nomenclatura "MUJER" == .upper()
        adjetivo = "reina"
    elif (gender == "hombre"): # -> nomenclatura "hombre" == .lower()
        adjetivo = "king"
    else:
        adjetivo = "caballere"

    print(f"Aliénor: {nombre}, como estás mi {adjetivo}?")

# preguntando nombrem, género y ejecutando la función simple
nombre = input("Dime tu nombre ")
gender = input("Ahora tu género ")
saludar(nombre,gender)

# # # # # # # # # # # # # # # # # # # # # # # # 

# crear una función que nos retorne valores // sin que se vea en pantalla
def crea_pass_random(num): # para uso seguro
    chars = ["lkddkjfj"] # characters
    num_int = str(num)
    num = int(num_int[0]) # se queda con el primer dígito
    c1 = num -2
    c2 = num
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num}"
    print(contraseña)

