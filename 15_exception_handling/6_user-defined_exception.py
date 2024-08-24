# user-defined exception -

# step 1 -
# create exception class and inherit it from BaseException class. i.e Exception

# syntax -
# class InvalidAge(Exception):
#     pass


# step 2 -
# raise InvalidAge exception for particular condition (age<0) inside try block 
# InvalidAge ye ek aisa exception class hoga jo hamne banaya hai, and usse inherit kiya hai from exception class 

# syntax -
# try :
#     if age < 0 :
#         raise InvalidAge("message")




# step 3 -
# handle the exception using except block 

# syntax -
# except Exception as obj :  # here obj is our variable, iss variable me message aa jayega jo hamne raise statement me likha tha
# print(obj)




# example - write a python program for FiveDivisionError Exception

# class FiveDivisionError(Exception):  # Exception class se inherit kiya because FiveDivisionError ye hamara ek exceptio bann jaye
#     pass

# try :
#     num1 = int(input("Enter a number 1 : "))
#     num2 = int(input("Enter a number 2 : "))

#     if num2 == 5 :
#         raise FiveDivisionError("Cannot devide by five")
    
#     result = num1 / num2
#     print("Result : ", result)

# except (FiveDivisionError, ZeroDivisionError) as obj:
#     print(obj.__class__)
#     print(obj)


# or 


# class FiveDivisionError(Exception):  # step 1

#     def __init__(self) :   # constructor
#         print("cannot divide by five")
#     pass

# try :  # step 2
#     num1 = int(input("Enter a number 1 : "))
#     num2 = int(input("Enter a number 2 : "))

#     if num2 == 5 :
#         raise FiveDivisionError
    
#     result = num1 / num2
#     print("Result : ", result)

# except (FiveDivisionError, ZeroDivisionError) as obj:  # step 3
#     print(obj.__class__)
#     print(obj)









