# Exception handling -

# what is exception ?
# =>
# An Exception is an event which occurs during the execution of program that disrupts normal flow of program
# it is the situation that python cant cope with it 

# # ex. 1)
# num1 = 10
# num2 = 0
# result = num1 / num2   # we got error here only, after this line our code will not execute. because here we are doing 10 / 0 so python is not able to understand this. and also rest of the cod will not execute
# print(result)  
# print("rest of code")

# # o/p - ZeroDivisionError


# # ex. 1)
# in1 = 100
# in2 = "hello"
# result = in1 + in2  # here we are adding a number to a string, in python, we cannot do like this, so it will give type error and rest of the code will not execute
# print(result)
# print("rest of code")

# # o/p - TypeError



# why this exception is dangerous ?  or need of exception handling 
# =>
# lead to sudden terminate of program
# can block the application
# data loss problem can occur (ex. two program - debit,credit   debit : rs. 100 but due to some issue in the credit program, money is not credited.  )
# corrupt data files



# exception vr syntax error 

# error - errors cannot be handled
# exception - exception can be handled using exception handling syntax.   

















