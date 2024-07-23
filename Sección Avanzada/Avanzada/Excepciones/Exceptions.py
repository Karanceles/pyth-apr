def sumar_dos():
    # La mejor forma de para manejar el error es meterlo en un bucle
    while True: # aunque no está bien visto, es útil en ciertas ocasiones
        a = input("Número 1:")
        b = input("Número 2:")
        try:
            resultado = int(a) + int(b)
        # si no puede intentar ejecutarlo, lanza excepción    
        except ValueError as v: # access to Exception, the main one (ValueError/ZeroDivisionError)
            print("Te pedí un número, pete")
            # print(f"Error: {type(e).__name__}") --> know type of exception so we add it (ValueError)
            print(f"Error: {type(v)}") # ValueError
        else: # para los casos distintos a la excepción
            break # si logra intentarlo, romperá el bucle
        finally: # executed always // rarely used
            print("Manejo de excepción finalizado")
            
    return resultado

print(sumar_dos())