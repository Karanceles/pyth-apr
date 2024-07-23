# INHERITANCE | related classes properties altogther
class Wizard:
    def __init__(self, name):
        if not name:
            return ValueError("Missing name")
        self.name = name
        
class Student(Wizard):  # Student as a subclass of Wizard
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Proffesor(Wizard):
    def __init__(self, name, subject):
        super.__init__(name)
        self.topic = subject

wizard = Wizard("Albus")
student = Student("Hermione", "Geyffindor")
professor = Proffesor("Severus", "Defense Against Dark Arts")