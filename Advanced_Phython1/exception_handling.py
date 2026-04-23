try:
   num1 = int(input("Enter first number:"))
   num2 = int(input("Enter second number:"))
   res = num1 / num2
   print(res)
except ZeroDivisionError:
   print("You can't divide any number by zero.")
# except TypeError:
#    print("Invalid input!")   
except ValueError:
   print("Invalid input!")       