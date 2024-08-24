# Method Overriding -

# isme hum jo parent class hai usme jo method hai uske same name se parent me method banayenge aur usme kuch alg operation krenge but jo method ka name hai vo same hona chahiye toh isase - jo child class me method hogi vo override kregi parent class wali method ko
# jab hum parent class ke method ko same child class me banate hai toh usko method overriding bolte hai.

# class University_Person :  # parent class
#     def __init__(self, n, a) :
#         self.name = n
#         self.age = a
#     def make_attendance(self) :
#         print("Attendance marked as present")
#     def leave_application(self) :
#         print("leave application submitted")

# class Teacher(University_Person):  # child class
#     def upload_test(self) :
#         print("test uploaded")
#     def leave_application(self) :  # ye method parent class wale method ko override kregi
#         print("leave application submitted and waiting for approval")

# class Student(University_Person): # child class 
#     def upload_answer(self) :
#         print("answer uploaded")

# class Clerk(University_Person): # child class 
#     def upload_data(self) :
#         print("data uploaded")


# teacher1 = Teacher("teacher1", 25)

# # teacher1.leave_application()  # leave application submitted and waiting for approval  -> because child class me jo leave_application() wali method hai vo override kr rhi hai parent class me jo leave_application() wali method hai usko


# # student1 = Student("stud1", 20)
# # student1.leave_application()  # leave application submitted




# ****8**********


# super() :- agr hum chahte hai ki parent class wala function bhi run ho jab hum method overiding kr rhe hai tb
# isase hum parent class ko call krte hai
# parent class ke kisi bhi method ko call kr sakte hai child me

class University_Person :  # parent class
    def __init__(self, n, a) :
        self.name = n
        self.age = a
    def make_attendance(self) :
        print("Attendance marked as present")
    def leave_application(self) :
        print("leave application submitted")

class Teacher(University_Person):  # child class
    def __init__(self, n, a, s):
        super().__init__(n, a)
        self.salary = s
    def upload_test(self) :
        print("test uploaded")
    def leave_application(self) :  # ye method parent class wale method ko override kregi
        super().leave_application()  # isase pehle parent class ki jo method hai vo aa jayegi
        print("waiting for approval")

class Student(University_Person): # child class 
    def upload_answer(self) :
        print("answer uploaded")

class Clerk(University_Person): # child class 
    def upload_data(self) :
        print("data uploaded")


teacher1 = Teacher("teacher1", 25, 30000)

teacher1.leave_application()  # leave application submitted
                              # waiting for approval  
print(teacher1.salary)  # 30000





