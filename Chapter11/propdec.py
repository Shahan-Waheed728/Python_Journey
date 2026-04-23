# class Student:
#     # name = "Aisha Khalid"
#     # age = 23

#     @property
#     def name(self):
#         return (f"{self.fname} {self.lname}")
    
#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# s = Student()
# s.name = "Aisha Khalid"
# print(s.fname,s.lname)


# Challenge1
# class Circle:
#     @property
#     def area(self):
#         return (3.14 * 2 * 2)

# c = Circle()
 
# print(c.area)

# Challenge2
# class Student:
#     def __init__(self,age):
#         self.age = age
#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self,value):
#         if(value < 0):
#             raise ValueError("Age can't be less then 0!")
#         self._age = value
    
# a = Student(7)
# print(a.age)

# Challenge3
class Temperature:
    def __init__(self,cel):
         self.cel = cel

    @property
    def fahrenheit(self,cel):
         fah = (cel * 9/5) + 32
         return fah
    
    @fahrenheit.setter
    def fahrenheit(self,temp):         
         self._temp = temp

t = Temperature(35)
print(t.fahrenheit)


         
