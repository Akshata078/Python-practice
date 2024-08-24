# String Methods


# 1. upper() :- it will convert the string into capital letter, and this method will not change our original string

# text = 'My name is Akshata'
# new_text = text.upper()
# print(new_text)



# 2. lower() :- it will convert the string into small letter, and this method will not change our original string

# text = 'My name is Akshata'
# new_text = text.lower()
# print(new_text)



# 3. title() :- it will make first character/letter of every word capital and rest to the small letter. and this method will not change our original string

# text = 'My name is AKSHATA'
# new_text = text.title()
# print(new_text)



# 4. strip() :- it removes the white spaces from both the sides i.e. from left side as well as right side

# text = '        My name is Akshata            '
# print(text)
# new_text = text.strip()
# print(new_text)


# 5. lstrip() :- It removes the white spaces from the left side

# 6. rstrip() :- It removes the white spaces from the right side


# 7. find() :- If we want to find something or search something inside our text or string. This will search or find whatever we want to find inside our string and returns its index no. of first occurence

# text = 'My name is Akshata'
# new_text = text.find("name") # 3
# # new_text = text.find("Name")  # -1
# print(new_text)

# if we are searching something that is not present inside our string or text then it will return -1


#### in  :-  agr hame check krna hai ki koi word ya letter hamare string me present hai ya nhi toh hum use kr sakte hai.
# isme hame jo bhi search krna hota hai vo hum single ya double quotes me likhte hai, means string me likhte hai, then in keyword, uske baad kisme vo word ya letter search kr rhe hai uss variable ka name

# It will return True or False

# text = 'My name is Akshata'
# # new_text = "name" in text  # True  - here we are searching name inside the text 
# # new_text = "Name" in text   # False
# new_text = "Name" not in text   # True  - here we are checking that "Name" is not present in the text, thats why it is giving True
# print(new_text)



# 8. replace() :- We have to pass here two string, first string is for which string we want to replace, and second string is for with whom (which word) we want to replace.

# text = 'My name is Akshata'
# # new_text = text.replace("My", "Your") # we are replacing My to Your, it means we want to replace My with Your
# new_text = text.replace("a", "@") # here "a" will be replaced by @, jitne bhi "a" letter present honge text wali string me vo sare replace ho jayenge @ se
# print(new_text)













