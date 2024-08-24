


# sort the list according to student marks in decending order

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






# by using lambda function -




# Lambda function -

# It is the function without name
# It is the anonymus function (anonymus function means - the function that dont have any name)
# when we have to write only one statement inside the function then we can use lambda function
# isme hum kitne bhi arguments pass kr sakte hai, but iske andar only one expressio ya statement likh sakte hai.
# jab hame ek function ke andar dusra function pass krna hota hai, aur uss function ke andar only one statement chahte hai tb lambda function use krenge
# iss function me return likhne ki jarurt nhi hoti hai

# syntax - 
# lambda parameter:statement

# lambda - means hum ek function bana rhe hai jiska koi name nhi hai
# parameter - means yaha pr koi bhi parameter pass kr sakte hai.
# statement - one line wala statement ya code, expression likhenge




# sort the list according to student marks in decending order

# students = [
#     ("Akshata", 91),
#     ("Tanvi", 95),
#     ("Janhavi", 90)
# ] 

# students.sort(key=lambda stu: stu[1], reverse=True) 
# print(students)  # [('Tanvi', 95), ('Akshata', 91), ('Janhavi', 90)]