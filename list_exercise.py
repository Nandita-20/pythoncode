#===Python Program to Find the Largest, 2nd largest and smallest Number in a List

'''list=[]
num=int(input("enter the limit for list\n"))
for i in range(0,num):
    n=int(input("enter the number in list\n"))
    list.append(n)
print(list)
list.sort()
l1=list
print("Largest value in list is",l1[-1])
print("Second Largest value in list is",l1[-2])
print("Smallest value in list is",l1[-0])'''

#==Python Program to Put Even and Odd elements in a List into Two Different Lists===
#==Python Program to Merge Two Lists and Sort it
'''list=[]
even=[]
odd=[]
num=int(input("enter the limit for list\n"))
for i in range(0,num):
    n=int(input("enter the number in list\n"))
    list.append(n)
print(list)

for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even list",even)
print("odd list",odd)

#Merge Two Lists and Sort it
merge=even+odd
print("after merging even and odd",merge)
merge.sort()
sort_list=merge
print("after merging the sorted list is",sort_list)'''

#==Python Program to Sort a List According to the Length of the Elements

'''list=[]
n=int(input("enter the limit to enter animal names in list"))

for i in range(0,n):
    str=input("enter the animal names\n")
    list.append(str)
print("the list of animals is",list)
list.sort(key=len)
sorted_list=list
print("the sorted list according to length of elemnts is",sorted_list)'''

#===Python Program to Find the Union of two Lists maintaing with and without order and repetition
#===Python Program to Find the intersection of two Lists
'''l1=[2,23,34,4]
l2=[23,34]
u1=l1+l2
print("union of two list wothout maintaining order and repetition",u1)
u1.sort()
u2=u1
print("union of two list maintaining order but not repetition",u2)
u3=list(set().union(l1,l2))
u3.sort()
print("union of two list maintaining order and repetition",u3)
u4=list(set(l1).intersection(l2))
print("intersection of two list maintaining order and repetition",u4)'''

#==python program to count sub-list inside the list
'''l1=[[21,23],['cat','dog'],['123nand']]
l2=len(l1)
print("Length of sub-list inside the list",l2)'''

#==Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number===
#===using list_comprehension===

'''lower=int(input("enter the lower limit\n"))
upper=int(input("enter the upper limit\n"))
res=[(i,i**2) for i in range(lower,upper+1)]
print("The result is\n",res)

#or you can use for loop to get the result
print("result using for loop\n")
for i in range(lower,upper+1):
    print(i,i**2)'''

#==Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
'''import random
a=[]
n=int(input("enter the limit to generate random number\n"))
for i in range(0,n):
    a.append(random.randint(1,20))
print("list of random number is \n",a)'''

#==Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple ==
#use of lambda function
#way to take input in tuple from user by using list and then convert that list into tuple
'''inList=[]
for i in range(1,4):
    instr = input('Enter a point (x,y): \n')
    inList.append([int(n) for n in instr.split(',')])   # check for parens too?
    point = tuple(inList)
print(point)
output = sorted(point, key=lambda x: x[-1])
print (output)
#we can use for loop alos inplace of lambda to return the tuple value from last index
for i in point:
    print(i-1)'''

#===Python Program to Swap the First and Last Value of a List===
#===Python Program to Remove the Duplicate Items from a List===
'''list=[]
list2=[]
n=int(input("enter the limit to create the list\n"))
for i in range(0,n):
    str=input("enter the animal names\n")
    list.append(str)
print(list)
#Swap the First and Last Value of a List
a=list[-1]
b=list[0]
list[0]=a
list[-1]=b
print(list)
#Remove the Duplicate Items from a List
for j in list:
    if j not in list2:
        list2.append(j)
print("after removing the duplicate values the list is",list2)'''

#==Python Program to Read a List of Words and Return the Length of the Longest One
list=[]
#list2=[]
n=int(input("enter the limit to create the list\n"))
for i in range(0,n):
    str=input("enter the animal names\n")
    list.append(str)
print(list)
maxl=len(list[0])
temp=list[0]
temp1=list[0]
for j in list:
    if len(j)<maxl:
        maxl=len(j)
        temp=j
    if len(j)>maxl:
        maxl=len(j)
        temp1=j
print("the smallest string is",temp)
print("the longest string is",temp1)