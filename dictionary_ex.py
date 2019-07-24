#===Input the dictionary values from USER====
#===Program to check whether the given key exist in dictionary or not
#Note: here i have assigned multiple values in key 'Hobby' for dictionary
'''dict1={}
print("enter the employee details")
dict1['Name']=input("please enter the name\n")
dict1['grade']=input("enter the grade of employee\n")
dict1['Age']=int(input("Enter the age of employee\n"))
dict1['Office']=input("Enter the organsation name\n")
#dict1['Hobby']=input("Enter the hobby of person\n")
for i in range(0,2):
    h1=input("Enter the hobby of person\n")
    key = "Hobby"
    dict1.setdefault(key, [])
    dict1[key].append(h1)

print("now the dictionary values are\n")
print(dict1)

print("\n",dict1.keys()) #it will display key
print("\n",dict1.items()) #it will display keys and value both
print(str(dict1)) #It converts the dictionary into printable string format

#check whether the key exist in dictionary key or not
key1=input("enter the key that yow want to search in dictionary\n")
if key1 in dict1.keys():
    print("\n key is available in dictionary")
else:
    print("\nkey is not available in dictionary")'''

#Python Program to Concatenate Two Dictionaries Into One

'''d1={}
d2={}
d3={}
print("enter the values for 1st dictionary")
d1['name']=input("enter the name\n")
d1['age']=int(input("enter the age of employee\n"))
print("enter the values for second dictionary")
d2['langauge']=input("enter the language you like\n")
d2['database']=input("enter the database you like to work\n")
print("after concacenate the new dictionary is\n")
d3=d1.copy()
d3=d2.copy()
d3.update(d1)#concate 2 dictionaries into new dictionary
print("the new dictionary is\n",d3)
d1.update(d2)
print("After concate the new dictionary into existing\n",d1)'''

#==Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).==
#==hre comprehension will be used:

'''n=int(input("Enter a limit for dictionary up to u want to generate:\n"))
d={x:x*x for x in range(1,n+1)} #here dictionary comprehension is used
print(" the result is\n",d)'''

#==Python Program to Sum All the Items in a Dictionary
#==Python Program to Multiply All the Items in a Dictionary

'''subject={}
subject['maths']=int(input("enter the marks for maths\n"))
subject['english']=int(input("enter the marks for english\n"))
subject['science']=int(input("enter the marks for science\n"))
subject['physics']=int(input("enter the marks for physics\n"))
subject['hindi']=int(input("enter the marks for hindi\n"))
#res=sum(subject.values())
sum=0
mul=1
for i in subject.values():
    sum=sum+i
    mul=mul*i
print("the sum of the values in dictionary is==>>",sum)
print("the multiplication of the values in dictionary is==>>",mul)'''

#==Python Program to Remove the Given Key from a Dictionary===

'''subject={}
subject['maths']=int(input("enter the marks for maths\n"))
subject['english']=int(input("enter the marks for english\n"))
subject['science']=int(input("enter the marks for science\n"))
subject['physics']=int(input("enter the marks for physics\n"))
subject['hindi']=int(input("enter the marks for hindi\n"))
print("the dictionary is\n",subject)
k=input("enter the key to delete\n")
if k in subject:
    del subject[k]
else:
    print("Key not found!")
    exit(0)
#del subject[k1]
print("after deleting the key the dictionary is\n",subject)'''

#==Python Program to Create a Dictionary with Key as First Character and Value as Words Starting with that Character

'''test_string=input("Enter string:")
list=test_string.split()
d={}
for i in list:
    if(i[0] not in d.keys()):
        d[i[0]]=[]
        d[i[0]].append(i)
    else:
        if(i not in d[i[0]]):
          d[i[0]].append(i)
for k,v in d.items():
        print(k,":",v)'''

#==Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary ===

'''str=input("enter the string\n")
word=[]
word=str.split()
dic={}

print(word)

for i in word:
    dic[i]=word.count(i)

print("count of dictionary items are\n",dic)'''

#program to sort nested dictionary and sum the values in nested dictionary
'''test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
             'Akshat' : {'roll' : 54, 'marks' : 12},
             'Akash' : { 'roll' : 12, 'marks' : 15}}
res = sorted(test_dict.items(), key = lambda x: x[1]['marks'])
print("sorting in nested dictionary",res)
sum=0
for i in test_dict.items():
    sum=sum+i[1]['marks']
    print(i[1]['marks'])
print(sum)'''

#how to add keys in nested dictionary
'''d1={'hobby':{'sports':'swimming','movie':'hollywood'}}
print("nested dictionary",d1)
print("after adding key in nested dictionary\n")
d1['hobby']['rank']=1
print(d1)
#using update method
print("Using Update Method to adding key in nested dictionary\n")
d1['hobby'].update({'book':'english','music':'jazz'})
print(d1)
d1.update({'education':'Bachelors','phd':'CS'})
print(d1)'''

#passing list into dictionary
'''list=['roli','anna','charlie']
list1=[2,3,4]
abc=dict(zip(list,list1))
print(abc)

#passing tuples into dictionary
t=(12,34,45)
t1=((2,3),(4,6),(4,5))
abc1=dict(zip(t,t1))
print(abc1)'''

#passsing dictionary into string
'''dict = {'Name': 'nandita', 'Age': "twenty"};
print ("Equivalent String : %s" % str (dict))
print(type(str))

a=sorted(dict)
print("sorted dictionary",a)

b=list(dict.values())
b.sort()
print(b)

print(dict)'''

'''key = [chr(x) for x in range(100, 110)]
val = [x ** 2 for x in range(10)]

# creating dict with squares of numbers
mydict = dict(zip(key, val))
print(mydict)
print(mydict)'''

'''from collections import defaultdict
#If the key does not exist, and we try to access it, it raises a KeyError. so to deal this situation we use defaultdict
def defaultvalue(): #we define a python function to return a default value for the keys we don’t initialize.
                return 0
#create a Python defaultdict using the defaultdict() function. To this, we pass the function defaultvalue as a function argument.
#always pass an object dont call the function using paranthesis
otherdict=defaultdict(defaultvalue)
otherdict['a']=1
otherdict['b']=2
otherdict['c']=3
otherdict['d']

print(otherdict)''' #here for key 'd' no value is assigned so default value '0' will be assigned

#setting the default value as user defined for the key whether the key is mentioned or not

'''from collections import defaultdict
marks = defaultdict(lambda:67) #it will set the value 67 for the keys for whome no value is defined or key is not defined
marks['ankita'] = 45
marks['sangita']= 77
marks['radha']
print(marks)
print(marks['shikha'])'''#if we try to access the value to a key that doesn’t exist, it saves 67 to it.

#*******Ordereddict()***********
#Python OrderedDict is just like a regular dictionary in python, but it also saves the order in which pairs were added.

from collections import OrderedDict

dic=OrderedDict()
dico=OrderedDict()
dic={'name':'nandita','office':'HCL','loc':'bangalore'}
dico={'name':'ankita','loc':'karnataka','office':'IBM'}
print(dic)
print(dico)
print("Ordered dictionary : Order matters==>",dic==dico)

#ordiniary dictionary : order does not matter
d1={'maths':24,'english':78,'hindi':89}
d2={'english':78,'hindi':89,'maths':24}
print("ordiniary dictionary : order does not matter==>",d1==d2)
