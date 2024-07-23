#comparar usuario y contraseña
usuario_base_dato = "Aliénor Villalobos"
contraseña_dada = "Astrosmuertos_1"
#datos escritos
usuario_escrito = "Leonora Villalobos"
contraseña_escrita = "Astrosmuertos_1"

if contraseña_dada == contraseña_escrita and usuario_base_dato == usuario_escrito:
    print("Acceso válido")
else:
    print("Incorrecto, intente de nuevo")
