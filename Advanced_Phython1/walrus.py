# # simple operation
# n = 3
# list = [1,2,3,4,5,6]
# if(len(list) >= n):
#     print("List can't store more then three items.")

# using walrus operator
# if( n := len([1,2,3,4,5,6]) >= 3):
#     print("List can't store more then three items.")

# if len(name := input("Enter your name: ")) > 5:
#     print("Long name!")

if (length := len(input("Enter your name: "))) > 5:
    print("Long name!")

