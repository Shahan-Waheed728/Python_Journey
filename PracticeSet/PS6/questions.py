# # # python program to find the greatest of four numbers entered by the user 
# # n1 = int(input("Entered first number:"))
# # n2 = int(input("Entered second number:"))
# # n3 = int(input("Entered third number:"))
# # n4 = int(input("Entered fourth number:"))
# # if(n1 > n2 and n1 > n3 and n1 > n4):
# #     print(f"{n1} is greater than {n2}, {n3} and {n4}")

# # elif(n2 > n1 and n2 > n3 and n2 > n4):
# #     print(f"{n2} is greater than {n1},{n3} and {n4}")

# # elif(n3 > n1 and n3 > n2 and n3 > n4):
# #     print(f"{n3} is greater than {n1},{n2} and {n4}")

# # else:
# #     print(f"{n4} is greater than {n1},{n2} and {n3}")

# # print("Program ended successfully...")

# # python program to check weather a student pass or fail in exam
# # print("----Student Result Card----")
# # s1 = int(input("Enter math marks:"))
# # s2 = int(input("Enter english marks:"))
# # s3 = int(input("Enter urdu marks:"))
# # total = s1 + s2 +s3
# # per = (total / 300) * 100
# # print(f"Total marks: 300")
# # print(f"Obtained marks:{total}")
# # print(f"Percentage : {per}%")
# # if(per >= 40):
# #     print("Congratulations, You are PASS!")

# # elif(per < 40 and  per >= 33):
# #     print("Promoted in next class!")

# # else:
# #     print("Better luck for next time, FAIL!")

# # print("Program ended successfully...")

# # python prgram to detect spam words
# # comment = "This is the last item remaining, Buy now for free."
# # w1 = "Make alot of money"
# # w2 = "Buy now"
# # w3 = "Subscribe this"
# # w4 = "Click this"
# # if(comment.find(w1) or  comment.find(w2) or comment.find(w3) or comment.find(w4)):
# #     print("Spam comment detected.")
# # else:
# #     print("No spam comment.")

# # python program to check weather a given user name contain less than 10 characters or not 
# # name = "Shahan"
# # len = len(name)
# # if(len > 10):
# #     print("Given user name length is greater than 10 characters.")
# # else:
# #     print("Given user name length is less than 10 characters.")

# # python program to check weather a given name is present in list or not 
# # name_list = ["Shahan","Niha","Zoya","Fahad","Huzaifa"]
# # name = input("Enter your name:")
# # if(name in name_list):
# #     print("You are selected!")
# # else:
# #     print("You are not selected!")

# # python program to calculate the grade of student from his total marks in a subject
# # total = int(input("Enter student marks:"))
# # if(total >= 90 ):
# #     print("Exceptional!")
# # elif(total >= 80 and total < 90 ):
# #     print("Grade : A")
# # elif (total >=70 and total < 80):
# #     print("Grade : B")
# # elif(total >=60 and total < 70):
# #     print("Grade : C")
# # elif (total >=50 and total < 60):
# #     print("Grade : E")
# # else:
# #     print("FAIL")

# # python program to check weather a given letter is talking about Shahan Waheed or not 
# letter = "Congratulation, Shahan Waheed upton completion of chapter 6 practice set. Keep hard working!"
# name = "Shahan"
# if(name in letter):
#     print("Yes, this letter is taking about you.")
# else:
#     print("No, this letter is not about you. ")

#Login and security checker
user_name = input("Enter user name:")
password = input("Enter your password:")
age = int(input("Enter your age"))
if(len(user_name) < 6):
    print("Invalid username length")

elif(len(password) < 8 or "@" not in password):
     print("Weak password")

elif(age < 13):
      print("Access denied (Underage)")      
      print("Login Failed.")    
else:
  print("Login Successful.")
  print(f"Username:{user_name}")
  print(f"Password:{password}")
  print(f"Age:{age}")