# falto el profe; alguien va a sustituirlo (pedir nombre y edad)
# función para obtener asistente y profesor entre los compañeros
def get_compas(cant_compas):
    
    # creando list vacía de compañeros
    compañeros = []
    
    # ejecutando data personal // appending (apila) los nombres AL FINAL
    for i in range(cant_compas):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)

    # swap students index en la tupla/lista -> arrange by 2nd index
    compañeros.sort(key=lambda x:x[1])
    
    # X para edad e Y para nombre [x][y]
    asistente = compañeros[-2][0] # el 2ndo mayor es profe
    profesor = compañeros[-1][0] # último (mayor edad) es profe
        
    # retornamos una tupla
    return asistente,profesor

# funcion recuperada entre cierta cantidad de gente
asistente,profesor =  get_compas(5)
# printing final decision
print(f'El profesor es: {profesor} y el asistente es: {asistente}')

