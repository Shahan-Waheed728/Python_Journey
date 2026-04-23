# python program to print a table of given number using for loop
# n = int(input("Enter number for table: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")

# python program to greet all the persons stored in a list whose name starts with S
# name = ["Shahan","Bilal","Niha","Shazaib","Saqib"]
# for n in name:
#     if("S" in n):
#         print(f"Good morning {n}!")

# python program to print table of given number using while loop 
# n = int(input("Enter number for table:"))
# i = 1
# while(i < 11):
#     print(f"{n} * {i} = {n * i}")
#     i += 1

# n = int(input("Enter number:"))
# if(n <= 1):
#     print(f"Given number {n} is not a prime number")
# else:
#     for i in range(2,n):
#        if (n % i == 0):
#         print("Given number {n} is not a prime number")
#         break   
#     else:
#        print("Given number {n} is a prime number")

# n = int(input("Enter number for sum:"))
# i = 1
# sum = 0
# while( i <= n):
#   sum+=i 
#   i+=1
# print(sum)

# python program to calculate factorial of given number using for loop
# n = int(input("Enter number for factorial:"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"Facototial of {n} is = {fact}")

# python program to print the given start pattern
# n = 3
# for i in range(1,n+1):
#     for s in range(n-i): 
#        print(" ", end="")      
#     for j in range(2*i-1):
#        print("*",end="")
#     print()

# python program to print a table of given number in reverse order
# n = int(input("Enter number for table:"))
# i = 10
# while(i >=1):
#     print(f"{n} * {i} = {n*i}")
#     i-=1

# n = 10
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()   

n = 10
for i in range(1,n+1):
    for j in range(i-1,10):
        print(j,end="")
    print()