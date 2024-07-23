## todo es enrutamiento + encoding UTF8 para tildes, acentos, etc.
## Alt+Shift cambia idioma teclado
archivo = open("Intermediate-Advanced\\Archivos\\trata.txt",encoding="UTF-8")

## leer archivo completo
# print(archivo.read())

## si queremos leer un archivo actualizado, hay que cerrarlo y volver a abrirlo
## por seguridad no se lee dos veces al mismo tiempo

## lectura linea por linea (have to be used with consciousness)
## readlines() ==> convert lines as an array with all lines
## readline() ==> reads a certain quantity of characters // but can overload RAM
linea = archivo.readline()

# cerrar el archivo
archivo.close

print(linea)