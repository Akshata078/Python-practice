# Multilevel Inheriance - 

# agr hum chahte hai ki koi class hai vo multiple classes ko inherit kre
# multiple classes ko inherit krne ke liye hum simple jiss class me inherit karna hai uss class me parenthesis ke andar unn sare classes ka name likhnge aur sbko comma se seperate krenge
# isme hum ek sath multiple classes ko inherit kr sakte hai

class Animal :
    def eat(self) :
        print("eating")

class Bird:  
    def fly(self) :
        print("flying")

class Eagle(Animal, Bird): # Eagle class Animal aur Bird inn dono classes ko inherit kr rha hai 
    def breed(self) :
        print("white-tailed eagle")


eagle1 = Eagle()  # eagle1 object created

eagle1.eat()  # eating
eagle1.fly()  # flying
eagle1.breed()  # white-tailed eagle



