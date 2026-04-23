# # python program to make a  class Programmer contianing information of few programmers working at microsoft
# class Programmer:
#     company = "Microsoft" #class attribute
#     def __init__(self,id,name,lang,position,salary,exp):
#         self.id = id
#         self.name = name
#         self.lang = lang
#         self.position = position
#         self.salary = salary
#         self.exp = exp
#     @staticmethod
#     def record():
#         print("----Microsoft Employee Record----")  
# p1 = Programmer(101,"Shahan Waheed","Python","Senior Manager",4500000,7)
# p1.record()
# print(f"Id: {p1.id}\nName: {p1.name}\nLanguage: {p1.lang}\nPosition: {p1.position}\nSalary: {p1.salary}\nExperience: {p1.exp}\nCompany: {p1.company}")
# print()

# p2 = Programmer(102,"Aisha Khalid","Dart","Employee",1500000,4)
# print(f"Id: {p2.id}\nName: {p2.name}\nLanguage: {p2.lang}\nPosition: {p2.position}\nSalary: {p2.salary}\nExperience: {p2.exp}\nCompany: {p2.company}")
# print()

# p3 = Programmer(103,"Huzaifa Khan","Java","Branch Manager",4000000,6)
# print()
# print(f"Id: {p3.id}\nName: {p3.name}\nLanguage: {p3.lang}\nPosition: {p3.position}\nSalary: {p3.salary}\nExperience: {p3.exp}\nCompany: {p3.company}")


# python program to make a class calculator capable of performing operations like square, cube , square root
# class Calculator:
#     def square(self):        
#         num = int(input("Enter number: "))
#         square = num * num
#         print(f"Square of {num} is")
#         return square
#     def cube(self):
#         num = int(input("Enter number: "))
#         cube = num * num * num
#         print(f"Cube of {num} is")
#         return cube
#     def square_root(self):
#         num = int(input("Enter number: "))
#         s_root = num ** 0.5
#         print(f"Square root of {num} is")
#         return s_root
# opr = Calculator()
# print(opr.square())
# print(opr.cube())
# print(opr.square_root())

# python program to change the class attributes with object attributes
# class ClassA:
#     a = "class attribute" #setting class attribute
# c = ClassA()
# c.a = 0 #setting object attribute
# print(c.a)

# python program to add static greet() method in problem2 which print 'hello'
# class Calculator:
#     @staticmethod
#     def greet():
#         print("Hello user!")
#     def square(self):     
#         num = int(input("Enter number: "))
#         square = num * num
#         print(f"Square of {num} is")
#         return square
#     def cube(self):
#         num = int(input("Enter number: "))
#         cube = num * num * num
#         print(f"Cube of {num} is")
#         return cube
#     def square_root(self):
#         num = int(input("Enter number: "))
#         s_root = num ** 0.5
#         print(f"Square root of {num} is")
#         return s_root
# opr = Calculator()
# opr.greet()
# print(opr.square())
# print(opr.cube())
# print(opr.square_root())

# python program to make a class Train which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Pakistan Railways. 
class Train:   
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    def book_ticket(self):
        if(self.seats > 0):
            self.seats -= 1
            print("Ticket booked successfully!")
        else:
            print("Oops, no seat available")            
           
    def get_status(self):       
        print(f"Train= {self.name} \nSeats= {self.seats}")
    def fair(self):        
               
        print(f"Ticket fare=  {self.fare}")
green_line = Train("Green-line",3,4500)
green_line.book_ticket()
green_line.get_status()
green_line.fair()



        




    