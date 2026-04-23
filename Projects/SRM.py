# python program to make a student record manager
name = input("Enter student name:") #getting student name from user
roll_no = int(input("Enter roll number:")) #getting roll no from user
s1 = int(input("Enter math marks:")) #getting math marks 
s2 = int(input("Enter sci marks:")) #getting science marks
s3 = int(input("Enter urdu marks:")) #gettin urdu marks
s4 = int(input("Enter eng marks:")) #getting english marks
s5 = int(input("Enter pstd marks:")) #getting pak studies marks
marks = [s1,s2,s3,s4,s5] #storing marks in a list
print(f"Marks{marks}") #printing marks list
new_marks = tuple(marks) #converting marks list into tuple
print(f"Marks{new_marks}") #printing marks tuple
#creating student dictionary
student = {
    "name" : name,
    "roll_no" : roll_no,
    "Maths" : s1,
    "Science": s2,
    "Urdu" : s3,
    "English" : s4,
    "PakStudy": s5
}
marks_set = {s1,s2,s3,s4,s5} #storing marks in a set
print(f"Unique marks:{marks_set}") #printing all unique marks
print("Length of marks set is:",len(marks_set)) #calculating length of marks
total = (s1 + s2 + s3 + s4 + s5) #calculating total marks
max_marks = max(marks_set) #calculating maximum marks
min_marks = min(marks_set) #calculating minimum marks
avg = total / 5 #calculating average marks
print(f"Total marks:{total}") #printing total marks
print(f"Highest marks:{max_marks}") #printing hihhest marks
print(f"Lowest marks:{min_marks}") #printing lowest marks
print(f"Average marks:{avg}") #printing average marks