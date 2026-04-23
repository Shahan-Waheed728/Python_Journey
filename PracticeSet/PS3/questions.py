# python program to display name entered by user followed by Good afternoon
# name = input("Enter your name:")
# print("Good afternoon Mr.",name,"!")

# python program to fill the letter by name and date
# letter = """Dear <|Name|>,
# You are selected!
# # <|Date|>
# # """
# letter = (letter.replace("<|Name|>","Shahan Waheed"))
# letter = (letter.replace("<|Date|>","9-1-2026"))
# print(letter)

# text = "The quick  brown fox jumps over the lazy dog."
# print(text.find("  ")); #this prints the double space in a string which is at 9th index between quick and brown
# print(text) #string before replac double space with single space
# rep = (text.replace("  "," ")) #replace double space with single space
# print(rep) #string after replacing

# python program to format the letter
# letter = "\"Dear Harry!\n this python course is nice.\nthanks!\""
# print(letter)

# challenge task
text = input("Enter your favourite sentence:")
print(text) #printing user entered string
length = len(text) #finding length of text
print(f"Total characters in text:{length}") #printing length of text
spaces = text.count(" ") #count space in text
print(f"Total number of spaces {spaces}") #printing total number of space
test = text.find("python") #finding the words python
print(f"Text contains the word python? {test}") #printing index of python
text = text.replace("a","*")  #replace a with *
text = text.replace("e","*")  #replace e with *
text = text.replace("i","*")  #replace i with *
text = text.replace("o","*")  #replace o with *
text = text.replace("u","*")  #replace u with *
print(f"Updated text {text}") #printing final text