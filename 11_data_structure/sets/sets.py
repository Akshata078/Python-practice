# sets -

# It is the collection of unique data
# isme duplicate data nhi hoga
# it will return the output in curly bracket {}
# if duplicate data present then it will remove that duplicate data
# This will not support indexing, for accessing element inside set we can use loop
# in this, the items are shuffle their position

# set() :-

list1 = [1, 2, 3, 1, 2, 5, 2]
set1 = set(list1) # converting list into set
# print(set1)  # {1, 2, 3, 5}


# add() :- for adding data in the set

# set2 = {1, 8, 5, 4}
# set2.add(12)
# print(set2)  # {1, 4, 5, 8, 12}
# set2.add("set_item_add")
# print(set2)  # {'set_item_add', 1, 4, 5, 8, 12}


# remove() :- remove item from the set

set3 = {1, 2, 3, 5}
# set3.remove(5)
# print(set3)  # {1, 2, 3}



# len() :- return length of set

# print(len(set3))  # 4



# union of set :- combining two or more set in one set
#  for this we use here pipe symbol :-  |

set4 = {1, 2, 5, 7, 6}
set5 = {1, 4, 2, 3}

# union = set4 | set5
# print(union)  # {1, 2, 3, 4, 5, 6, 7}



# intersection of set :- common data in two or more set
#  for this we use here & symbol :-  &

# intersection = set4 & set5
# print(intersection)  # {1, 2}




# search item in set :-

fruits = {"apple", "cherry", "orange"}

# print("cherry" in fruits)  # True



# convert set into list :-

# print(list(fruits))  # ['apple', 'cherry', 'orange']

