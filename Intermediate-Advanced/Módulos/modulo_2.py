
# importar modulo en la misma carpeta (ruta)
# import Fx_buenas.modulo_saludar
# print(Fx_buenas.modulo_saludar.saludo_panas("Aliénor"))

import sys # built-in
# py le da prioridad a modulos nativos de python antes que los propios

# find sys -> print(sys.builtin_module_names)
# (sys.path) pathing of the folder -> print(sys.path)
sys.path.append('C:\\Users\\lcsvi\\OneDrive\\Escritorio\\pyth apr\\Intermediate-Advanced\\Fx_buenas')

import modulo_saludar as salud

print(salud.saludo_panas("Aliénor")) # (sys.builtin_module_names) -> available modules