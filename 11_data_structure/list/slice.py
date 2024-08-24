# slice() :- extracts a part of a list

# syntax -
# list_name[starting_index : ending_index]
# isme stating_index se slice hona start hoga aur ending_index tk jayega but ending_index wale item ko include nhi krega
# slice hamare original list ko change nhi krta hai

names = ["Akshata", "Shweta", "Payal", "Aachal"]
new_names = names[0 : 2]  # in this, it will start from index 0 and goes upto index 2 but it will not include index 2

# print(new_names)  # ['Akshata', 'Shweta']
# print(names)  # ['Akshata', 'Shweta', 'Payal', 'Aachal']



new_list = names[ : 2] # isme humne starting index nhi diya iska matlab vo 0 index se start hoga.

# print(new_list)  # ['Akshata', 'Shweta']

end_list = names[2 :] # isme ending index nhi diya hai iska matlab vo index 2 se start hoga aur last tk jayega

# print(end_list)  # ['Payal', 'Aachal']

new_names_list = names[ : ]  # isme humne starting aur ending index dono nhi diya hai mtlb ye 0 index se start hoga aur puri list ki jitni length hai vaha tk jayega. means isme puri list as it is print hogi

# print(new_names_list)


minus_end = names[1 : -2]  # isme index 1 se start hoga aur ending index -2 hai iska matlab end se 2nd item aur vo hai Payal name toh ye isko include nhi hoga.
# - minus hoga toh end se lega

# print(minus_end)  # ['Shweta']


two_colon_list = names[0 : 4 : 3]  # it means ye 0 index se start hoga, index 4 tk jayega aur 3 index pr jump krega matlab jo item hoga uske 3rd index pr jump krega direct
# jo colon ke baad last wala digit hota hai vo increment ke liye hota hai. ye batata hai ki kitna increment karna hai, aur ye by default 1 hota hai

# print(two_colon_list)  # ['Akshata', 'Aachal']


leave_one_item = names[::2]  # this will start from index 0 and leave one item then print item at index 2, like this.

# print(leave_one_item)  # ['Akshata', 'Payal']


reverse_list = names[::-1] # it means -1 se start kro mtlb reverse order me print hoga list
# print(reverse_list)  # ['Aachal', 'Payal', 'Shweta', 'Akshata']