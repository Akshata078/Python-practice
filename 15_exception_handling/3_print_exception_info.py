# Print Exception name -
# 1. using exception class object
# 2. using sys module


# harr ek class ek built in exception hota hai. 
# jab bhi exception occur hota hai ye class ko call krta hai.
# ex. class ZeroExceptionError



# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# try :
#     division = num3 / num4
#     print(division)
# except ZeroDivisionError as var:  
#     print(var.__class__)  # jo bhi class hai vo call jayega

# print("rest of code")



# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# try :
#     division = num3 / num4
#     print(division)
# except Exception as var:  # if we dont know which exception will occur
#     print(var)  # information
#     print(var.__class__)  # jo bhi class hai vo call jayega

# print("rest of code")




# using sys module -



# import sys

# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# try :
#     division = num3 / num4
#     print(division)
# except :
#     print(sys.exc_info()[0])  # it will print exception class 
#     print(sys.exc_info()[1])  # it will print exception information

# print("rest of code")






# which Exception first ? 

# => jo exception pehle occur hoga usko pehle handle karta hai python


# import sys

# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# try :
#     division = num3 / num   # NameError
#     print(division)
# except :
#     print(sys.exc_info()[0])  # it will print exception class 
#     print(sys.exc_info()[1])  # it will print exception information

# print("rest of code")









# Python Exception Hierarchy =>

# Python me harr ek exception ek built in class hota hai.
# ex. - consider ZeroDivisionError ye ek exception hai aur ye ek built in class hai

# jab koi exception occur hota hai toh python iterpriter three steps follow karta hai -
# 1. calls class 
# 2. constructor
# 3. raise statement

# means agr ZeroDivisionError ye exception aaya toh pehle uske class ko call krega fir uska constructor execute krega and uske constructor me raise statement hoga

# Root class of exception hierarchy - BaseException

# built in class ko hum bolte hai - built in exception 
# built in exception ko python creater create kata hai
