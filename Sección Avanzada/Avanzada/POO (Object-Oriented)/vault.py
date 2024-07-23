class Vault:
    def __init__(self, luca=0, quina=0, gamba=0):
        self.luca = luca
        self.quina = quina
        self.gamba = gamba

    def __str__(self):
        return f"{self.luca} lucas, {self.quina} quinas, {self.gamba} gambas"
    
    def __add__(self, other):
        luca = self.luca + other.luca
        quina = self.quina + other.quina
        gamba = self.gamba + other.gamba
        return Vault(luca, quina, gamba)

nora = Vault(80, 5, 10)
print(nora)

pablo = Vault(20, 10, 100)
print(pablo)

total = nora + pablo # overloading operator
print(total)