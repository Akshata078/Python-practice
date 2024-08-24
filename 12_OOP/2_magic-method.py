# magic method :
# ye already define hota hai hame bss inka use krna hota hai.
# iss method ke name ke aage do underscore hoga aur name ke baad two underscore
# jab koi event occur hota hai toh ye automatically call hota hai.


# difference between magic method and normal method -

# magic method -  jab koi event occur hota hai toh ye automatically call hota hai.
# normal method - we need to call it 


#print(dir(int))  # ye pure magic method ka name de dega

#           ***************

# 1. __init__
# jab jab koi object create hoga ye tb tb call hoga

# class Human :
#     def __init__(self) :
#         print("object created...")
#     def eat(self):
#         print("eating...")
#     def walk(self):
#         print("walkning..")

# akshata = Human()  # we have created a akshata object of Human class
# # akshata.eat()

# surbhi = Human()  # we have created a surbhi object of Human class
# # surbhi.walk()  



# 2. __str__
# iss method me jo bhi kuch print krna hai usko hum return karte hai print nhi krte hai
# jab hum object ko print karana chahte hai toh ye __str__ magic method execute hoga

# class Human :
#     def __init__(self, f,  age_val) :
#         self.first_name = f
#         self.age = age_val

# akshata = Human("Akshata",  20)

# print(akshata)  # ye hame batayega jo akshata hai vo Human name ka object hai. 

# jab bhi hum kisi object ko print krte hai tb vo batata hai ki vo konse class ka object hai aur uski memory location batata hai. 
# agr hum iske behaviour ko change karna chahte hai ki jab bhi hum object ko print karwaye alg tarah se output aana cahiye toh iske liye hum __str__ iss magic method ka use krte hai



class Human :
    def __init__(self, f,  age_val) :
        self.first_name = f
        self.age = age_val

    def __str__(self) :
        return f"{self.first_name} is a human object and age of this human is {self.age}" # iss method me jo bhi kuch print krna hai usko hum return karte hai print nhi krte hai
        

akshata = Human("Akshata",  20)

print(akshata)  # this is a human object, jab bhi hum akshata object ko print krenge toh vo magic function me jo bhi code hai usko execute krega

