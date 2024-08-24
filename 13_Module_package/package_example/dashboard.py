
# package ke module ko kaise import krenge =>
# import packageName.moduleName

# import student.fee
# import student.atten


# agr kisi module ke function ko use krna hai call karna hai toh =>
# packageName.moduleName.functionName()

# student.fee.status()  # fees due
# student.atten.status()  # present




# another method for importing -

from student.fee import status
status()  # fees due



# agr pure module ko import krna hai toh - 

# from student import fee

# fee.status()  # fees due



# agr koi subpackage import karna ho =>
# import packageName.subPackageName.moduleName



# academic name ka sub-package import karna hai =>

import student.academic.homework

student.academic.homework.hw()  # homework




# alias -

import student.academic.exam as e

e.exam()  # exam

# isme hum baar baar student.academic.exam ye reapeat kr rhe hai .
# toh harr bar itna likhne ki jagah pr hum isko koi dusra name dete hai =>  as new_name

# use - 1. jab hamara name bohot lamba ho jata hai
#     - 2. jab do ya isase jyada module me same function ko call kr rhe hote hai 
# (jaha pr naming conflict ho rha hota hai vha pr use krte hai)