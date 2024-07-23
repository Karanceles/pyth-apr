import Packages.saludar_panas # Packages.Subpackage => para el subpaquete (mientras tenga archivo __init__.py)

print(Packages.saludar_panas.saludo_panas("Aliénor")) ## sigue siendo módulo, pero un paquete no deja de ser un módulo
# Paquetes + modulo + función + input(en este caso es {name})