# **kargrs :- we can pass unlimited keyword arguments
# we get output in dictionary

# def add_student(**args) :  # firstly we have to write the two asterisk ** symbol and then any variable name, by doing this, we can pass unlimited keyword arguments in the variable, here instead of args you can give any name to variable
#     print(args)  # {'name': 'Akshata', 'roll_num': '19EE037', 'age': 20} - we get output in dictionary

# add_student(name="Akshata", roll_num = "19EE037", age = 20)  # yaha se hum jo bhi keyword arguments pass krenge vo args variable me store ho jayega.



# how can we access the value one by one
# ex.
# def add_student(**args) : 
#     for x in args :
##         print(x)  # yaha pr hame keyword milega, means jo argument ka name hai, keyword hai vo milega
#         print(args[x])  # we get the value of the keyword

# add_student(name="Akshata", roll_num = "19EE037", age = 20) 



# if we want name and value both
# ex.
# def add_student(**args) : 
#     for x, y in args.items() :  # items() name ka function liya jo hame name aur value dono return karega. aur name ki value hamne x variable me store ki aur uski value hamne y variable me store ki
#         print(f"{x} = {y}")
# add_student(name="Akshata", roll_num = "19EE037", age = 20) 



