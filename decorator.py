import time
def dec1(func1): #decorator takes one argument, it could be anything, we pass function inside the decorator function
    def sum(a,b):
        print("executing now")
        time.sleep(1)
        func1(a,b)
        print("executed")
    return sum

def dec2(f):  #second decorator definition
    def tab1(n):
        print("Table before execution")
        time.sleep(2)
        f(n)
        print("Table after execution")
    return tab1

@dec1    #add decorator before the function that you pass as an argument
def add(a,b):
    sum=a+b
    print("the sum is",sum)



@dec2   #add decorator before the function that you pass as an argument
def tab(n):
    for i in range(1,11):
        t=n*i
        print(t)

#function calling
add(23,45)
tab(3)


