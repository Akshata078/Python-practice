# Nested if else statement

# syntax -
# if condition :
#     if condition :
#         code
#     else :
#         code

# elif condition :
#      if condition :
#         code
#     else :
#         code

# else :
#     code




print("Checking Legal Age Of Marriage In India")

gender = input("Enter Male (m) or Female (f) : ")
age = int(input("Enter your age : "))

if gender == "m" :
    if age >= 21 :
        print("Legal age for marriage")
    else :
        print("Child Marriage")

elif gender == "f" :
    if age >= 18 :
        print("Legal age for marriage")
    else :
        print("Child Marriage")

else:
    print("Enter m for male and f for female")







