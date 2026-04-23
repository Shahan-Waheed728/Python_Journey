# printing my name by uisng single , double and triple quotes
name1 = 'Shahan Waheed'
name2 = "Bilal Awan"
name3 = '''Najma Sadia'''
print(name1)
print(name2)
print(name3)

# slicing of string 
print(name1[0:6])  #print Shahan
print(name1[0:4]) #print Shah
print(name1[4:6]) #print an
print(name1[7:]) #print Waheed
print(name1[:13]) #print Shahan Waheed

print(name2[-4:]) #print Awan
print(name2[-10:-5]) #print Bilal
print(name2[-8:-5])

print(name3[0:]) #print Najma Sadia
print(name3[2:9]) #print jma Sad
print(name3[-5:]) #print Sadia

#working with skip method
print(name1[0:13:3]) #print Saaaed
print(name2[0:10:2]) #print BllAa
print(name2[0:10:3]) #print BaAn
print(name3[0:11:2]) #print NjaSda
print(name3[0:11:3]) #print NmSi