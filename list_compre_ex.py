#write a program to print the square

'''for i in range(1,4):
    sqr=i*i
    print(i,sqr)'''

#using list=comprehension
'''list1=[i*i for i in range(1,4)]
print("The list containing squares",list1)'''

#write a python program to store numbers divisble by 3 by using loop and list-comprehension
'''print("below using FOR LOOP")
list=[]
for i in range(1,20):
    if i%3==0:
        list.append(i)
print(list)

print("\nbelow using list comprehension")

list=[i for i in range(1,20) if i %3 ==0]
print("The list containing divisble by 3",list)'''

#write a program to find the length of each element in list using for loop and list-comprehension
'''list=['nandita','srivastava']
for i in list:
    print(i,len(i))

list1=[len(i) for i in list]
print(list1)'''

#Python Program to Put Even numbers using list-comprehension
'''list1=[i for i in range(1,20) if i%2==0]
print(list1)'''

#python program to find total vowels from a list of string
'''list=['nandita','srivastava']
print("using LOOP to count no of vowels in Python List ")
v=()
for i in list:
    #print(i)
    for j in i:
        if j in 'aeiou':
            v=v+1
print("Total Vowels",list,v)


vowels=len([j for i in list for j in i if j in 'aeiou'])
print("using list comprehension",vowels)'''

#Remove the Duplicate Items from a List
'''list=[2,3,4,56,67,2,67,56]
print("Using For Loop")
list1=[]
for i in list:
    if i not in list1:
        list1.append(i)
print("list after removing duplicate values",list1)

print("By using list comprehension is not possible so used set")
#list2=[]
list2=set(list)
#list2=[i for i in list if i]==> it is not possible through list comprehension
print(list2)'''

#python program to count sub-list using list comprehension method
'''new_list=[[23,45],[34,56]]
list3=len([i for i in new_list])
print(list3)'''

#set comprehension
'''f={'nan','dit'}
g={'mama','chacha'}
g_lower={i.upper() for i in g}
print(g_lower)'''

#dictionary_comprehension
'''dict1={'name':'nandita', 'office':'HCL'}
dic_comp={i:j for i , j in dict1.items()}
print(dic_comp)'''

