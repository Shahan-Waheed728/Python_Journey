# object and class in python 
# print("---Student Result 2026---")
class Student:
    def __init__(self,name,grade,marks,status):
        self.name = name 
        self.grade = grade
        self.marks = marks
        self.status = status
        
    # name = "Shahan Waheed" class attribute
    grade = 9
    # marks = 98
    @staticmethod
    def record():
        print(f"---Annual Result 2026---")
std1 = Student("Ali Hassan",9,96,"Pass")
# std1.name = "Ali Hassan"
# std1.marks = 96
std1.record()
print(f"Name: {std1.name}\nClass:{std1.grade}\nMarks: {std1.marks}\nStatus: {std1.status}")
print()

std2 = Student("Aisha Khalid",9, 86,"Pass")
# std2.name = "Amna Zaidi" #instance attribute
# std2.marks = 87
std2.record()
print(f"Name: {std2.name}\nClass: {std2.grade} \nMarks: {std2.marks}\nStatus: {std2.status}")
print()

std3 = Student("Hamza Mir",9,32,"Fail")
std3.record()
print(f"Name:{std3.name}\nClass: {std3.grade}\nMarks: {std3.marks}\nStatus: {std3.status}")
    