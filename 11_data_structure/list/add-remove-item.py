# Adding and Removing Item in List

names = ["Akshata", "Vaishnavi", "Surbhi"]

# append() :- It will add item to the last in the list and it will change the original list

# names.append("Ananya")
# print(names)  # ['Akshata', 'Vaishnavi', 'Surbhi', 'Ananya']


# insert() :- if we want to add a item at specific position in a list, insert item in a list at specific position
# iske andr hum do values likhte hai - first : kis index pr hum insert karna chahate hai, second : what or which item we want to insert

# names.insert(0, "Akshu")
# print(names)  # ['Akshu', 'Akshata', 'Vaishnavi', 'Surbhi']

# names.insert(1, "Janhavi")
# print(names)  # ['Akshata', 'Janhavi', 'Vaishnavi', 'Surbhi']



# pop() :- it will remove the item from the last

# names.pop()
# print(names)  # ['Akshata', 'Vaishnavi']


# agr hame kisi specific index number ka item delete krna ho toh - iske liye hum pop() ke parenthesis ke andar jiss bhi index number se item remove karna hai vo index number likhenge -

# names.pop(1)  # index number 1 pr jo bhi item hoga vo remove ho jayega
# print(names)  # ['Akshata', 'Surbhi']



# remove() :- we can remove a item in the list by the name of the item
# if we want to delete the item by its name

languages = ["html", "css", "javascript", "react js", "jQuery"]
# languages.remove("jQuery")
# print(languages)  # ['html', 'css', 'javascript', 'react js']

# agr koi item repeate ho rha hai list me aur hum usko remove() method se delete kr rhe hai toh, jo first time item aayega vhi delete hoga list se, baki nhi honge -
phone = ["iphone", "apple", "realme", "iphone", "techno"]
# phone.remove("iphone")
# print(phone) # ['apple', 'realme', 'iphone', 'techno']




# del :- we can remove a item by its index number, also we can delete more than one item in a list

# del phone[3]  # index 3 pr jo bhi item hoga vo delete ho jayega
# print(phone)  # ['iphone', 'apple', 'realme', 'techno']

# del phone[1 : 4]  # pehle phone wale list ko slice kiya then delete kr rhe hai.
# print(phone)  # ['iphone', 'techno']


# clear() :- it will delete the all items in the list

# phone.clear() # it will delete all the items in the phone list and gives empty list as output
# print(phone)  # []