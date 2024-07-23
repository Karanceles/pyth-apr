class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # getter/setter finds out if you're trying to change values manually // it doesn't allows it
    @property # new f(x) called house ||| but variable is also called house // need to define it 
    def house(self):
        return self._house

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") # we can check out for errors in the setter instear in __init__
        self._house = house
    # getter returns attribute value --> ._house (attribute/variable) assigns --> house (parameter) as attribute

def main():
    student = Student.get()
    print(student)

if __name__ == "__init__":
    main()