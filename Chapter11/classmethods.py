class Student:
    name = "Ali Raza"
    age = 22
    @classmethod
    def show_record(cls):
        print(f"Student name = {cls.name}\nAge = {cls.age}")
    print("")

s1 = Student()
s1.name = "Basit Shah"
s1.age = 19
print(s1.name, s1.age)
s1.show_record()