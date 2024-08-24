# escape sequence

# text1 = 'this is 'python' turorial'  # in this if we want single quotes to python word then if we write like this then it will show error
# text2 = "this is "python" tutorial" # in this also if we want double quotes to python word and if we write like this then it will show error.

# if we want single quote to python word then we can write like this - 
text1 = "this is 'python' tutorial" # agr python pr single quotes chahiye toh jo puri string hogi usko double quotes lagayenge

# if we want single quote to python word then we can write like this -
text2 = 'this is "python" totorial'  # agr python pr double quotes chahiye toh jo puri string hogi usko single quotes lagayenge


# but what if we want to print the python word like this - 'python" or "python' or 'python  , for this we can use escape sequence


# Escape Sequence

# In this, we use escape character - (back slash) i.e. :- \

text3 = 'This is "python\' tutorial'
text4 = "This is 'python\" tutoral"
# print(text4)

# aur isme \ (back slash) print nhi hoga, back slash hai vo khud print nahi hoga jo uske next hota hai usko print krta hai without printing itself.


# escape character :   \

# esccape sequence : jab bhi hum escape character ke sath kuch likhte hai toh vo escape sequence bann jata hai.

# 1. back slash ke aage jo bhi  character aayega uska origial meaning badal diya jayega
# 2. escape character (backslash) ye khud print nhi hota
# 3. jab hum escape character ke sath koi chij milate hai toh usko escape sequence bolte hai




text5 = 'This is python\\ tutorial'
# print(text5)  # isme hame only one backslash milega because jo first backslash hai vo dusre wale ko escape kr dega



# \n  : it means vo next line me print karega, ek next line de dega

text6 = "This is \n python \ntotorial"
# print(text6) # ye This is ke baad ek new line me chalega jayega, python tutorial new line me print hoga.









