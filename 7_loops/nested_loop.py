# nested loop :- loop inside a loop (loop ke andar loop)


# nested loop : for

# for num1 in range(5):
#     for num2 in range(3):
#         print(f"{num1}, {num2}")
#     print("-----------")

# output
# 0, 0
# 0, 1
# 0, 2
# -----------
# 1, 0
# 1, 1
# 1, 2
# -----------
# 2, 0
# 2, 1
# 2, 2
# -----------
# 3, 0
# 3, 1
# 3, 2
# -----------
# 4, 0
# 4, 1
# 4, 2
# -----------

# in the above examle, pehle num1 wala loop execute hoga fir usme num2 wala loop nested hai toh num2 wala loop execute ho jayega pura jab num2 wala execute ho jayega toh fir vo firse num1 wale loop me chala jayega aur ye loop aise hi chalta jayega jab tk num1 wale loop ki condition false nhi ho jati means num1 wala loop khatam nhi ho jata tb tk



# if we want to print the table from 1 to 5

# for table1 in range(1, 6) :
#     print(f"Table of {table1}")
#     for num in range(1, 11):
#         print(f"{table1} * {num} = {table1 * num}")
#     print("--------------")





# right angled triangle pattern of star

# *
# **
# ***
# ****

# for star in range(1, 6):
#     for star2 in range(1):
#         print(f"{star  * "*"}")


# OR

# end = \n :   python me by default end me \n hota hai jo hame next line deta hai.

# for x in range(1, 6):
#     for y in range(1, x+1):
#         print("*", end="")
#     print("")  # this is for next line








# nested loop : while

# right angled triangle pattern of star

# *
# **
# ***
# ****

# rows = 1

# while rows <= 5:
#     col = 1
#     while col <= 1 :
#         print(f"{rows  * "*"}")
#         col+=1
#     rows += 1


# OR


# rows = 1

# while rows <= 5:
#     col = 1
#     while col <= rows :
#         print("*", end=" ")  # iss end ke baad jo bhi likhenge vo print hoga
#         col+=1
#     print(" ")
#     rows += 1




# we can nest for loop in while loop also we can nest the while loop in for loop

