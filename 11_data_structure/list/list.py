# data structure - data ko kis tarah se store kr rhe ho aur operatrion kr rhe ho

# if we want to store only one name then we can use a variable - # name = "Akshu"
# but if we want to store multiple values then we use list -

# indexing - in list, indexing starts from 0



# list in python

names = ["Akshata", "Janhavi", "Riya"]  # created a list

# print(type(names))  # list
# print(names)  #  ['Akshata', 'Janhavi',Riya']


# To store numbers in a list -
numbers = [1, 2, 3, 4, 5, 6]

# in a list we can write diffrent data types values also means we ca mix up the data type like if we want to store strings and numbers in one list then we can do that
mix_list = ["Akshata", "Janhavi", 37, 29]


# hum list ke andar bhi list store kr sakte hai -
marks = [[1, 2, 3], [5, 5, 7], [9, 3, 1], "Akshata", 37]



# how to join two lists
combine_list = names + numbers
# print(combine_list)  # ['Akshata', 'Janhavi', 'Riya', 1, 2, 3, 4, 5, 6]




# list() : list function -

# if we want a list that contains 0 to 100 whole numbers
num = list(range(101))
# print(num)


# if we want all odd no. in a list between 0 to 100
even = list(range(1, 100, 2))
# print(even)

# if we want every character of a string becomes the list item
text = "My name is Akshata"
new_list = list(text)
# print(new_list)



# len()

# if we want to find length of our list -
product = ["pen", "pencil", "book", "marker", 4]
length = len(product)
# print(length)



