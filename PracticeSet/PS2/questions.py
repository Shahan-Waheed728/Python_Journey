# python program to add two number
# way 1
# a = 6;
# b = 5;
# print("The sum of a and b is: ", a + b);
# way 2
# a = int(input("Enter the first number :"));
# b = int(input("Enter the second number:"));
# c = a + b;
# print("Sum of a and b is :",c)

# python program for finding a remainder when number is divided by z
# x = 7 #the first number
# z = 3 #the second number
# y = x % z; #will give the remainder of x
# print("Remainder :",y) # printing the remainder of x

# python program for checking the type of variable using input function
# name = input("Enter your name here:")
# age = int(input("Enter your age:"))
# perc = float(input("Enter your percentage:"))
# print("My name is ",name,"and i am ",age,"years old. I get ",perc,"% marks in final exam.")
# print(type(name))
# print(type(age))
# print(type(perc))

#python program to check a is greater then b or not using comparison operator
# a = 34
# b = 80
# c = a > b #storing the result of a > b either True or False
# print("a is greater then b ?",c)

#python program to find the average of two numbers entered by user
# num1 = int(input("Enter number 1:")) #storing first number
# num2 = int(input("Enter number 2:")) #storing second number
# res = ((num1 + num2) / 2) #storing average number
# print("Average of num1 and num2 is:",res)

# python program to calculate the square of a number entered by the user 
# num = int(input("Enter number:")) #storing a number given by user
# sqr = num * num #storing a square of given number
# print("Square of",num,"is:",sqr) #printing a square of given number

# challenge task
num1 = int(input("Enter first number:")) #storing first number
num2 = int(input("Enter second number")) #storing second number
total = num1 + num2 #storing sum of two numbers
diff = num1 - num2 #storing difference of two numbers
prod = num1 * num2 #storing product of two numbers
# div = num1 / num2 #storing division of two numbers
avg = ((num1 + num2) /2 ) #storing average of two numbers
print("Sum of ",num1,"and",num2,"is:",total) #printing the sum of two numbers
print("Difference of ",num1,"and",num2,"is:",diff) #printing the difference of two numbers
print("Product of ",num1,"and",num2,"is:",prod) #printing the product of two numbers
# print("Division of ",num1,"and",num2,"is:",div) #printing the division of two numbers
print("Average of ",num1,"and",num2,"is:",avg) #printing the average of two numbers
print("Type of sum is:",type(total))
print("Type of diff is:",type(diff))
print("Type of prod is:",type(prod))
print("Type of avg is:",type(avg))