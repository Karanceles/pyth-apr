diccionario = { # Key: dato
    "Nombre": "Aliénor",
    "Apellido": "Villalobos",
    "Songs": 200
}

# recorriendo diccionario con items()
for key in diccionario:
    key
    print(f"la clave es: {key}") # obteniendo claves

# recorriendo diccionario con items() para obtener -> clave y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"Clave: {key}; Valor: {value}") # obteniendo claves


