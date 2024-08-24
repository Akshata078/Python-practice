# Excepthook in Python -

# what happens when we didnt handle exception using try and except block ?

# - the interpreter calls sys.excepthook() which is present in sys module, and with three arguments.
# 1. the exception class 
# 2. exception instance/value 
# 3. a traceback object  # object containing the information that what happen internally

# three parameter leta hai, aur excepthook iss unction me pass kr deta hai, aur excepthook inn three things ko print krta hai on output window
# This function prints out a given traceback and exception to sys.stderr

# In an interactive session this happens just before control is returned to the prompt


# inside sys module -

# def excepthook(exc_type, exc_value, exc_traceback):
#     # prints arguments here


# we can customize output by overriding this function 
# sys.excepthook() handles uncaught exceptions.

import sys

def format_traceback(exc_type, exc_value, exc_traceback):
    print("something went wrong !")
    print(exc_traceback)
    print(exc_type)
    print(exc_value)

sys.excepthook = format_traceback

def display():
    print(1+"hello")


display()






