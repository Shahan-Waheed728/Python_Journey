import os
# def donkey(): 
#  text = """
#   donkey derby
#   there was a little donkey he was very small
#   when stood by others they looked rather tall
#   he had a big ambition to win a donkey race
#   a derby for the donkeys he could win first place
#   he put down his name at the local donkey show'
#   in the donkey derby he could have a go
#   he took it nice and easy till halfway through the race
#   then towards the finish at his fasted pace
#   the little donkey won his dream it had come true
#   to win the donkey derby just like he dreamed to do 
#   """

 
#  word = "donkey"
#  if word in text:
#     text = text.replace(word,"#####")
#     print(text)
#  else:
#     print("The word \'donkey\' is not present in give text")
#  return text
# text = donkey()
# with open("donkey.txt","w") as file:
#     file.write(text)


# python program to replace list of words with ##### that censor
def problem5():
    text="""
I Want To Be Like You

Thank you, teacher,
for being my life's role model.
When I consider all you've taught me
and reflect on the kind of person you are,
I want to be like you—
smart, interesting and engaging,
positive, confident, yet unpretentious.
I want to be like you—
well-informed and easy to understand,
thinking with your heart as well as your head,
gently nudging us to do our best,
with sensitivity and insight.
I want to be like you—
giving your time, energy and talent
to ensure the brightest possible future
for each of us.
Thank you, teacher
For giving me a goal to shoot for:
I want to be like you!

"""
    words_list = ["I","you","my","me","our"]
    for word in words_list:
     text = text.replace(word,"#####")
    
     return text
text = problem5()
with open("teacher_poem.txt","w") as file:
  file.write(text)

with open("teacher_poem.txt","r") as file:
  file.read()
if "sensitivity" in text:
    print("Yes, the file containes the word sensitivity.")
else:
    print("No, the files don't contain the word sensitivity.")

with open("teacher_poem.txt") as f:
   content = f.read()
with open("teacher_copy.txt","w") as file:
   file.write(content)

with open("teacher_poem.txt") as file1:
   con1 = file1.read()
with open("teacher_copy.txt") as file2:
   con2 = file2.read()
if(con1 == con2):
   print("Both files are identical.")
else:
   print("Both files are different")

with open("teacher_poem.txt","w") as file:
   pass

# with open("teacher_copy.txt") as file:
old_name = "teacher_copy.txt"
new_name = "renamed_by_python.txt"
os.rename(old_name,new_name)
print("teacher_copy.txt is successfully renamed into renamed_by_python.txt")