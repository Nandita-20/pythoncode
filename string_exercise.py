#===== Python Program to Replace all Occurrences of ‘a’ with $ in a String ======
#=====Python Program to Remove the nth Index Character from a Non-Empty String ====
#to remove we need to convert string into list bcoz in string there is no remove method
'''a=input("enter the string\n")
print("the string is",a)
res=a.replace('a','$')
print("the replaced string is",res)
n=int(input("enter the position for which you want to remove character\n"))
res=list(a)
res.pop(n)
a="".join(res)
print(a)
str="*****this is string example....wow!!!*****"
print(str.strip('*'))'''

#====Python Program to Detect if Two Strings are Anagrams(equal)=========
#====Python Program to Form a New String where the First Character and the Last Character have been Exchanged===
#==== Python Program to Count the Number of Vowels in a String======
#====Python Program to Take in a String and Replace Every Blank Space with Hyphen=====
#====Python Program to Calculate the Length/number of characters of a String Without Using a Library Function ===
'''str=input("enter the first string\n")
str1=input("enter the second string\n")
print(sorted(str))
print(sorted(str1))
if sorted(str)==sorted(str1):
    print("Strings are Anagrams")
else:
    print("strings are not anagrams")

res=str[0] #extract 1st char
res1=str[-1] #extract last charcater and then merged
print("The new string after swapping==>:",str[-1]+str[1:-1]+str[0])

#vowels counting
count=0
for i in str:
    if i in ('a','e','i','o','u'):
        print(i)
        count=count+1
print("total vowels are==>:",count)
#Replace Every Blank Space with Hyphen
str=str.replace(' ','-')
print(str)
#Length of a String, no of characters Without Using a Library Function
c=0
for i in str:
    c=c+1
print("the length of the string is:",c)'''

#Python Program to Calculate the Number of Words and characters in a string
# Python Program to search substring in a string
'''str2 = input("Please Enter your Own String : \n")
total = 1
c=1
for i in range(len(str2)):
    c=c+1
    if(str2[i] == ' ' or str2 == '\n' or str2 == '\t'):
        total = total + 1

print("Total Number of Words in this String = ", total)
print("Total characters in string",c)

sub=input("enter the sub string to search\n")
total=0
a=[]
a=str2.split(" ")
for i in range(0,len(a)):
    if sub == a[i]:
        total=total+1
else:
    print("FALSE: substring is not inside the string")
print("total occurence of substring",total)'''

#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
#Python Program to Count Number of Lowercase Characters in a String
'''str1=input("enter the first string\n")
str2=input("enter the second string\n")
c=0
c1=0
for i in str1:
    c=c+1
print("the length of the first string is",c)

for j in str2:
    c1=c1+1
print("the length of the second string is",c1)

if c>c1:
    print("the first string is larger than 2 string")
else:
    print("the second string is larger than 1st string")

total=0
for k in str1:
    if k.islower(): #Count Number of Lowercase Characters in a String
        total=total+1
print("no of lower charcaerts",total)

if str1==str1[::-1]:
    print("string is pallindrome")
else:
    print("string is not pallindrome")

print("without reverse",str1[0:])
print("after reverse",str1[::-1])'''

##write a program to reverse the string

'''str="nandita123 is nandita123...wow"
str1=""
for i in str:
    str1=i+str1;
print(str1)

a=str.ljust(15,'*')
print("Output of LJUST()",a)
a=str.rjust(15,'@')
print("Output of RJUST()",a)
str2='123'
a=str.rindex(str2)
print(a)
a=str.index(str2)
print(a)
str1 = "this is really is a string example....wow!!!";
str2 = "is";
print (str1.rfind(str2))'''

'''str1 = "this is string example....wow!!!";
str2 = "is"

print (str1.rindex(str2))
print (str1.index(str2))'''

x = "Guru99"
x = x.replace("Guru99","Python")
print(x)

x = "Guru99"
x.replace("Guru99","Python")
print(x)
