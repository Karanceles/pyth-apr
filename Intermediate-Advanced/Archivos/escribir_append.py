with open("Intermediate-Advanced\\Archivos\\texto_nueo.txt","a", encoding="UTF-8") as archivo:
    # adding appended lines
    archivo.writelines(["- Así como así: ","Añado otra línea"])
    # even can be done as a range iteration + \n at start
    archivo.write("\n")
    for i in range(4):
        archivo.write(f"- Así es como añado una línea {i+1}\n")