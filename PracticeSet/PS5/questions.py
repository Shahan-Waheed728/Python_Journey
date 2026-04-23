# # python program to create dictionary of hindi words with their english meaning
# dic = {
#     "Khana" : "Eat",
#     "Sona" : "Sleep",
#     "Bhaagna" : "Run",
#     "Khailna" : "Play",
#     "Rona" : "Cry"
# }
# print(dic,type(dic)) #printing element of dictionary and it's type

# python program to input eight numbers from user and display all the unique numbers once
# n1 = int(input("Enter first number:"))
# n2 = int(input("Enter second number:"))
# n3 = int(input("Enter third number:"))
# n4 = int(input("Enter fourth number:"))
# n5 = int(input("Enter fifth number:"))
# n6 = int(input("Enter sixth number:"))
# n7 = int(input("Enter seventh number:"))
# n8 = int(input("Enter eighth number:"))
# values = {n1,n2,n3,n4,n5,n6,n7,n8} #storing numbers in set , it always returns unique values
# print(f"Unique values in a set are:{values}") #printing unique values

# python program to check same values but different data type in set 
# s = {18,"18"}
# print(s,type(s)) #yes we can have same values with different data type in set

# python program to find the length of set 
# s = set() #defining an empty set
# s.add(20) #storing int value
# s.add(20.0) #storing float value
# s.add("20") #storing str value
# print(len(s)) #it ruturn 2 because 20 and 22.0 are same 

# python program to check the type of s 
# s = {}
# print(type(s)) #it return dic because this is the syntax of defining empty dic 

# python program to create empty dictionary and add four friends favourite language in it.
# languages = {}
# languages.update({"Shahan": "Python"})
# languages.update({"Fahad" : "Java"})
# languages.update({"Talha":"SQL"})
# languages.update({"Huzaifa":"C++"})
# print(languages)

# # python program to checking two same  keys in dictionary
# languages = {}
# languages.update({"Shahan": "Python"})
# languages.update({"Fahad" : "Java"})
# languages.update({"Shahan":"SQL"})
# languages.update({"Huzaifa":"C++"})
# print(languages) #it will print the last updated value of Shahan

# python program to checking two same values in dictionary
# languages = {}
# languages.update({"Shahan": "Python"})
# languages.update({"Fahad" : "Java"})
# languages.update({"Talha":"Python"})
# languages.update({"Huzaifa":"C++"})
# print(languages) #it will print the values as written 

# python program to change the value of list contained in set s 
# s = {8,7,12,"Shahan",[1,2]}
# print(s,type(s)) #it gives error of unhashabe type list

# challenge task
marks = {
    "Ali" : 95,
    "Bilal" : 82,
    "Maria" : 95,
    "Huzaifa" : 87,
    "Tabish" : 70
} #creating dictionary of students marks

print(max(marks.values())) #printing student with highest marks
print(min(marks.values())) #printing student with lowest marks
std_marks = marks.values()
print(std_marks) #printing values of student keys
marks_set = set(std_marks) #converting marks values into set
print(marks_set) #printing set of marks
print(len(marks_set)) #printing total unique marks in set

