with open("Intermediate-Advanced\\Archivos\\texto_nueo.txt","w", encoding="UTF-8") as archivo:
    # overwriting the file
    # archivo.write("kjsdjfld la recontra viste") # 'w' if doesn't find a file, creates one
    
    # adding 2 lines
    archivo.writelines(["Dead\n","Astros\n"]) # use a list for more parameters
    # can add 2 more
    archivo.writelines(["No me digas\n","Te digo"]) # use a list for more parameters