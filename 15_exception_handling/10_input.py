# Handling exceptions while taking input 
# A Pitfall while using exception handling

# Handling exceptions while taking input 

# def get_square():
#     try:
#         num = int(input("Enter the number : "))
#         print("Square is :", num**2)
#     except Exception as e:
#         print(e)
#         get_square()

# get_square()




# A Pitfall in exception handling

# -> Exception while file handling

# try :
#     f = open("15_exception_handling/leet-code.txt")
#     my_data = f.read()
#     print(my_data)
# except Exception as e:
#     print(e)
# else:
#     print("read operation success")
# finally:
#     try:
#         f.close()
#     except:
#         pass


# print("rest of code")
