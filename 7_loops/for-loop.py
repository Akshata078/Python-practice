# Loop :- Loop means repeating something over and over until a particular condition is satisfied.

# Two types of loop in python : 1. for loop   2. while loop
# There is no do while loop in python :)

# For Loop :- A for loop is used for itering over a sequence (that is either a list, a tuple, a distionary or a string)



#             ****range() function****

# Python range() Function :- returns a list of arithmetic progression.

# The range() function returns a swquence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number

# ex. Range(5) = 0,1,2,3,4

# range function is iterable object means it will itrerate over each element in it






# for loop syntax =>

# for variable-name in range(3) :
#     print("") or your code


# ex.
# for num in range(3) :
#     print("hii.. Akshata", num)

# print("for loop ends") # ye ek hi baar print hoga because ye for loop ka part nhi hai kyuki iske pehle 1 tab ka space nhi diya hua hai, toh ye for loop ke bahar ho jayega aur only one time print karega.

# in the above ex. range function me hamne 3 likha hai matlab hamara for loop 0 se start hoga and 2 pr end hoga, like 0, 1, 2 aur jo bhi range ki value hogi vo num variable me chali jayegi, means pehle 0 aayega, then 1, then 2 aayega.
# range function ne hame list of number diya, aur for loop hai vo harr number ke pass ek ek baar jayega, aur uss number ko store krega num variable me.




# if we want our for loop start from 5 and ends at 10

# for num in range(5,10):  # 5 is starting point, and 10 is ending point
#     print("hello", num)




# if we want our for loop ek specific number se aage badhe, ya agr hum chahte hai ki kisi particular number ka gap aa jaye bich me

# for num in range(5, 10, 2):  # 2 se jump krega means pehle 5 se start ho rha hai toh 5 aayega then 2 se jump krega toh 7 aayega, firse 2 se jump krega toh 9 aayega. aur 9 pr hamara loop end ho jayega, isme 2 ka gap aa jayega
#     print("Hiiiii..........", num)



# range(3) => 0, 1, 2
# range(2, 5) => 2, 3, 4
# range(1, 10, 2) => 1, 3, 5, 7, 9





#          ***************

# logical for loop

#print 1 to 10

# for number in range(1, 11):
#     print(number)



# print even number between 1 to 10

# for even in range(1, 11):
#     if even%2 == 0:
#         print(even)
    

# 2 math table

# for table in range(1, 11):
#     print(f"2 * {table} = {table * 2}")






# for loop on string -


# name = "Akshata"\
# for char in name:
#     print(char)



# lname = "Khadse"
# for char in lname:
#     print(char)




# shopping cart example

# cart = ["Grapes", "Pen", "Coffee"]
# for item in cart:
#     print(item)