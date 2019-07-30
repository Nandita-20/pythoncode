#program to print the sum of two number without passing parameters inside the function

'''def sum(): #defining the function

	#taking input from user
	a=int(input("enter the value of a\n"))
	b=int(input("enter the value of b\n"))
	sum=a+b
	print("the sum is",sum)

sum() #calling the function '''

#program to print the sum of two number by passing parameters inside the function

'''def sum(a,b):
	return a+b
a=int(input("enter the value of a\n"))
b=int(input("enter the value of b\n"))
print("the sum of two number is",sum(a,b))'''

#function to print the table

'''def table():
	num=int(input("enter the numto print the table"))
	i=1
	while(i<=10):
		t=num*i
		print(t)
		i=i+1
table()'''

#program to print the factorial of the number

'''def fact():
	num=int(input("enter the number to print the factorial value\n"))
	f=1
	i=num
	while(i>=1):
		f=f*i;
		i=i-1
	print("the factorial is",f)
fact()'''

#program to print the factorial using call by reference

'''def fact(a):
	f=1
	i=a
	while(i>=1):
		f=f*i;
		i=i-1
	print(f)
num=int(input("enter the value of a"))
fact(num)'''

#passing immutable object(LIST) in function (Call by refernce)

'''def disp(list1):
	list1=[1,2,3,4,5]
	#list1.append(30)
	print("the list inside the function\n",list1)
list2=[10,40,60]
disp(list2)
print("the list defined outside the function",list2)

Output: the list inside the function
 [1, 2, 3, 4, 5]
the list defined outside the function [10, 40, 60]'''

'''def disp(list1):
	list1.append(20)
	list1.append(30)
	print("the list inside the function\n",list1)
list2=[10,40,60]
disp(list2)
print("the list defined outside the function",list2)

Output: the list inside the function
 [10, 40, 60, 20, 30]
the list defined outside the function [10, 40, 60, 20, 30]'''

#passing mutable object(String) in function (Call by refernce)

'''def disp(str1):
	str1=str1+"hello Python"
	print("the string inside the function\n",str1)

str2="hello world\t"
disp(str2)
print("the string value outside the function\n",str2)'''

#Keyword Arguments

'''def sum1(num1,num2):
	sum=num1+num2
	print(sum)
a=int(input("enter the value for a\n"))
b=int(input("enter the value for b\n"))
sum1(num2=a,num1=b)'''



#write to a program to find that whether the first character for both string is same or not
'''str1="nandita Nrivastava"
str2=str1.lower().split()
print(str2)
fir=str2[0]
sec=str2[1]
print(fir,"\n",sec)
if fir[0]==sec[0]:
	print("first character for both string is same\n")
else:
	print("first character for both string is not same\n")'''

#write a program to reverse the words of string

'''str1="My name is nandita"
wordlist=str1.split()
reverse_word=wordlist[::-1]
print(reverse_word) #it will reverse the string
fir=wordlist[0]
sec=wordlist[1]
third=wordlist[2]
four=wordlist[3]
print(fir[::-1],sec[::-1],third[::-1],four[::-1]) #it will reverse the word of strings'''

#Given a list of ints, retrun True if array contains a 3 next to a 3 somewhere

'''def arr():
	nums=input("enter the numbers")
	for i in range(0,len(nums)-1):
		if nums[i]==3 and nums[i+1]==3:
			print("true")
arr()'''

#write a program for string where for each character in original string will be 3 characters.

'''str1="nandita"
result=''
for i in str1:
	result=result+i*3
print(result)

output: nnnaaannndddiiitttaaa (if print will be outside)
output: If print will be inside
nnn
nnnaaa
nnnaaannn
nnnaaannnddd
nnnaaannndddiii
nnnaaannndddiiittt
nnnaaannndddiiitttaaa '''

#Understanding the scope of variables
'''a=2
def sum():
    global a
    a=3
    b=8
    s=a+b
    print(s)
sum()
print(a)

#command to delete the function
#del sum'''

#unserstanding Default Arguement scenario.

#first exmaple
'''def sum(c=0):
    a=4
    for i in range(1,a+1):
        c=c+a
    print(c)
sum()'''

#2nd Example
'''def sum(a=2,b=3):
    c=a+b
    print(c)
sum(4,6)'''


#first scenario: non-default argument can not follow  default argument

'''def sum(a=23,b):
    s=a+b
    print(s)
sum(2,6)'''  #SyntaxError: non-default argument follows default argument

#Second scenario: default arguments can follow non-default argument

'''def sum(a,b=23):
    s=a+b
    print(s)
sum(2)'''

#Understanding Keyword Argument
#first program
'''def divide(a,b):
    c=a/b
    print(c)
divide(b=6,a=3)''' #o/p: 0.5 , no issues while changing the order of argument.
#divide(a=6,3) # error: positional argument follows keyword argument
#divide(b=3,a) # error multiple values of a

#second program
'''def sum1(num1,num2):
	sum=num1+num2
	print(sum)
a=int(input("enter the value for a\n"))
b=int(input("enter the value for b\n"))
sum1(num2=a,num1=b)'''

#Variable length Arguments *args


#a,b,c,d = [int(x) for x in input("Enter 4 values with single space: ").split()] #list comprehension method for taking multiple inputs
'''add(a,b)
add(a,b,c)
add(a,b,c,d)'''


def sum(*num,**num1):
    s=0
    for i in num:
        s=s+i
    print("positional",s)
    print("keywords",num1)
sum(2)
sum(2,3,a=234,b=236)
sum(34,45,56,name='nandita',office='HCL')



'''def intro(**data):
	print("\nData type of argument:",type(data))
	for key, value in data.items():
		print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
#intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)'''