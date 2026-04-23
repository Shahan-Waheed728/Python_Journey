s1= {1,2,3,4,5,6,7,8,9,10}
s2 = {1,3,5,7,9}
s3 = {2,4,6,8,10}
s = {2,6}
s4 = {1,2,4,5,6}
# print(s1, type(s1))
# print(s2,type(s2))
# print(s3,type(s3))
s4.add(8)
s4.remove(2)
# print(s4,type(s4))
print(s2.union(s3))
print(s2.intersection(s4))
print(s2.issubset(s1))
print(s3.issuperset(s4))
print(s.issubset(s3))
print(len(s1))
print(len(s2))
print(len(s3))
print(len(s))
print(len(s4))
print(s1.clear())
print(s2.clear())
print(s3.clear())
print(s.clear())
print(s4.clear())
