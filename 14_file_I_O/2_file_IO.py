# file I/O :-

# volatile : jispr data persist nhi krta hai (RAM me data store hota hai, jo temorary hota hai. agr hum hamari system firse restart krenge toh vo jo data tha hamara vo delete ho jayega automatically)
# vo memory jisme temporarily program run hote hai 

# non volatile : data ko store krne ke liye hum hamare data ko file me likhenge


# two types of files - 
#  1. Text files : .txt, .docx, .log, etc
#  2. Binary files : .mp4, .mov, .png, .jpeg, etc

# open() - ye python me ek built in function hai jo files ko open krne ke liye kaam aata hai.
# ye two parameters leta hai - 1. filename  2. mode
# by default mode - 'r' (i.e. read)

# read() - files ko read krne ke kaam aata hai
# close() - file ko close krne ke liye


# readline() - ek ek krke hamare file ki lines ko read krta hai.
# readlines() - ye hame lines ki list return krta hai. 



# mode -

# 1. 'r' - open for writing
# 2. 'w' - open for writing
# 3. 'a' - open for appending (end me kuch jodna chahte hai)
# 4. '+' - for update
# 5. 'rb' - read in binary 
# 6. 'rt' - read in text  (default)


# with statement - 

# isme file automatically close ho jayegi

# ex. - with open("14_file_I_O/practice.txt", "r") as f:



# ********<- Practice Que -> ***********

# 1. write a program to read the text from a given file "poems.txt" and find out whether it contains the word Twinkle

# def check_word():
#     with open("14_file_I_O/poems.txt") as f:
#         data = f.read()
#         if "Twinkle" in data:
#             print("word found")
#         else:
#             print("word not found")
# check_word()


# 2. the game() function a program lets a user play a game and returns the score as integer. you need to read a file "high_score.txt" which is either blank or contains the privious high-score.
# you need to write a program to update the high-score whether the game() function breaks the high-score
# game name - random number generator 

# import random

# def game():
#     print("You are playing the game...")
#     score = random.randint(1, 50)  # it will give the random number between 1 and 50
#     with open("14_file_I_O/highscore.txt") as f:
#         high_score = f.read()
#         if high_score != "":
#             high_score = int(high_score)
#         else :
#             high_score = 0

#     print(f"your score is : {score}")

#     if score > high_score:
#         with open("14_file_I_O/highscore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()




# 3. write a program to generate multiplication table from 1 to 10, and write it to the different files. place this files in a folder for 13-year old

# def generate_table(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} * {i} = {n * i}\n"

#         # print(type(table))
#     with open(f"14_file_I_O/table/table_{n}", "w") as f:
#         f.write(table)

# for i in range(1, 11) :
#     generate_table(i)




# 4. replace "," to "." in demo.txt -


# with open("14_file_I_O/demo.txt") as f:
#     data = f.read()
        
# new_data = data.replace(",", ".")
# # print(new_data)

# with open("14_file_I_O/demo.txt", "w") as f:
#     f.write(new_data)





# 5. make a copy of file demo.txt in demo2.txt-

with open("14_file_I_O/demo.txt") as f:
    content = f.read()

with open("14_file_I_O/demo2.txt", "w") as f:
    f.write(content)