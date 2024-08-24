# filter function -

# it will return a filter object

# syntax -
# filter(function, iterable)



students = [
    ("Akshata", 91),
    ("Tanvi", 95),
    ("Janhavi", 89), 
    ("Kajal", 70)
]

# if we want a students list whoes marks is greater than 90

# new_list = []
# for x in students:
#     if x[1] > 90 :
#         new_list.append(x[0])
# print(new_list)  # ['Akshata', 'Tanvi']



# by using filter function

# filter_names = list(filter(lambda name : name[1] > 90, students))
# print(filter_names)  # [('Akshata', 91), ('Tanvi', 95)]