# optimal way to open and close a file // less errors
with open("Intermediate-Advanced\\Archivos\\muchotexto.txt","r", encoding="UTF-8") as archivo:
    # read file
    contenido = archivo.read()
    #showing content
    print(contenido) # we can read it (archivo.read()) or use it ("Hola")
