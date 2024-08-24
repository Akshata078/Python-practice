# OOP (Object Oriented Programming)

# 1. object 
# 2. class  - blueprint of object
# 3. inheritance - 1. parent class 2. child class

# DRY (Dont Repeat Yourself)


# class : blueprint fro creating a new object (ex. class)
# object : instance of class   (ex. vishwajeet, ajit)

# property / feature = Attributes
# function = method



# class -

# agr hum class bana rhe hai toh python me uska first letter capital rakhenge

# create class -
    
# class Human :
#     pass


# create object -

# vishwajeet = Human()  # we have created a object and store it in vishwajeet variable, vishwajeet is object here

# print(type(vishwajeet))  # <class '__main__.Human'>  # jo bhi class ham banayenge uske aage __main__ aayega

# print(type(2))  # <class 'int'> - it  means 2 ek object hai int class ka  # ye class python me banaya hai toh  isme __main__ nhi aayega


# method - function inside the class
# jab bhi hum function ya method banante hai class me toh uske parameter me self name ka parameter hamesha rhega

class Human :
    def eat(self):
        print("eating...")
    def walk(self):
        print("walkning..")

akshata = Human()

akshata.eat()
# akshata.walk()

surbhi = Human()

# surbhi.eat()
surbhi.walk()


















