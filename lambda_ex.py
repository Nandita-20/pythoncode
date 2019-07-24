#Use of lambda function

'''g=lambda x:x*x
a=int(input("enter the value to find the result\n"))
print(g(a))'''

# lambda() with filter()
'''li=[2,3,45,56,67,78]
new_list=list(filter(lambda x:x%2==0,li))
print("list of even numbers\n",new_list)'''

#lambda() with map()
'''li=[2,3,45,67,78]
print("the list before addition\n",li)
new_list=list(map(lambda x:x+2,li))
print("after adding 2 in each digit the list is\n",new_list)'''

#lambda() with reduce()
'''from functools import reduce
li=[2,3,4,5,6,7]
new_list=reduce(lambda x,y:x+y,li)
print("the sum of the list numbers are\n",new_list)'''


'''x = lambda x: (for i in x : print i)
a=int(input("enter the limit\n"))
print(x(a))'''

listOfLambdas = [lambda i=i: i*i for i in range(1, 6)]
#print(listOfLambdas)
for f in listOfLambdas:
   print(f)


y = 8
z = lambda x : x * y
print z(6)
