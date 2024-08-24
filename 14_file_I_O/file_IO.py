# File I/O in Python - Python can be used to perform operations on a file. (read & write data)


# Types of all files -
# 1. Text files : .txt, .docx, .log, etc
# 2. Binary files : .mp4, .mov, .png, .jpeg, etc


# Operations on files -

# Open, read & close file =>
# We have to open a file before reading or writing.

# f = open("14_file_I_O/demo.txt", "r")  # open a file

# file _name :- ex. sample.txt or demo.docs
# mode :- r = read mode (by default)
#         w = write mode

# data = f.read()  # reads entire file  # ye hame hamare file ka pura data de dega in the form of string
# print(data)  # I am learning Python.
# print(type(data))  # str
# f.close()  # close the file



# modes -

# 'r' -> open for reading (defaulot)
# 'w' -> open for writing, ye override krega means jo hamare file ka purana data hai usko delete keraga then uske baad hum uss file me  jo likhna chahte hai vo likha jayega
# 'x' -> create a new file & open it for writing
# 'a' -> open for writing, appending to the end of the file if it exists
# 'b' -> binary mode
# 't' -> text mode (default)
# '+' -> open a disk file for updating (reading and writing) [do operations ko agr ek sath krna hai toh, r+ => file ke andar read bhi karna hai aur write bhi krna hai, w+ => file ke andar white bhi karna hai aur read bhi krna hai]
# 'r+' -> we can read and override the existing data (pointer at starting)  [no truncate]
# 'w+' -> we can read and override the existing data (pointer at starting)  [truncate - ye override krega means jo hamare file ka purana data hai usko delete keraga then uske baad hum uss file me  jo likhna chahte hai vo likha jayega]
# 'a+' -> we can read and append (pointer at end)  [no truncate]


# Reading a file -
# data = f.read(5)  # I am (read ke andar 5 likha hai it means only five character hi read krega) 
# print(data)

# # reads one line at a time => readline() 
# line1 = f.readline()  # read first line
# print(line1)  # jab hum line1 ko print kr rhe hai toh next line me space aa rha hai because hamare file me next line di hai hamne, next line ke liye by default \n hota hai jo hame dikhayi nhi deta hai.  next line me blank space aa rha hai because of \n

# line2 = f.readline()  # read second line
# print(line2)

# line3 = f.readline()  # read third line
# print(line3)

# agr ham pura data pehle hi read kr rhe hai toh readline ke andar jab hum print krenge toh only blank spaces aayenge because jo data tha  vo hamne pehle hi read kr liya hai toh readline ke pass kuch bachega hi nhi only nex line bachegi tbhi vo blank spaces print krega 




# writing to a file =>

# f = open("14_file_I_O/demo.txt", "w") 
# data = f.write("this is a new line")  # overwrites the entire file



# f = open("14_file_I_O/demo.txt", "a") 
# data2 = f.write("\nThis is a new line")  # adds to the file



# agr hame koi file create krni hai toh =>

# f = open("14_file_I_O/sample.txt", "a")  # a ki jagah pr w likhenge toh bhi file create ho jayegi
# f.close()





# with syntax -

# with ka use krte hai tb vo hamari file ko automatically close kr deta hai

# with open("14_file_I_O/demo.txt", "a") as f:
#     data = f.read()



# deleting a file -

# we can delete a file by using - os module  (os - operating system)
# module - module(like a code library) is a file written by another programmer that generally has a functions we can use.

# import os
# os.remove(filename)





# ********************

with open("14_file_I_O/practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing Java.\nlike programming in Java")

# replace all occurences of "Java" with "python" in above file -

with open("14_file_I_O/practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
# print(new_data)

with open("14_file_I_O/practice.txt", "w") as f:
    f.write(new_data)



# search if the word "learning" exists in the file or not -

def check_for_word():
    word = "learning"
    with open("14_file_I_O/practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")

# check_for_word()


# find in which line of the file does the word "learning" occur first. print -1 if word not found -

def check_for_line():
    word = "pyq"
    data = True
    line_no = 1
    with open("14_file_I_O/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1
    return -1

# print(check_for_line())


