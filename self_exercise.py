'''list1=['nandita','ankita']
list2=['ash','sash']

list1.append(list2)
print("first_list",list1)
list2.extend(list1)
print("second list",list2)'''

'''list1=[]
list2=["nandita",123]
for i in range(0,3):
    a=input("enter the books name\n")
    list1.append(a)
print("the new list is",list1)
list1.append(list2)
print("after appending the list",list1)
list1.extend(list2)
print("after extending the list",list1)
list1.pop()
print("after popping the element the list is",list1)'''

l1=[23,34,45,34,56]
l2=[3,4]
l1.append(l2)
print("appended list",l1)
print("\n")
l1.extend(l2)
print("extended list",l1)
l1.extend("nandita")
print("extended list after passing argument",l1)
print(l1[5][0])
count=l1.count(34)
print("the count is",count)
l1.reverse()
print("the reversed list is",l1)
a=l1.index(56)
print("the indexed value is",a)
b=l1.index('a',0,7)
print("the indexed value is",b)
