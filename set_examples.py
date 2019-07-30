#take input from user to add values in set

'''days=set()
for i in range(0,4):
    val=input("enter the values in set\n")
    days.add(val)
print("the created set values are\n",days)'''


#===Python Program to Count the Number of Vowels Present in a String using Sets
'''s=input("Enter string:")
count = 0
c=0
vowels = set("aeiouAEIOU")
for letter in s:
    if letter in vowels:
        count += 1
    else:
        c+=1
print("Count of the vowels is:")
print(count)
print("Count of the consonants is:")
print(c)'''

#==Python Program to Check Common Letters in Two Input Strings using set method

'''str=input("enter the first string\n")
str1=input("enter the second string\n")
a=set(str)
b=set(str1)
print(a.intersection(b))'''

#==Python Program to Check Common Letters in Two Sets input by user
'''days=set()
for i in range(0,4):
    val=input("enter the values in set\n")
    days.add(val)
print("the created first set values are\n",days)

day2=set()
for i in range(0,4):
    val=input("enter the values in set\n")
    day2.add(val)
print("the created  second set values are\n",day2)
print("common values in two sets are==>",days.intersection(day2))'''

s1=set([2,3,4,5])
sr=set([34,45,56,67])
s1.add(89)
print(s1)
s1.update(sr)
print(s1)
s1.pop()
print(s1)
s1.remove(67)
print(s1)
print("diffrence")
print("first set",s1)
print("second set",sr)
diff=s1.difference(sr)
print(diff)
print("diffrence_update")
print("first set",s1)
print("second set",sr)
s1.difference_update(sr)
print(s1)
print("isdisjoint")
print("first set",s1)
s2={3,45,56,67}
print("second set",s2)
disjoi=s1.isdisjoint(s2)
print(disjoi)
print("symmetric_difference")
print("first set",s1)
s2={3,45,56,67}
s3={3,45,56,67}
print("first set",s2)
print("second set",s3)
disjoi=s2.symmetric_difference(s3)
print(disjoi)
print("symmetric_difference_update")

s2={3,45,56,67}
s3={3,45,56,67,455,566}
print("first set",s2)
print("second set",s3)
s2.symmetric_difference_update(s3)
print(s2)
s4=s2.copy()
s2.add(77)
s4.add(88)
print("copied set",s4)
print("after adding the set is ",s2)
print("copy the set without using copy method, by using =")
s5=s2
print(s5)
s5.add(90)
print("copied set after adding element in copied set",s5)
print("original set",s2)
s2.add(890)
print("copied set after adding element in original set",s5)
print("original set after adding element in original set",s2)
