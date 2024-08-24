# finding something in the list

languages = ["html", "css", "js", "css", "react js" ]

# if "css" in languages:
#     print("Yes")
# else:
#     print("No")



# index() :- it will gives us the index number of the item in a list (first occurence wala index number dega agr item repeat ho rha hai toh.)

# print(languages.index("css"))   # 1

# agr hum index() function ka use kr rhe hai aur vo particular item hamare list me present nhi hai toh ye hame error dega.




# count() :- koi item list me kitni baar aa rha hai ya kitni baar occur ho rha hai vo batayega

# print(languages.count("css"))  # 2
# print(languages.count("html"))  # 1
print(languages.count("python"))  # 0 - because python is not present in the list