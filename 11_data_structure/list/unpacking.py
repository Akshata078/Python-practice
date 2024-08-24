# list unpacking :-

# list unpacking means ye list ke harr ek item ko ek individual variable me store ya save krega
# agr hum chahte hai ki hamare list ke item alg alg variable me assign ho jaye


# ex.
products = ["Pen", "Pencil", "Notebook"]
first, second, third = products  # products is name of the list

# print(first)  # Pen
# print(second)  # Pencil
# print(third)  # Notebook


# isme hame jitne items hai utne hi variable ke name dene padenge

# agr hamari list bohot badi hai aur hame only some part uska unpack krna hai toh pehle hum list ko slice krenge then usko unpack krenge
first, second = products[0 : 2]

# print(first)  # Pen
# print(second)  # Pencil


# agr hame jo sare names hai vo alag alag variable me store krna ho aur jo numbers hai unko ek list me store karna hai
names = ["Akshata", "Vaishnavi", "Surbhi", 1, 2, 3, 4]
first, second, third, *list2 = names  # isme na pehle first me Akshata chala jayega, then second me Vaishnavi aur third me Surbhi, fir uske baad usko asterisk* wala symbol milega toh python samz jayega ki iske aage ke jitne bh items hai unko ek list me daal do, toh list2 iss variable me baki sare numbers store ho jayege list me.

# print(first)   # Akshata
# print(second)  # Vaishnavi
# print(third)  # Surbhi
# print(list2)  # [1, 2, 3, 4]


items = ["Akshata", "Surbhi", 1, 2, 3, 4, "India", "YouTube"]
first, second, *list3, fourth, fifth = items  # isme Akshata first me jayega then surbi second variable me jayega, fir usko asterisk wala symbol dikhega toh vo check krega ki iske baad koi next variable toh nhi hai na, agr nhi hai toh vo baad ki sari values list me daal dega, aur agr hai toh fir vo last wala variable lega aur usme list ka jo last item hai vo daal dega, fir last se 2nd lega....... iske baad jo bhi items bachege usko list me store kr dega

# print(first)   # Akshata
# print(second)  #  Surbhi
# print(list3)   # [1, 2, 3, 4]
# print(fourth)  # India
# print(fifth)   # YouTube