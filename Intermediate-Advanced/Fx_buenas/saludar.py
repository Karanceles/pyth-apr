# Cuando se callea el modulo, trabajamos con namespace
import modulo_saludar as mod_x # => namespace (nombre asignado aquí)
# funciona como método y se comporta como objeto (se le puede hacer append, sort, etc)
# se puede renamear con as ==> tanto módulo como f(x)

from modulo_saludar import saludo_panas
# para importar más de 1 f(x) ==> saludo_panas,saludar
# para importar todo ==> * // puede ser pesado y lento innecesariamente

extraños = mod_x.saludar("Extraño")
compas = mod_x.saludo_panas("Aliénor") # limitación de definición
# en modulo_saludar.py puedo acceder directamente a la función
# Aqui debo definir módulo, la acción (saludar) y "Aliénor" como {name}

# al ejecutar crea un folder pycache (caché del programa)
print(extraños)
print(compas)

# para ver propiedades y métodos del namespace
# print(dir(mod_x))

# accedemos al nombre del modulo que se ejecuta
# print(mod_x.__name__) ==> modulo llamado
# print(__name__) ==> este modulo



