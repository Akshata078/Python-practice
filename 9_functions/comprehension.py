# comprehensions : map aur filter function ko easy way me likhne ka tarika

students = [
    ("Akshata", 91),
    ("Tanvi", 95),
    ("Janhavi", 90)
]

# map function

# names = list(map(lambda item : item[0], students)) # jo hame map object milega map function se usse hum yahi pr list me concert kr rhe hai
# print(names)  # ['Akshata', 'Tanvi', 'Janhavi']



# map function by using comprehension -

# syntax ->  variable_name = [statement_of_function for x in list]

# new_names = [item[0] for item in students]
# print(new_names)  # ['Akshata', 'Tanvi', 'Janhavi']


# filter function

# filter_names = list(filter(lambda name : name[1] > 90, students))
# print(filter_names)  # [('Akshata', 91), ('Tanvi', 95)]




# filter function by using comprehension -

# syntax ->  variable_name = [statement_of_function for x in list if condition]

# new_filter_names = [name for name in students if name[1]>90]
# print(new_filter_names)   # [('Akshata', 91), ('Tanvi', 95)]