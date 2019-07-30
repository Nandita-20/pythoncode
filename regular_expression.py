import re

str='''Learn Tutorials Leeaaearn Java 
    Learean Data Structures Learn C 
    Programming Javatpoint.com Hindi100.com
    Lyricsia.commmm Quoteperson.com '''

str1="Address: G-13, 2nd Floor, Sec-3 Noida, UP, 201301, India Contact No: 0120-425646, 9990-449935, +91-2345678921 +91-7754455454 Contact Us Subscribe Us"
str3="i like learning python, python is one of the scripting langayge, i love python very much"
#print(str,"\n",str1)

#use of Findall
print("Output of findall function")
matches=re.findall(".com",str)
print(matches)

#use of search method: serach method also search string but it returns match object, i.e span, group and string

print("Output of match function")
matches1=re.search("Us",str) #returns none as as no match in str
matches2=re.search("Us",str1)
print(matches1)
print(matches2)
print(matches2.span()) #It returns the tuple containing the starting and end position of the match.
print(matches2.group()) #It returns a string passed into the function.
print(matches2.string) #The part of the string is returned where the match is found.

#split function: it split the string from matched pattern and returns the string before and after the matched string
print("Output of split function")
matches3=re.split("python",str3)
print(matches3)

#sub method: sub(pattern,repl,string) => it replaces the searched pattern with given string pattern within the pattern string

print("Output of sub method")
res=re.sub("python","python3",str3)
print(res)

#matacharacters
#res1=re.compile(r'.hon') # (.) will give the character before (.) i.e thon in the string
#res1=re.compile(r'^Learn') #^ is used to return the if string starts with Learn otherwise no reuslt
#res1=re.compile(r'com$') # ($) is used to return the if string ends with Learn otherwise no reuslt
#res1=re.compile(r'c*om*') #return 0 or more occuerence of character before the aestric i.e there may be 0 or multile 'm' and 'c'
#res1=re.compile(r'c+om+') #return 1 or more occurences
#res1=re.compile(r'ea{1}') #The specified number of occurrences of a pattern the string
#res1=re.compile(r'Learn|Java') #It represents either this or that character is present.
#res1=re.compile(r'(ea){1}')
#result=res1.finditer(str)
#for i in result:
 #   print(i)

#Special Sequence

#res=re.compile(r'\ALearn') #\A is uesd to return if the string starts with learn
#res=re.compile(r'Learn\b')
#res=re.compile(r'\d{4}-\d{6}') #search for digit like befor hypen there are 4 characters and after hypen there are 6 characters
#here we used curly braces bxoz we know by using curly braces we can give exact no of digits or characers
#res=re.compile(r'\D{4}-\d{6}') #search if the string does not have digits
#res=re.compile(r"[+91]{3}-[0-9]{10}") #here [] sqaure brackets are used to create set
#result=res.finditer(str1) #we can use findall() function also to display only mobilenos
#for i in result:
#    print(i)

