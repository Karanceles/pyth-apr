class Student: # by convention // own data type called Student
    def __init__(self, name, coven, palisman): # --> instance method ////// __ = dunder
        # customize classes objects // as an instance method
        if not name: # equals to say if name == ""
            # trying to catch a Value Error // by using try and except in get_student()
            raise ValueError("Missing name") # instead of just exit: sys.exit("Missing name") // or: return None 
        if coven not in ["Abomination", "Potions", "Bard", "Beast Keeping", "Construction", "Healing", "Illusion", "Oracle", "Plant", "Every"]:
            raise ValueError("Invalid Coven track")
        self.name = name
        self.coven = coven
        self.palisman = palisman

    # need to defined __str__ to recieve a 'readable' object instead of calling the file's hosting folder
    def __str__(self):
        return f"{self.name} from {self.coven} coven track"

    def charm(self):
        if self.palisman == "Ghost":
            return "😼👻"
        elif self.palisman == "Clover":
            return "🐝🍀"
        elif self.palisman == "Emmiline":
            return "🐌💙"
        elif self.palisman == "Owlbert":
            return "🦉"
        else:
            return "🧙‍♀️"


def main():
    student = get_student() ## returned student as a tuple containing name and coven
    # print(f"{student.name} from {student.coven} coven") // too much of a hell
    print(student)
    print("Here we go!")
    print(student.palisman) # |||| funca ahora si djflkd pero los emotes no zzz


# class is powerful/migthy || both shit() and get_student() are similar
def get_student():
    name = input("Name: ")
    coven = input("Coven: ")
    palisman = input("Palisman: ")
    return Student(name, coven, palisman) # construct call --> treating Student as a function
    # defined an architecture for a variable/different parameter (covens in suburbs)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def shit(): # other way to define evrthng
    student = Student() # matches class
    # for libraries/dicts student["name"]
    student.name = input("Name: ") # recalling
    student.coven = input("Coven: ")
    return student


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# instead of using index assignation, let's use direct name assign.
def longer():
    student = {}
    student["name"] = input("Name: ") # remember to recall printing
    student["coven"] = input("Coven: ")
    return student
#   return (name, coven) ---> tuple inmutable + indexed || [n,h] list pliability
# we can recall the tuple by his index --> {student[0]} from tuple
# tuple for a more defensive programing way || in contrast, a list is pliable, but can lead to bugs
# also, tuples can't be assigned twice, so 'tuple' object can't support this (INMUTABLE)

# shorter/compacted version
def shorter():
    name = input("Name: ")
    coven = input("Coven: ")
    return {"name": name, "coven": coven}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

if __name__ == "__main__":
    main()