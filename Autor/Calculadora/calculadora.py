def main():
    x = int(input("Qué número quieres elevar? "))
    print("El cuadrado de {x} es:", cuadrado(x))

def cuadrado(n):
    return n ** 2

if __name__ == "__main__":
    main()