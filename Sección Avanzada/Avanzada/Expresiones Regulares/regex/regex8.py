import re

email = "don_wea73@mail.pucv.cl"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# el '+' busca 1 o más coincidencias // no permite 0
# el '*' en ese caso es flexible

result = re.match(pattern,email)

if result:
    print("Dirección de correo válida")
else:
    print("Correo inválido")