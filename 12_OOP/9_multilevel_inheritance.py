# Multilevel Inheritance -


class Animal :
    def eat(self) :
        print("eating")

class Bird(Animal):  # inherit Animal class
    def fly(self) :
        print("flying")

class Eagle(Bird): # Inherit bird class and bird class inherit kr rha ai Animal class ko, toh isme Animal class aur Bird class inn dono ki methods and properties aa jayegi, isi ko hum multilevel inheritance bolte hai.
    def breed(self) :
        print("white-tailed eagle")




























