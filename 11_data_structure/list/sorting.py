# sorting list 

numbers = [1, 100, 6, 200, 3, 99, 4]

# sort() :- it will sort the list in ascending order
# it will change the original list

# numbers.sort()
# print(numbers)  # [1, 3, 4, 6, 99, 100, 200]




# reverse the list items using sort() -

# numbers.sort(reverse=True)
# print(numbers)  # [200, 100, 99, 6, 4, 3, 1]



# sorted() :-  it will sort the list in ascending order
# but it will not change the original list

# new_list = sorted(numbers)
# print(new_list)  # [1, 3, 4, 6, 99, 100, 200] - sorted list
# print(numbers)   # [1, 100, 6, 200, 3, 99, 4] - original list

# reverse the list items using sorted()-

# new_list = sorted(numbers, reverse=True)
# print(new_list)  # [200, 100, 99, 6, 4, 3, 1]




# sort words in a list

names = ["Akshata", "Surbhi", "Suhani", "Ashwini", "Anjali"]
# names.sort()
# print(names)  # ['Akshata', 'Anjali', 'Ashwini', 'Suhani', 'Surbhi']

# reverse 
names.sort(reverse=True)
# print(names)  # ['Surbhi', 'Suhani', 'Ashwini', 'Anjali', 'Akshata']

