# 2 listas, nombres
nombres = ["Aliénor","Pablo","Yo","Moca"]
nicks = ["Karanceles","Creepdead","AirLinks","Bicha"]

# register this info in a txt file optimal
with open("Nombres_nicks.txt","w",encoding="UTF-8") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\n Nick: {a}\n----------\n") for n,a in zip(nombres,nicks)]
    # created an array(list) with every column of data
#          | | | | | | | | | | | | | | | | | | | | | | | | | | | 
#          V V V V V V V V V V V V V V V V V V V V V V V V V V V 
#  #  #  #  #  #  #  #  #   EQUALS TO  #  #  #  #  #  #  #  #  #  
# for n,a in zip(nombres,nicks):
    # arch.writelines(f"Nombre: {n}\n Nick: {a}\n----------\n")
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  

