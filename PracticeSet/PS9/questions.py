import random

# text = """
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# """
# writing content in file 
# file = open("poem.txt","w")
# file.write(text)
# file.close()

# reading content from poem.txt
# file = open("poem.txt")
# content = file.read()
# print(content)
# if "twinkle" in content:
#     print("Yes, twinkle in present in peom.")
# else:
#     print("No, twinkle is not present in poem.")
# file.close()
# text = "Highest score = 56"
# file = open("Hi-score.txt","w")
# file.write(text)
#---reading old file---
with open("Hi-score.txt") as f: 
 old_score = f.read()
 old_score = int(old_score) if old_score != "" else 0

 print(f"Old highest score = {old_score}")

#   ----game funciton---
def game():
  computer = random.randint(1,50)
  attempts = 0
  new_score = 0

  while(attempts < 5):
    you = int(input("Choose your number:"))
    attempts += 1    
    
    if(computer == you):
     print("Correct")
     print(f"Attempts =  {attempts}")
     if(attempts == 1):
       new_score = 10
     elif(attempts == 2):
       new_score = 8
     elif(attempts == 3):
       new_score = 6
     elif(attempts == 4):
       new_score = 4
     else:
       new_score = 2

     print(f"Score = {new_score}")

     return  new_score
    
    elif(you > computer):
     print("High")

    elif(you < computer):
     print("Low")

    else:
     print("Invalid choice!") 
  print(f"Correct number was = {computer}")
  return 0 

result = game()
print(f"Your score = {result}")

if result > old_score:
 with open("Hi-score.txt",'w') as file:
  file.write(str(result))
  print("New Hi-score updated!")
else:
   print("Hi-score not broken!")

with open("Hi-score.txt") as f:
  print(f"Current Hi-score = {f.read()}")






  










