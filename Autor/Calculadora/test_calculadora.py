from calculadora import cuadrado

def main():
    test_cuadrado()

def test_cuadrado():
    assert cuadrado(2) == 4 ## AssertionError when not fullfiling that boundary
    assert cuadrado(3) == 9
    assert cuadrado(0) == 0
    assert cuadrado(-3) == 9
    assert cuadrado(-2) == 4

if __name__ == "__main__":
    main()