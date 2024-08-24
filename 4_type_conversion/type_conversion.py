# Type Conversion : Convert one type of data to another type of data

# Two types of type conversion - 
# 1. explicit :- if we are converting data type from one data type to another manually then it is explicit conversion  
# 2. implicit :- python automatically convert one data type to another


# Data Types or Types of Data

# 1. int  (5)
# 2. float (2.5)
# 3. string  ("Hello")
# 4. boolean  (True or False)


# type()  ;- for checking the type of data (which data type we are using, we can check it by using type())

# print(type(5))   # int
# print(type(9.4))  # float
# print(type("hello"))  # str
# print(type(True))   # bool
# print(type(False))   # bool



# print(1 + 1)   # 2
# print("1" + "1")  # 11 -  because we are concatenating two strings here
# print("1" + 1)  # it will give error because we can not concatenate a string with a number

# + will work only when both  the data types are same otherwise it will give error





# 1) explicit 


# inbuild function for type conversion -

# 1. int() :- it will convert the data type to integer

# data = "1"
# result = int(data) + 1   # in this, string of 1 that is stored in data variable is converted into integer
# print(result)     # 2

# 2. float() :- it will convert the data type to integer (it will convert the string to the float, or any integer number to float)

# print(float(7) + 2)   # 9.0
# print(float("5") + 2.5)   # 7.5


# 3. str() :- it will convert the data type to string data type

# print(str(6))   # string of 6
# print(str(5) + 4) # it wll give error because 5 is a integer and we are converting it inot string data type and then we are adding 4 to it, so  in this we are adding a string with a number, thats why it will give error
# print(str(5) + "4") # 54 - because firstly number 5 converted into string and 4 is also a string so t will concatenate and gives 54


# 3. bool() :- it will convert the data type to boolean data type
# in this, if it is falsy value then it will print False, otherwise print True

# falsy value - False, "", 0, None

# other than this falsy value all values are truthy

# print(bool("true"))   # True
# print(bool("hi"))     # True
# print(bool(1))        #True
# print(bool("false"))  # True  # it is a string but not empty string, so it will give True
# print(bool(0))        # False  - 0 is falsy value thats why it is giving False
# print(bool(False))    # False - Falsy value
# print(bool(None))     # False - None is Falsy value
# print(bool(""))       # False - empty string ("") is Falsy value




# in this, if there is falsy value, only that time it will give false. otherwise true

# falsy value - "", 0, None