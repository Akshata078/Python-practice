# Difference between tuples and list=>
# list : we can change the list
#      : It is mutable (we can change)
# tuples : we cannot change it
#        : It is immutable (we cannot change)



# Tuples :-
# 
# we use parenthesis() for creating tuples
# agr hum parenthesis nhi denge tb bhi vo tuple bann jayega, jab bhi hum ek se jyada item kisi variable me store krna chahege toh vo tuple bann jayega
# we can store any kind of data types in tuples, we can mix it also and store (in this, we can store string, numbers, character, boolean )
# in tuple indexing starts from 0 

# student = ("Akshata", 37, True)
# print(student)  # ('Akshata', 37, True)
# print(type(student))  # tuple


# t = (1, 2, 3)
# t[0] = 5     # it will give type error, we cannot change the items in tuple




# agr hum parenthesis nhi denge tb bhi vo tuple bann jayega, jab bhi hum ek se jyada item kisi variable me store krna chahege toh vo tuple bann jayega - 

# student = "Akshata", 37, True
# print(student)  # ('Akshata', 37, True)
# print(type(student))  # tuple


# student = "Akshata",  # isme hamne "Akshata" ke baad comma diya toh python ko lagega ki iske aage kuch hai toh vo isko tuple bana dega
# print(student)  # ('Akshata', )  
# print(type(student))  # tuple

# student = ()  # we have created a empty tuple here
# print(student)  
# print(type(student))  # tuple



# add two tupple (concatenate)

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tupple_add = tuple1 + tuple2
# tupple_add = (1, 2, 3) + (4, 5, 6)
# tupple_add = tuple2 * 3  # 3 times tuple2 repeate hoga
# print(tupple_add)  # (1, 2, 3, 4, 5, 6)




# tuple()

# convert list into tuple

# list1 = [1, 2, 3, 4]
# tuple1 = tuple(list1)
# print(tuple1)  # (1, 2, 3, 4)




# in tuple indexing starts from 0 

# access item in tuple

tuple2 = (1, 2, 3, 4, 5)
# print(tuple2[1])  # 2 
# print(tuple2[-1])  # 5 (we have give -1 that means indexing starts from last)



# unpacking in tuple

tuple3 = (1, 2, 3)
first, second, third = tuple3
# print(first)  # 1
# print(second)  # 2
# print(third)  # 3



# check item present in tuple or not

tuple4 = (1, 2, 3, "Pen", "Pencil")

# if "Pen" in tuple4 :
#     print("yes")
# else:
#     print("no")





# # sort the list according to student marks in decending order

# students = [
#     ("Akshata", 91),
#     ("Tanvi", 95),
#     ("Janhavi", 90)
# ]  # hamare pass ek list hai, jisme hum info store kr rhe hai, isme harr ek student ka information ek tuple me store hai, tuple me do information hai name aur marks 

# # # students.sort()  # ye hame name ke hisab se sort krke dega

# def sort_students(stu) :  # isme humne ek function banaya aur ye one by one jo students name ki list hai uske andar jo tuple hai uski value access kr rha hai aur vo stu variable me ja rhi hai. matlb tuple stu variable me ja rha hai
#     return stu[1]  # means tuple ke index one ki value jo ki student ke marks hai
# ## sort me ek argument hota hai key, isme hum batate hai ki hame kya sort krna hai
# students.sort(key=sort_students, reverse=True) 

# print(students)



