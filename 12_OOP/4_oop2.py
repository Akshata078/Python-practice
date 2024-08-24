# accessing variable inside the class itself

class Human :
    def __init__(self, f, l,  age_val) :
        self.first_name = f
        self.last_name = l
        self.age = age_val
    
    def full_name(self) :
        print(f"full name : {self.first_name} {self.last_name}")  # accessing variable inside the class

akshata = Human("Akshata", "Khadse", 20)

# print(akshata.first_name)  # accessing variable outside the class

# akshata.full_name()  # full name : Akshata Khadse
