# Dictionaries :- it is the collection of key value pair 
# we can not access data by indexing, we can access it by key

# create dictionary - 
# dic1 = {"x" : 20, "y" : 10}

#  we can creat a new dictionary like above ex.
# in this, we use colon 
# and, we use single quote or double quotes for writting key name

student = {
    "name" : "Akshata", 
    "age" :20,
    "Course" : "BTech"
}

# print(student)  # {'name': 'Akshata', 'age': 20, 'Course': 'BTech'}


# dict() :-

#  we can creat a new dictionary from this function also
# in this, we use equal to sign instead of colon
# and, we dont use single quote or double quotes for key

dict2 = dict(
    name = "Akshata", 
    age = 20,
)
# print(dict2)  # {'name': 'Akshata', 'age': 20}





# how to access data ?

# if i want to access name from student dictonary -
# print(student["name"])  # Akshata



# update value of key -

# student["Course"] = "Software Programming"
# print(student)  # {'name': 'Akshata', 'age': 20, 'Course': 'Software Programming'}


# add data or add new key value pair -

# student["contact no."] = 87749944
# print(student)  # {'name': 'Akshata', 'age': 20, 'Course': 'BTech', 'contact no.': 87749944}



# check key present in dictionary or not -

# if "name" in student:
#     print("yes")
# else:
#     print("no")


# get()  :- 
# 
# we can check the key present in disctionary or not,if it is present then we get that value of the key, if the key is not present the we get None
# also if the data is not present then we can print the default value also 

# print(student.get("name"))  # Akshata
# print(student.get("mobile"))  # None
# print(student.get("phone", 10000))  # 10000
# print(student.get("phone", "Not present"))   # Not present



# del - we can delete key value pair from dictionary

# del student["Course"] 
# print(student)  # {'name': 'Akshata', 'age': 20}


