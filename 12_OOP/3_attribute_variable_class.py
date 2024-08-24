# create variable or attribute in class by using __init__ magic method


# class Human :
#     def __init__(self) :
#         self.name = "Akshata"  # created name variable
#         self.age = 20  # created age variable
#     def eat(self):
#         print("eating...")
#     def walk(self):
#         print("walkning..")

# akshata = Human()  # we have created a akshata object of Human class
# akshata.eat()
# print(akshata.name)  # Akshata
# print(akshata.age)   # 20

# surbhi = Human()  # we have created a surbhi object of Human class
# surbhi.walk()  

# print(surbhi.name) # Akshata
# surbhi.age = 19
# surbhi.name = "Surbhi"
# print(surbhi.age)  # 19 - because hamne surbhi iss object me jo age hai usko update kiya hai.
# print(surbhi.name)  # Surbhi



# how to change default value of variable or attribute- 

# jab hum new object bana rha hai toh, ussi time jo usme name aur age ki value pass kr rhe hai, toh isme hum __init__ method ka use kr rhe hai toh jab jab hum naya object create krenge tb tb ye init wala function call hoga, aur fname variable me name ki value chali jayegi aur age_val variable me age ki value jayegi. fir self.name hai toh name me fname ki value jayegi aur age me age_val ki value.
# aur jab jab hamara object create hoga ye method call ho jayegi toh hamare name aur age ki value store hoti jayegi variable me

class Human :
    def __init__(self, fname, age_val) :
        self.name = fname
        self.age = age_val
    def eat(self):
        print("eating...")
    def walk(self):
        print("walkning..")

akshata = Human("Akshata", 20) 
surbhi = Human("Surbhi", 19) 

# print(akshata.name, akshata.age)  # Akshata 20
# print(surbhi.name, surbhi.age)  # Surbhi 19