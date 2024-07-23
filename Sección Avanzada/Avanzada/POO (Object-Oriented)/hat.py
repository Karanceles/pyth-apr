import random

# way to encapsulate chunks of data into several classes, differentiating each one among themeselves
class Hat: # mantains order in longer lines of code
    covens = ["Abomination", "Potions", "Bard", "Beast Keeping", "Construction", "Healing", "Illusion", "Oracle", "Plant", "Every", "Any"]
    
    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.covens), "Coven")

Hat.sort("Luz")