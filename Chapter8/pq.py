# # python program to print hello python 
# def greet():
#     print("Hello Python!")
# greet()

# # python program to print my name and age
# name = "Shahan Waheed"
# age = 22
# def info():
#     print(f"Name : {name} , Age : {age}")
# info()

# # python program to print numbers from 1 to 10
# def num():
#     for i in range(1,11):
#         print(i)
# num()

# python program to take two numbers and print their sum 
# def sum(n1,n2):   
#     sum = (n1 + n2)
#     print(f"Sum of {n1} and {n2} is = {sum}")
# sum(12,12)

# python program to takes a number and prints whether it's even or odd 
# def check(num):
#     if(num % 2 == 0):
#         print(f"{num} is even number")
#     else:
#         print(f"{num} is odd number")
# check(8)
# check(13)

# python program to takes string and prints it's length
# def check(text):
#     length = len(text)
#     print(f"Length of {text} is = {length}")
# check("\'Today is thursday.\'")

# python program to write a default parametrized greeting function
# def welcome(name="Guest"):
#     print(f"Welcome {name}!")
# welcome()
# welcome("Ali")

# python program to calculate power of given number using default parametrized  function
# def power(base,exp=2):
#     res = pow(base,exp)
#     print(f"Result of base {base} power {exp} is = {res}")
# power(5)
# power(3,3)

# python program to calculate discount using default paramterized function
# def discount(price,dis=10):
#     disc = price * (100-dis) / 100
#     print(f"Original price = {price}")
#     print(f"Discount = {dis} %")
#     print(f"Price after discount = {disc}")
# discount(130)
# discount(250,15)

# python program that ruturn square of a number
# def sq(num):
#     return num * num
# res = sq(8)
# print(f"Square is = {res}")
# why it give error when i wirte print(f"Square of {num} is = {res}") ?

# python program that returns max of three number
# def maximum(n1,n2,n3):
#     res = max(n1,n2,n3)
#     return res
# a = maximum(5,14,11)
# print(a)

# python program that returns factorial of a number
# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     return n * factorial(n-1)
# n = int(input("Enter number:"))
# print(f"Factorial of {n} is = {factorial(n)}")