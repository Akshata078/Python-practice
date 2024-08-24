# Inheritance -

# how can we inherit - jo bhi class me hame dusra class inherit karna hoga uss class name ke samne hum parenthesis ke andar jiss class ko inherit karna hai uska name likhenge
# jo class dusre class ko inherit kr rha hai vo child class hoga aur jo class inherit ho rha hai dusre class me vo parent class hoga.
# jab child class parent class ko inherit karta hai toh parent class ki sari properties sare methods child ke pass aa jate hai aur hum unko child class me use kr sakte hai.


class University_Person :  # parent class
    def __init__(self, n, a) :
        self.name = n
        self.age = a
    def make_attendance(self) :
        print("Attendance marked as present")
    def leave_application(self) :
        print("leave application submitted")

class Teacher(University_Person):  # child class - Teacher class inherit kr rha hai University_Person iss class ko
    def upload_test(self) :
        print("test uploaded")

class Student(University_Person): # child class - Student class inherit kr rha hai University_Person iss class ko
    def upload_answer(self) :
        print("answer uploaded")

class Clerk(University_Person): # child class - Clerk class inherit kr rha hai University_Person iss class ko
    def upload_data(self) :
        print("data uploaded")


teacher1 = Teacher("teacher1", 25) # teacher1 ye ek object create ho jayega

# teacher1.make_attendance()  # Attendance marked as present (isme make_attendance ye University_Person iss class ka method hai isko hum Teacher wale object me access kr pa rhe hai)


# student1 = Student("akshata", 20)
# student1.leave_application()  # leave application submitted
# print(student1.name, student1.age)  # akshata 20




# class Car:
#     def __init__(self,name,color) :
#         self.car_name = name 
#         self.car_color = color 
#     def car_func(self):
#         print("transportation")

# class Mahindra(Car):
#     def speed(self):
#         print("30km/hr")

# mahindra = Mahindra("mahindra","red")
# print(mahindra.car_color)
# mahindra.car_func()
