# if statement

# syntax - 
# if condition :
#     code

# jab bhi if statement true hoga,  tohh uske niche jo bhi statement indent krke likha hai (matlab kuch space chod kr likha hua hai) vo execute hoga, print hoga jab if statement true hoga tbhi, agr condition false hogi toh vo print nhi hoga.


marks = 5

if marks >= 40 :
    print("Result : PASS")

    print("check if statement")  # ye wala part bhi run hoga jab if statement true hogi, agr if statement false hogi toh ye execute nhi hoga. ye if statement ka part hoga because one tab ka space chod kr likha hai

print("This is not part of if statement") # ye wala statement hamesha run hoga if statement true ho ya na ho because this is not part of the if statement (if statement ka part nhi hai because ye statement ke pehle hamne space nhi diya hai 1 tab ka.)




# if statement true hoga tbhi uske andar ka part run hoga nhi toh run nhi hoga

# if statement ke andar ka statement vahi mana jayega, jiske aage space choda rhega indent rahega





# if 1 > 2 :
#     print("5 is greater than 2")
# print("always")



# we can also write like this

# agr condition me hame truthy value milti hai toh vo if wali statement run hogi, agr koi falsy value mili (ex. "", 0, False) toh vo if statement run nhi hogi
# if True :
#     print("Hello World")

# if "" :
#     print("empty string")

# if "hii" :
#     print("hii is not empty string")


# if ko falsy value milegi toh vo if statement run nhi hogi