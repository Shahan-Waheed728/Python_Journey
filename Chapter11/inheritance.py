# class Person():
#     def __init__(self,name,age):
#       self.name = name
#       self.age = age
#     def display_info(self):
#         print(f"Name: {self.name} \nAge: {self.age}")
        
# class Student(Person):
#     def __init__(self,name,age,reg_no,semester,cgpa):
#       super.__init__(name,age)
#       self.reg_no = reg_no
#       self.semester = semester
#       self.cgpa = cgpa
#     def stdInfo(self):
#         print(f"Reg-no: {self.reg_no}\nSemester: {self.semester}\nCGPA: {self.cgpa}")

# p1 = Person()
# p1.display_info("Shahan Waheed",22) #this return name and age of person
# p2 = Student("Shahan Waheed",22,"SP23-BSE-006",7,3.14)
# p2.display_info() #this return name and age of Person
# p2.stdInfo()  #this return name,age, reg_no , semester and cgpa of student


# class Employee():
#     name = "Ali Raza"
#     salary = 450000
#     def show_details(self):
#         print(f"Name= {self.name} , Salary= {self.salary}")
# class Manager(Employee):
#     department = "HR"    
#     def dep(self):
#         super().__init__()
#         print(f"Department= {self.department}")

# e1 = Manager()
# print(e1.show_details())
# print(e1.dep())

# super() is better in case of when we have multiple classes and have more methods which take 
# very long time to write, if we manually     copy paste it and then change , we will change in 
# evry place, by using constructor we can easily handle mehtods and change is easy.

# multilevel inheritance

# class Animal:
#     def eat(self):
#         print("All animals eat.")
# class Dog(Animal):
#     def bark(self):
#         print("All dogs bark.")
# class Puppy(Dog):
#     def play(self):
#         print("Puppy is playing with ball.")
# o = Puppy()
# print(o.eat(),o.bark(),o.play())

# multiple inheritance
# class Camera():
#     def take_photo(self):
#         print("Camera is used to take picture.")
# class Phone():
#     def call(self):
#         print("Phone is used for calls.")
# class SmartPhone(Camera,Phone):
#     pass
# o = SmartPhone()
# o.take_photo()
# o.call()

