#Range() function provides us list of number to iterate andis used with loop

'''print("print negative values on reverse order\n")
for i in range(-7,-3):
    print(i)
print("print negative to positive values on reverse order\n")
for i in range(-7,3):
    print(i)

print("print values in reverse order by jumping r values\n")
for i in range(7,1,-2):
    print(i)
print("print values upto the given limit\n")
for i in range(8):
    print(i)
print("print values from lower to upper limit m-n\n")
for i in range(1,8):
    print(i)'''

#######################################################################################

#zip() : is a built-in Python function that gives us an iterator of tuples
'''Like a .zip file holds real files within itself, a zip holds real data within. 
It takes iterable elements as input and returns an iterator on them (an iterator of tuples). 
It evaluates the iterables left to right.'''

#zip function using multiple argument of same length
'''a=[1,2,3]
b=['nandita','sangita','ankita']
print(dict(zip(a,b)))'''

'''for i in zip(['red','green'],['rose','leaves'],['%','#','$']):
    print(i)'''

#zip function using multiple argument of same length
#Note: When we provide multiple lists of different lengths, it stops at the shortest one.

'''for i in zip(['red','green'],['rose','leaves'],['%']):
    print(i)'''
    #op: ('red', 'rose', '%')

#zip() function using single argument

'''for i in zip([1,2,3]):
    print(i)'''

#unzipping() function in python

'''z=zip(['red','green'],['rose','leaves'],['%','#'])
a,b,c=zip(*z)
print(a,b,c)'''

#O/P: Now it is unpacked: ('red', 'green') ('rose', 'leaves') ('%', '#')

