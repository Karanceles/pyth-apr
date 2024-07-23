cadena1 = "Je,Suis,Aliénor" # "Je Suis Aliénor"
cadena2 = "Sejan Bemvindos"

# resultado = dir(cadena1) CORRECTO (dir esta como función)
# INCORRECTO (upper es método) ----->
# resultado = upper(cadena1)
mayus_ = cadena1.upper() ##   MAYUS
minus_ = cadena1.lower() ##   minus
letra_1 = cadena1.capitalize() ## Primera Letra

#buscamos una cadena en otra cadena
busca_find = cadena1.find("A") ## devuelve (-1) si no está
busca_index = cadena1.index("J") ## si no hay coincidencia, tira excepción
## método == función ---> True; método es función referida a un objeto
## función == metodo --> False

# si es numérico, devolvemos true // caso contrario, false
es_num = cadena1.isnumeric()
es_alfanum = cadena1.isalpha() # space == special character

# cuenta las coincidencias // cuenta el largo (cant caracteres)
cont_veces = cadena1.count("s")
cont_largo = len(cadena1) # len es función, no método

# verifica si empieza/termina con determinado caracter
first_check = cadena1.startswith("H")
ends_check = cadena1.endswith("r")

# chains enchained (reemplaza un trozo de cadena por otra)
new_chain = cadena1.replace(","," ") # lista con coma == space
new_chain2 = new_chain.capitalize()
newchain3 = new_chain2.replace("aliénor", "Leonora")

# separa cadenas con la cadena que pasemos
split_chain = cadena1.split(",") # returns a matrix  split_chain[x]
# x is a vector from that matrix

print(split_chain[2])





