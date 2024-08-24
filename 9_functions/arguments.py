# argument - when we are calling a function, whatever we write in parenthesis, is called argument

# parameter - when we define a function, whatever we write in parenthesis is  called parameter


# def say_hello(name) :   # here name is parameter
#     print(f"Hiii....{name}")

# say_hello("Akshata")   # Akshata is  argument



# we can pass more than one argument

# def say_hello(fname, lname) :   # here fname and lname are parameter
#     print(f"Hiii..{fname} {lname}")
#     print("Good Morning")

# say_hello("Akshata", "Khadse")   # Akshata, and Khadse are argument



# agr ham parameter me one argument pass kr rhe hai but vha pr do value accept kr rhe hai parameter me toh ye hame error dega

# def say_hello(fname, lname) :   # here fname and lname are parameter that is accepting two argument
#     print(f"Hiii..{fname} {lname}")
#     print("Good Morning")

# say_hello("Akshata")   # Akshata is one argument


# above que mai ye hame error de raha h because ham isme only one argument pass kr rhe hai but vo function uske parameter me two values accept kr rha hai.
# iske liye hum parameter me koi default value de sakte hai, toh jab bhi argument me value pass nhi krenge toh vo default value ko lega aur print krega.

# def say_hello(fname, lname = "K") :   # here fname and lname are parameter that is accepting two argument and we have given a default value to lname
#     print(f"Hiii..{fname} {lname}")
#     print("Good Morning")

# say_hello("Akshata", "Khadse")
# say_hello("Akshata")   # Akshata is one argument

# and above ex. me agr hum parameter me argument sahi se pass kr rhe hai to vo default value nhi lega, but agr only one argumnt pass kr rhe hai toh vo default value el rhaa h 




# function for creating table of any number

# def create_table(num) :
#     for table in range(1, 11) :
#         print(f"{num} * {table} = {num * table}")

# create_table(6)


