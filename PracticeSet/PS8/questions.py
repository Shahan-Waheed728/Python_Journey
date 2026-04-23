# python program to convert Celcius to Fahrenheit
# def conversion(temp):
#     F = 9/5*temp + 32
#     return F
# t = int(input("Enter temperature in degrees:"))
# print(f"{t} °C degrees is equal to = {conversion(t)} °F")

# python program to print sum of first n natural numbers
# def addition(n):
#     if(n <= 0):
#         return 0
#     elif(n == 1):
#         return 1
#     return n + addition(n-1)
# n = int(input("Enter number:"))
# print(f"Sum of {n} natural number is = {addition(n)}")

# python function to print first n line of pattern
# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,n-i+2):
#             print("*",end="")
#         print()
# n = int(input("Enter number :"))
# pattern(n)

# python program to convert inches to cm 
# def conversion(len):
#     cm = len * 2.54
#     return cm
# len = float(input("Enter length:"))
# print(f"{len} inch is equal to {conversion(len)} cm")

# python fuctions to print multiplication table of given number
def table(n):
    for i in range(1,11):     
      print(f"{n} * {i} = {n*i}")
    
n = int(input("Enter number:"))
table(n)

