# Handling an exception -

# for exception handling, python provides 4 blocks -
# 1. try block  (required)
# 2. except block  (required)
# 3. else block  (optional)
# 4. finally block  (optional)


# syntax -

# try:  # try keyword is used for writing a try block
#       # colon represents this is thie block of code
#       # code containing exceptions (suspicious code)


# except ExceptionName:  # ExceptionName is optional
#                        # code to handle exceptions (if occured)
                         # if exception

# else:  # code to execute if no exceptions occured
         # if no exception

# finally :  # always execute



# example 1-

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# try :
#     division = num1 / num2
#     print(division)
# except ZeroDivisionError:
#     print("division by zero is not allowed")
# except NameError:
#     print("variable name is wrong")

# print("rest of code")

# explanation - if we divide 10 by 0, thyen in python, this division is not possible. so we have written the division code in try block because this can create a exception.
# so when we do division then firstly it will go to try block, if there is no exception then the code will run as we want. but if exception occur then it will go to the except block, and whatever code we write in that, that code will execute
# so when user try to divide any no. by zero then at that time exception occured so it will go to the exception block and whatever cod we write in that, it wikl execute that one.
# then rest of the code will execute. 

# we can write multiple exception block also



# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# try :
#     division = num3 / num4
#     print(division)
# # except (ZeroDivisionError, NameError) as obj:  # we can also write multiple exception like this. in this we have write - as obj, it means the msg that show on terminal when any exception occured, that msg will came in obj
# #     print(obj)

# print("rest of code")




# num3 = int(input("Enter first number : "))
# num4 = int(input("Enter second number : "))

# try :
#     division = num3 / num4
#     print(division)
# except:  # when we dont know which type of exception will occur
#     print("something went wrong")
# else:
#     print("an exception didnt occur")
# finally:
#     print("always executed")

# print("rest of code")


