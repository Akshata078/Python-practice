# agr kisi object ko koi speacial variable dena ho, attribute dena ho


# class Human :
#     def __init__(self, f, l,  age_val) :
#         self.first_name = f
#         self.last_name = l
#         self.age = age_val

# akshata = Human("Akshata", "Khadse", 20)
# surbhi = Human("Surbhi", "Thakur", 19)

# # akshata ko suppose ek extra attribute dena hai -
# akshata.programming = "c, python, javascript"
# print(akshata.programming)  # c, python, javascript

# print(surbhi.programming)  # attributeError - because surbhi object ko programming ye attribute mila hi nhi hai.





# class attribute vs object attribute =>

# class attribute => country = "india"
#                  - isko hum bina object banaye bhi access kr sakte hai.

# object attribute => self.fname = name 
#                  - isme hum bina object banaye usko access nhi kr payenge
#                   


# class Human :

#     country = "India"  # isko hum bina object banaye bhi access kr sakte hai.

#     def __init__(self, f, l,  age_val) :
#         self.first_name = f
#         self.last_name = l
#         self.age = age_val

# print(Human.country)  # India

# print(Human.first_name)  # error - AttributeError: type object 'Human' has no attribute 'first_name'  # isme hum bina object banaye usko access nhi kr payenge












