# map function -

# in map function - we pass two arguments 1. function 2. iterable(iterable means koi bhi chij jisme ek se jyada element ho, jispr for loop lagaya ja sakta hai)
# ye hame ek map name ka object return krega

# syntax -
# map(function, iterable)

# it will work on list and tupple both


students = [
    ("Akshata", 91),
    ("Tanvi", 95),
    ("Janhavi", 90)
]

# if we want only list of names in the students list inside tuple

# names = []
# for x in students:
#     names.append(x[0])
# print(names)  # ['Akshata', 'Tanvi', 'Janhavi']


# by using map function

# map(lambda, list)

# names = map(lambda item : item[0], students)  # isme jo students name ki list hai uska one by one ek ek item aayega jo ki ek tuple hai, aur uss tuple ko item iss argument me le rhe hai aur vo hame item[0] means student ka name return kr rha hai one by one, aur ye hum names variable me store kr rhe hai.
# # yaha pr hum map function ka use kr rhe hai toh names me map wala object chala jayega, because map function hame ek object return krta hai.
# new_list = list(names)  # isme hum jo names me map wala object store tha usko list me convert kr rhe hai aur usko new_list iss variable me store kr rhe hai.
# print(new_list)  # ['Akshata', 'Tanvi', 'Janhavi']

# OR 

# names = list(map(lambda item : item[0], students)) # jo hame map object milega map function se usse hum yahi pr list me concert kr rhe hai
# print(names)  # ['Akshata', 'Tanvi', 'Janhavi']

