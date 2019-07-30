'''Here we have called the base class function 'cal' in child class and provided extra functionality, so it is also called
method overriding

and when a function have more thna one form that is called Polymorphism'''

# A simple Python function to demonstrate
# Polymorphism

'''def add(x, y, z=0):
    return x + y + z

# Driver code
print(add(2, 3))
print(add(2, 3, 4))'''

#Polymorphism / Method Overriding example in class-inheritance
'''class exam():
    def cal(self,num):
        self.num=num
        print("the sum is",num*num)
class exam2(exam):
    def cal(self,num,n1):
        self.num=num
        self.n1=n1
        print("the cal is",num+n1)
obj=exam()
obj1=exam2()
obj.cal(2)
obj1.cal(2,7)'''

#polymorphism with class-methods

'''class academic():
    def habits(self):
        print("i liked to play alot")

class profess():
    def habits(self):
        print("i liked music alot")

obj=academic()
obj1=profess()

for i in (obj,obj1):
    i.habits()'''

# Polymorphism with a Function and objects:
'''class academic():
    def habits(self):
        print("i liked to play alot")

class profess():
    def habits(self):
        print("i liked music alot")

def dis(ob):
    ob.habits()

obj=academic()
obj1=profess()

dis(obj)
dis(obj1)'''