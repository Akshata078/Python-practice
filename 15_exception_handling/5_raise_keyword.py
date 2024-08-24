# raise keyword  -

# for creating raise statement we use raise keyword
# we use raise statement for raising exception
# An exception can be raised forcefully by using the raise clause in python
# raise statement is used when we want to throw exception for particular condition


# user-defined exceptions :-

# Exceptions created by programmer
# ex. withdrawing money



# raise keyword example -
# ex. input age = -10
#     ValueError : invalid age  (ValueError is exception name  & invalid age is exception message)


# syntax => 
# raise ExceptionName("exception message")


try:
    age = int(input("enter your age : "))
    if age < 0 :
        raise ValueError("invalid age")
    print("Your age is : ", age)
    
except ValueError as var:
    print(var)

print("rest of code")