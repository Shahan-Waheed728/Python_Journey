# result = {
#     "Shahan Waheed" : 99,
#     "Huzaifa Khan" : 97,
#     "Amina Masood" : 93,
#     "Khadija Bibi" : 90,
#     "Huzaifa Murtaza" : 87
# }
# print(result)
# print(type(result))
# print(result.keys())
# print(result.values())
# result.update({"Shahan Waheed ": 100, "Aneeka" : 67})
# print(result)

# result.pop("Shahan Waheed")
# print(result)
# result.popitem()
# print(result)
# result.clear()
# print(result)

# # Practice Session
# print("--Enter marks here--")
# Math = float(input("Enter marks in maths:"))
# Science = float(input("Enter marks in science:"))
# Urdu = float(input("Enter marks in urdu:"))
# Isl = float(input("Enter marks in isl:"))
# English = float(input("Enter marks in english:"))
# Marks = {
#     "Math" : Math,
#     "Science" : Science,
#     "Urdu" : Urdu,
#     "Isl" : Isl,
#     "English" : English
# }
# print(Marks)
# Sum = sum(Marks.values())
# print("Total Marks:",Sum)
# Average = Sum / 5
# print("Average Marks:",Average)


#Problem 4
a = {"name": "Shahan", "age": 20}
b = {"city": "Lahore", "grade": "A"}
print(a)
print(b)
a.update(b)
print(a)
