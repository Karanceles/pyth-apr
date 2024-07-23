class ExcepcionPropia(Exception): # hereda la clase y características del padre
    def __init__(self,err): # self is given always, not caring 'bout the class type
        print(f"Impresionante, comiste el error: {err}")

# # raising my own exception
# raise ExcepcionPropia("Klkdjf, que aweonao se equivocó")

# handling it
try: # the mere fact of raising an error, will pop up in the code
    # to raise an error of any kind (ValueError/ZeroDivisionError)
    raise ExcepcionPropia("Klkdjf, que aweonao se equivocó")
except:
    print("PEEEEEEEEEEEEEEEEEEEEEEENNNNNNNNCCCCCCCAAAAAAAA")