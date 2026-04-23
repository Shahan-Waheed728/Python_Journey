# # python program to make a list of fruits entered by user 
# f1 = input("Enter first fruit: ")
# f2 = input("Enter second fruit: ")
# f3 = input("Enter third fruit: ")
# f4 = input("Enter fourth fruit: ")
# f5 = input("Enter fifth fruit: ")
# f6 = input("Enter sixth fruit: ")
# f7 = input("Enter seventh fruit:")
# fruits = [f1,f2,f3,f4,f5,f6,f7]
# print(fruits," ")

# python program to accepts marks of six student and place them in a sorted manner
# s1 = int(input("Enter student1 marks: "))
# s2 = int(input("Enter student2 marks: "))
# s3 = int(input("Enter student3 marks: "))
# s4 = int(input("Enter student4 marks: "))
# s5 = int(input("Enter student5 marks: "))
# s6 = int(input("Enter student6 marks: "))
# student_marks = [s1,s2,s3,s4,s5,s6]
# student_marks.sort()
# print(f"Students Marks:{student_marks}")

# python program to check that tuple type cannot change in python 
# lang = ("python","java","c++","c#","html","css","js")
# print(lang)
# print(type(lang))


# python program to sum of list with four numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))
# numbers = [num1,num2,num3,num4]
# sum = num1 + num2 + num3 + num4
# print(f"Sum of numbers is: {sum}")

# python program to count number of zeros in given tuple 
# a = (7,0,8,0,0,9)
# res = a.count(0)
# print(f"Number of 0s in a is: {res}")

# challenge task
n1 = int(input("Enter first num: ")) #getting first number from user
n2 = int(input("Enter second num: ")) #getting second number from user
n3 = int(input("Enter third num: ")) #getting third number from user
n4 = int(input("Enter fourth num: ")) #getting fourth number from user
n5 = int(input("Enter fifth num: ")) #getting fifth number from user
numbers = [n1,n2,n3,n4,n5] #storing number in list
print(f"Inital List : {numbers}") #printing elements of list
change = tuple(numbers) #changing list to tuple
print(f"New tuple: {change}")
print(max(change))#printing max number from tuple
print(min(change)) #printing min number from tuple
sum = n1 + n2 + n3 + n4 + n5 #calculating sum of numbers
print(f"Sum of numbers is : {sum}") #printing sum of numbers
count_num = int(input("Enter number you want to count from tuple : "))
print(change.count(count_num)) #printing the count of number entered by user
ch = int(input("Enter number you want to replace with zero : "))
print(change.replace(0,ch)) #updated list
change2 = list(change) #changing tuple to list
print(f"Updated tuple : {change2}")