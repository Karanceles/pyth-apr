# promedio duración en horas
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

# duración raw
crudo_prom = 5
crudo_dalto = 3.5

# diferencias de duración
dif_con_min = 100 - dalto_curso / otros_cursos_min * 100
dif_con_prom = 100 - dalto_curso / otros_cursos_prom * 100
dif_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
    # se puede recuperar el cien antes y luego devolver el menor numero
    # igual a mates, multiplicación y división primero

# calculando porcentaje de tiempo vacío removido
tiempo_vacio_prom = 100 - otros_cursos_prom * 1000 // crudo_prom / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

# calculando cuantos cursos se pueden ver en tiempo promedio
veces_dalto_vs_max = otros_cursos_max * 100 // dalto_curso / 100
veces_dalto_vs_min = otros_cursos_min * 100 // dalto_curso / 100
veces_dalto_vs_prom = otros_cursos_prom * 100 // dalto_curso / 100

# mostrando diferencias de duracion
print(f"El curso de Dalto dura un {dif_con_min}% menos que el más rápido")
print(f"El curso de Dalto dura un {dif_con_max}% menos que el más lento")
print(f"El curso de Dalto dura un {dif_con_prom}% menos que el promedio")

# cantidad de espacio muerto removido
print(f"El curso de Dalto eliminó un {tiempo_vacio_dalto}% de tiempo vacío")
print(f"Un curso promedio elimina un {dif_con_prom}% de tiempo vacío")

# mostrar diferencias duran 10 horas
print(f"Puedes ver {veces_dalto_vs_min} cursos de dalto en vez de un curso corto")
print(f"Puedes ver {veces_dalto_vs_max} cursos de dalto en vez de un curso largo")
print(f"Puedes ver {veces_dalto_vs_prom} cursos de dalto en vez de un curso promedio")

