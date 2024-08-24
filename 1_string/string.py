# how we can write a string in python ? 1. single quotes  2. double quotes  3. tripple quotes
# 1. single quotes : ''
# 2. double quotes  : ""
# 3. tripple quotes :  ''' ''' (agr hame ek line chod ke hamara text lekhna hai, aur isme jo bhi likhenge vo as it is print hoga without ignoring spaces and next line)
# tripple quote ex. 

sentense ='''Hiii
I am
Akshata'''
# print(sentense)

# this can be used in while writting email



##########*****


# Functions used in string 

# 1)

# len() - for string length (it gives us the length of the string)
# isme space bhi count hoga

# name = 'Akshata Khadse'
# length = len(name)
# print(length)


# if we want to know any specific character from its index no.  (isme indexing 0 se start hogi)

# f_name = 'Akshata'
# print(f_name[1])


# if we want last character - (we will use minus, if we give minus then it will count from last)
# jab positive hoga toh indexing 0 se start hoi, aur jab negative hoga toh indexing -1 se start hogi.

# f_name = 'Akshata'
# print(f_name[-1])

#*********


# 2)

# slice() : extracts a part of a string
# ex.
# greet = 'hello world'
# new_greet_after_extracted = greet[2 : 5]

# # new_greet_after_extracted = greet[2 :] # iska matlab index no. 2 se start krega aur end tk jayega
# # new_greet_after_extracted = greet[:]  # isme 0 indexing se start hoga aur end tk jayega means jo bhi string hogi vo as it is print ho jayegi.
# print(new_greet_after_extracted)

# in the above example - 0 means konse index no. se start hoga. and 5 means kaha pr end hoga, but it will not include 5.


####********


# Concatination  (joining two strings together)

first_name = "Akshata"
last_name = "Khadse"
# print(first_name + " " + last_name)


#*************



# Formated string

full_name = f'Good Morning, {first_name} {last_name}'
# print(full_name)

# isme pehle capital (F) ya small (f) likhenge, then single quotes ya fir double quotes denge, aur usme hum hamari string likhenge

# isme single ya double quotes likhenge toh vo string bann jayegi aur jab iske aage hum (f or F) likhenge toh vo formatted string bann jayegi.

# agr isme hame variable ki value likhni ho toh vo curly bracket {} ke andar likhenge. 

# aur agr do variables hai uske bich me space chahiye toh simply hum space de denge. isme alg se single ya double quotes ke andar space dene ki jarurat nhi hai.

#  isme curly bracket ke andar jo bhi statement likkhenge vo bhi run hoga like hum koi mathematical expression perform kr sakte hai (ex. {2+3} , then hum koi method ya function ko bhi likh sakte hai (ex. {len(first_name)} ))








