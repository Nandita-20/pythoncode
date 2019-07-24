'''new_list1=[i%3==0 for i in [1,2,3,4,5,6,7,8,9]]
print(new_list1)'''

# list1=[23,24,35,56]
'''for i in list1:
    print(i**2)'''

'''list2=[i**2 for i in range(1,11)]
print(list2)'''

name = ['harshit', 'rohit', 'mohit']
'''for i in name:
	print(i[2])'''

'''new_name=[i[2] for i in name]
print(new_name)'''

# Using IF in List comprehension

''' list2=[i for i in range(1,12) if i%2==0]
print(list2)'''

'''for i in range(1,12):
    if i%2==0:
        list2.append(i)
print(list2)'''

# Using Nested Loop in List comprehension

'''new_list=[]
for x in [2,4,6]:
	for y in [100,200,300]:
		new_list.append(x*y)
print(new_list)'''

'''new_list=[x*y for x in [2,4,6] for y in [100,200,300]]
print(new_list)'''

# progam to find divisbile by 3, 5 and 3,5 both if divisbleby 3 print "fizz", if by 5 print"buzz" if by 3 &5 print "fizzbuzz"

'''for i in range(1,31):
	if i%3==0:
		print("fizz",i)
	elif i%5==0:
		print("bizz",i)
	elif i%3==0 and i%5==0:
		print("fizz&bizz",i)'''

'''new_list1=[i for i in range(1,31) if i%3==0]
print(new_list1)'''

# print every word in the sentence that has an even number of letters


# program to find len of words , display the words separately and if len is = 5 then print even

'''st=['print', 'every', 'word']
for i in st:
	print("the words are\t",i)
	if len(i)==5:
		print("even")'''

# program to store first 3 characters of each word in list
'''st=['print', 'every', 'word']
for i in st:
	list2=i[0:3]
	print(list2)'''

# Using comprehension list
'''st=['print', 'every', 'word']
list2=[i[0:3] for i in st]
print(list2)'''

# Go through the string below and if the length of a word is even print "even!" "
#st = 'Every letter print every word in the sentence that has an even number of letters'
'''for i in st.split():
    if len(i) % 2 == 0:
        print(i, "even!")'''

# write the program to split the string and print out the word that starts with 'e'
'''st = 'Every letter print every word in the sentence that has an even number of letters'
for i in st.split():
    if i[0] == 'e' or i[0] == 'E':
        print(i)'''



