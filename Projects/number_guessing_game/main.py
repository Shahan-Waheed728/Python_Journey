import random 
def play():
      
   attempts = 0 
   user = 0

   level = input("Choose difficulty level (easy,medium or hard): ").lower()

   if(level == "easy"):
     max_num = 50
     max_attempts = 5
   elif(level == "medium"):
     max_num = 100
     max_attempts = 10
   elif(level == "hard"):
     max_num = 200
     max_attempts = 15
   else:
       print("Invalid choice!")
       return 

   computer = random.randint(1,max_num) 

   print(f"Guess the number between 1 and {max_num}")

   print(f"You have {max_attempts} attempts!")

   while(attempts < max_attempts):
    user = int(input("Enter your guess :"))
    attempts += 1
    difference = abs(user - computer)

    if(computer == user):
         print("Correct")
         print(f"Total attempts = {attempts}")
         break   
    elif(difference <= 5):
      print("Very close")
    elif(difference <= 10):
      print("Close")      
    elif(user > computer):
         print("Too High")
    elif(user < computer):
         print("Too Low")
   else:
         print("Game over!")
         print(f"The correct number was {computer}")
         
while True:
     play()
     again = input("Do you want to play again ? (y/n):").lower()
     if(again != "y"):         
          print("Thanks for playing")
          break
        