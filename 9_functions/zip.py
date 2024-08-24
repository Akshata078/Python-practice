# zip function :-

# The zip function returns a zip object which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together
# if the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator
# isme dono list jisko hum combine kr rhe hai ek list me tuple me toh dono list ki length same honi chahiye, nhi toh hamara data lost ho sakta hai isme


names = ["Shreya", "Puja", "Gauri"]
marks = [78, 98, 87]

students = zip(names, marks)  # this will return a zip object, 
students_list = list(students)
print(students_list)  # [('Shreya', 78), ('Puja', 98), ('Gauri', 87)]



