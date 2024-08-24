#Encapsulation

# private attribute :-

# if we want that our attribute should not access outside the class
# kisi bhi attribute ke aage do underscore lagayenge toh vo private attribute bann jayega


class Human :
    def __init__(self, f,  age_val) :
        self.first_name = f
        self.__age = age_val  # private attribute

        # print(self.__age)  # 20 - we can access private attribute inside the class

    def access_age(self) :
        print(self.__age)  # 20 # this is also inside the class so we can access


akshata = Human("Akshata",  20)

# print(akshata.__age)   # cannot access outside the class because __age is private attribute

# we can access private variable outside the class by using one trick =>
# print(akshata._Human__age)   # 20



# akshata.access_age()  # 20
