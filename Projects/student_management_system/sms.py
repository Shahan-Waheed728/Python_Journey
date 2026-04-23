# Project : Student Management System
# Created by: Shahan Waheed
#defining function for adding student
import os
import json
student_record = "student_record.json"
if os.path.exists(student_record):
  with open("sms.json","r") as file:
    students = json.load(file)
else:
  students = []     

def save_file():
  with open(student_record,"w") as file:
    json.dump(students,file,indent=3) 


def Add_Std():
     roll_no = int(input("Enter student roll no:"))
     if(student["roll_no"] == students["roll_no"]):
           print("Student roll_no cannot be same!")
     name = input("Enter student name:")
     grade = int(input("Enter class/grade:"))
     marks = {}
     marks["Math"] = float(input("Enter mathematics marks:")) 
     marks["Eng"] = float(input("Enter english marks:")) 
     marks["Urdu"] = float(input("Enter urdu marks:"))
     marks["Phy"] = float(input("Enter physics marks:")) 
     marks["Chem"] = float(input("Enter chemistry marks:")) 
     marks["Comp"] = float(input("Enter computer marks:"))
     marks["Isl"] = float(input("Enter islamiyat marks:"))
     marks["Sst"] = float(input("Enter social studies marks:"))
     total = 0
     while(marks < len(marks)):
       marks+= total
       print(f"Total marks: {total}")
     percentage = total / 8 * 100
     print(f"Percentage : {percentage}%")
     if(percentage >= 90):
       print("Grade: A+")
     elif(percentage >=80 and total < 90):
       print(f"Grade: A-")
     elif(total >=70 and total < 80):
       print(f"Grade: B")
     elif(total >=60 and total < 70):
       print("Grade: C")
    #  elif(total >=50 and total <):
       print
       
#defining dictionary for student   
     student = {
       "roll_no" : roll_no,
       "name" : name,
       "grade" : grade,
       "marks" : marks
     } 
     students.append(student)
     save_file()
     print(f"Student {name} added successfully!")
   

    
#defining function for viewing student
def View_Std():
       if(len(students) == 0):
         print("No student in record!")
       for student in students:      
         print("----- Student Record -----")
         print("Roll-no:",student["roll_no"])         
         print("Name:",student["name"])    
         print("Class:",student["grade"])  
         print("---Marks in Subjects---")  
         print("Math:",student["marks"]["Math"])    
         print("English:",student["marks"]["Eng"])    
         print("Urdu:",student["marks"]["Urdu"])    
         print("Physics:",student["marks"]["Phy"])    
         print("Chemistry:",student["marks"]["Chem"])    
         print("Computer:",student["marks"]["Comp"])    
         print("Islamiyat:",student["marks"]["Isl"])    
         print("Social-studies:",student["marks"]["Sst"])    


#defining function for searching student 
def Search_Std():
   search = int(input("Enter student roll_no for search:"))
   for student in students:
     if(student["roll_no"] == search):
        print("----- Student Record -----")
        print("Roll-no:",student["roll_no"])
        print("Name:",student["name"])    
        print("Class:",student["grade"])  
        print("---Marks in Subjects---")  
        print("Math:",student["marks"]["Math"])    
        print("English:",student["marks"]["Eng"])    
        print("Urdu:",student["marks"]["Urdu"])    
        print("Physics:",student["marks"]["Phy"])    
        print("Chemistry:",student["marks"]["Chem"])    
        print("Computer:",student["marks"]["Comp"])    
        print("Islamiyat:",student["marks"]["Isl"])    
        print("Social-studies:",student["marks"]["Sst"])  
     else:
      
      print("Student not found!")  

#defining function for updating student record
def Update_Std():
   upd = int(input("Enter student roll-no for marks updation:"))
   sub = input("Enter subject for marks updation:").title()

   for student in students:
     if(student["roll_no"] == upd):
        if sub in student["marks"]:
           new_marks = float(input(f"Enter marks for {sub}: "))
           student["marks"][sub] = new_marks
           save_file()
           print("Marks updated successfully!")
        else:
           print("Invalid input!")
        return 
       
   print("Roll-no not found!")
       
#defining function for deleting student record
def Delete_Std():
   roll_no = int(input("Enter student roll-no for deletion: "))
   for student in students:
     if(student["roll_no"] == roll_no):
       students.remove(student)
       save_file()
       print("Student deleted successfully!")
       return 
   print("Roll-no not found!")

user_choice = 0
while(user_choice != 6):   
    print("------ Student Management System ------")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search Student by roll no")
    print("4. Update Student Marks")
    print("5. Delete Student Record")
    print("6. Exit")
    user_choice = int(input("Select your operation :")) 

    if user_choice == 1 :    
     Add_Std()
    elif user_choice == 2:   
     View_Std()     
    elif user_choice == 3:     
     Search_Std()
    elif user_choice == 4:    
     Update_Std()
    elif user_choice == 5:    
     Delete_Std()
    elif user_choice == 6:
     print("Exiting...")
    else:
     print("Invalid choice , choose numbers only")


