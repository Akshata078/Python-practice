
# for importing module -
# from module-name import function-name

# module name = file name

# from attendance import mark # mark function ko import kiya attendance wale mode se
# from attendance import mark, percentage
# from attendance import *  
# from fees import *

# mark()  # marked
# percentage()  # 75%
# modify()  # modified

# status()  # fees due  -  status wala function attendance aur fees dono module mai available hai but isne fees wala function hai usko call kiya hai, means agr dono module me same function hai toh jo module humne last me import kiya hai, uss module ka function call hoga

# agr hame ek funtion import krna hai toh hum only ussi function ke name se import krenge  - ex.  from attendance import mark

# agr hame ek se jyada function kisi module se import karne hai toh fir ham comma dekr vo function ke name likhenge - ex. from attendance import mark, percentage

# agr hame kisi module me se sare functions ko import krna hai toh asterisk * wala symbol likhenge - ex. from attendance import *
# agr hame kisi module ke sare functions chahiye tbhi hum isko use krenge, agr sare function nhi chahiye toh use nhi krenge because ye good way nhi hota hai



# agr dono module me same function ho =>

# agr dono module me same function hai toh jo module humne last me import kiya hai, uss module ka function call hoga



# agr dono module me same function hai, aur hame dono function ko call karna hai toh =>

# import attendance, fees  # dono module ek satth import ho jayenge, 
# isase hamare dono module import toh jayenge but ye sahi way nhi mana jata, toh isko hum jyada use nhi krenge
# status()  # error - isko batana bhi padta hai ki hum konse module ke function ko call karna chahte hai
# attendance.status()  # present


# another way of importing -
import attendance
import fees

fees.status()  # isme hame batana padta hai ki hum konse module ka function call karna chahte hai.
# attendance.status()  # present




# jab hum koi module banate hai toh vo ek object bann jata hai -
# fees.status()  - isme fees name  ka ek module bann gya aur status() ye uss module ka method hai



# hum  jitne bhi module banayenge jab usko first time run krenge toh vo compile ho jata hai
# aur vo __pycache__ iss name ka folder banayega python aur isme vo chala jayega
# toh jab hum next time run krenge toh vo jo compiled version hai vahi use krega untill and unless hamne uss file me kuch change na kiya ho
# agr hamne code me kuch change kiya hai toh vo firse compile hoga varna compile nhi hoga




# jab hum koi bhi module import krte hai toh python usse kaise dhundhta hai -
# pehle jaha pr humne usse import kiya hai uss folder me dhundhega
# agr uss folder me nhi mila toh fir python usse kahi aur jakar dhundhega
# python kaha dhundhega ye janane ke liye -
# import sys  # sys module import kiya python se

# print(sys.path)  # path ye sys ki ek property hai  






