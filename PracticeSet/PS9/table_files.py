import os
# # python program to generate table from 2 to 20 and place them in different files, then place files in a folder which is 13 years old.
# def table():
#     t2 = 2
#     print("***Printing table of 2***")    
#     for i in range(1,11):
#         print(f"{t2} * {i} = {t2 * i}")

#     t3 = 3
#     print("***Printing table of 3***")
#     for i in range(1,11):
#         print(f"{t3} * {i} = {t3 * i}")
    
#     t4 = 4
#     print("***Printing table of 4***")
#     for i in range(1,11):
#         print(f"{t4} * {i} = {t4 * i}")

#     t5 = 5
#     print("***Printing table of 5***")
#     for i in range(1,11):
#         print(f"{t5} * {i} = {t5 * i}")
    
#     t6 = 6
#     print("***Printing table of 6***")
#     for i in range(1,11):
#         print(f"{t6} * {i} = {t6 * i}")

#     t7 = 7
#     print("***Printing table of 6***")
#     for i in range(1,11):
#         print(f"{t7} * {i} = {t7 * i}")
    
#     t8 = 8
#     print("***Printing table of 8***")
#     for i in range(1,11):
#         print(f"{t8} * {i} = {t8 * i}")

#     t9 = 9
#     print("***Printing table of 9***")
#     for i in range(1,11):
#         print(f"{t9} * {i} = {t9 * i}")
    
#     t10 = 10
#     print("***Printing table of 10***")
#     for i in range(1,11):
#         print(f"{t10} * {i} = {t10 * i}")

       
#     t11 = 11
#     print("***Printing table of 11***")
#     for i in range(1,11):
#         print(f"{t11} * {i} = {t11 * i}")

#     t12 = 12
#     print("***Printing table of 12***")
#     for i in range(1,11):
#         print(f"{t12} * {i} = {t12 * i}")
    
#     t13 = 13
#     print("***Printing table of 13***")
#     for i in range(1,11):
#         print(f"{t13} * {i} = {t13 * i}")

#     t14 = 14
#     print("***Printing table of 14***")
#     for i in range(1,11):
#         print(f"{t14} * {i} = {t14 * i}")
    
#     t15 = 15
#     print("***Printing table of 15***")
#     for i in range(1,11):
#         print(f"{t15} * {i} = {t15 * i}")

#     t16 = 16
#     print("***Printing table of 16***")
#     for i in range(1,11):
#         print(f"{t16} * {i} = {t16 * i}")
    
#     t17 = 17
#     print("***Printing table of 17***")
#     for i in range(1,11):
#         print(f"{t17} * {i} = {t17 * i}")

#     t18 = 18
#     print("***Printing table of 18***")
#     for i in range(1,11):
#         print(f"{t18} * {i} = {t18 * i}")
    
#     t19 = 19
#     print("***Printing table of 19***")
#     for i in range(1,11):
#         print(f"{t19} * {i} = {t19 * i}")

#     t20 = 20
#     print("***Printing table of 20***")
#     for i in range(1,11):
#         print(f"{t20} * {i} = {t20 * i}")
    
# result = table()
# print(result)
# with open("table_files.txt","w") as f:
#     f.write(str(result))

# def table():
#     result = ""
#     for i in range(2,21):
#         for j in range(1,11):
#            line = f"{i} * {j} = {i * j} \n"
#            print(line,end="" )                  
#            result += line
#         result += "\n"
#     return result

# result = table()

# with open("table_files.txt","w") as f:
#     f.write(result)


"""
     def table2():
      t2 = 2
      result = ""
      print("***Printing table of 2***")
      for i in range(1,11):
          line = f"{t2} * {i} = {t2 * i}"
          print(line,edu="")
          result += line
        result += "\n"
      return result

result = table()
with open("table2_5.txt,"w") as f:
  f.write(result)
"""
os.makedirs("Tables",exist_ok=True)
def table2_5():
    result1 = ""    
    for i in range(2,6):
     for j in range(1,11):
        line = f"{i} * {j} = {i * j} \n"
        print(line,end="")
        result1 += line
     result1 += "\n"
    return result1
result1 = table2_5()

with open("Tables/table2_5","w") as f:
   f.write(result1)

def table6_10():
    result2 = ""    
    for i in range(6,11):
     for j in range(1,11):
        line = f"{i} * {j} = {i * j} \n"
        print(line,end="")
        result2 += line
     result2 += "\n"
    return result2
result2 = table6_10()

with open("Tables/table6_10","w") as f:
   f.write(result2)

def table11_15():
    result3 = ""    
    for i in range(11,16):
     for j in range(1,11):
        line = f"{i} * {j} = {i * j} \n"
        print(line,end="")
        result3 += line
     result3 += "\n"
    return result3
result3 = table11_15()

with open("Tables/table11_15","w") as f:
   f.write(result3)


def table16_20():
    result4 = ""    
    for i in range(16,21):
     for j in range(1,11):
        line = f"{i} * {j} = {i * j} \n"
        print(line,end="")
        result4 += line
     result4 += "\n"
    return result4
result4 = table16_20()

with open("Tables/table16_20.txt","w") as f:
   f.write(result4)




