# scope of variable 
# 1. local scope    2. global scope


# 1. local scope 

# agr hum kisi variable ko kisi function me likhte hai toh vo variable uss function me hi access hoga, uss function ke bahar access nhi hoga
# agr hum kisi function me koi varible likhte hai, then hum usko function ke bahar print karna chahenge toh vo error dega ki varible is not defined, because vo variable only hum function me hi access kr sakte hai, function ke bahar access nhi kr sakte

# def hello():
#     message = "Good Morning"  # in this, message variable is local variable because ye function me hi access ho sakta hai, function ke bahar access nhi hoga.
# hello()
# print(message) # NameError: name 'message' is not defined



# 2. global scope

# agr hum kisi variable ko function ke bahar likhenge globally then vo function me bhi access hoga aur function ke bahar bhi access hoga, toh uska global scope hoga
# global variable means vo kisi bhi function me nhi likha hoga, and it is accesssible throughout the code

# num = 5  # num is a global variable here, because it is not written in any function, and it is accesssible throughout the code
# def hello_num() :
#     print(num)  # 5
# hello_num()  
# print(num)  # 5



# num = 1 # global variable
# def hello(name):  # name is local variable
#     message = "good morning"  # local variable
#     print(name)  # Akshata
# hello("Akshata")
# print(name)   # NameError: name 'name' is not defined

# jo ham arguments pass krte hai vo bhi local variable hote hai




# var0 = "global variable"

# def fun1() :
#     var0 = "local variable"
#     print(var0)  # local variable  - agr function me humne same name diya hai global variable ka hi, toh ye jo local variable ki value hai vahi lega, or we can say this like - ki humne jo var0 ki value thi vo function me update ki, tbhi vo local variable print kr rha hai. but jab hum function ke bahar var0 ki value print kr rhe hai toh vo globally check kr rha hai var0 ki value toh vo global variable ki value print krega
# fun1()
# print(var0) # global variable



# if we want to change the value of global variable inside the function also want to change it globally
# # ex.
# var0 = "global variable"
# def fun1() :
#     global var0   # ye batayega ki fun1 ke andar ek naya variable mt banao, local variable mt banao, uski jagah pr global wala variable access kro
#     var0 = "local variable"  # global varable ko access kiya aur var0 = "local variable" isne global variable ko overright kar diya
#     print(var0)  # local variable
# fun1()
# print(var0) # local variable