### creando una función de 3 parámetros
#    def frase(nombre,apellido,adjetivo):
#        return f"Hola {nombre} {apellido}, sos muy {adjetivo}"
#    frase_resultado = frase("Leonora","Villalobos","genia") # X,Y,Z

### forcing and arg => (adjetivo = "Z",nombre = "X",apellido = "Y")
#   print(frase_resultado) # mismos resultados al forzar args en un orden

# same f(x) but with an optional parameter and a default value
def frase(nombre,apellido,adjetivo = "weona"): ## weona es opcional
    return f"Hola {nombre} {apellido}, vo' eri muy {adjetivo}"

frase_resultado = frase("Leonora","Villalobos",adjetivo="genia")
print(frase_resultado) ## adjetivo "genia" le gana al opcional
