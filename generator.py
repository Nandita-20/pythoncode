'''def fab(n):
    nterms=10
    n1=0
    n2=1
    count=0
    if n==0:
        yield 0
    elif n==1:
        yield 1
    else:
        while count<nterms:
            print(n1,end=' ,')
            nth=n1+n2
            n1=n2
            n2=nth
            count=count+1
n=fab(7)
print(n.__next__())'''

'''def fab(n):
    n1=0
    n2=1
    if n==0:
        yield 0
    elif n==1:
        yield 1
    else:
        for i in range(n):
            print(n1,end=' ,')
            sum=n1+n2
            n1=n2
            n2=sum
n=fab(10)
print(n.__next__())'''

def fact(n):
    f=1
    i=1
    while i<=n+1:
        f=f*i
        i=i+1
        yield f
n=fact(6)
for j in n:
   print(j) #or uncomment below lines
#print(n.__next__())
#print(n.__next__())
#print(n.__next__())
#print(n.__next__())
#print(n.__next__())
#print(n.__next__())
#print(n.__next__())
#print(n.__next__())  On uncomment it will through error bcoz reached beyond the limit

#******************************************

'''def fact(n):
    i=n
    f=1
    while i>=1:
        f=f*i
        i=i-1
    print(f)

fact(5)'''

