'''Constructor types:
1) Default Constructor
2) parameterized Constructor
3) Non-parametrized constructor

There is no copcept of constructor overloading in python
__init__ is used to define the constructir in python

Python in-built class function:
    getatrr()
    setattr()
    delattr()
    hasattr()'''

#Default Constructor
'''class Employee:  #class creation
    id = 10;
    name = "John"

	#function created
		#the self is used as a reference variable which refers to the current class object.
		#It is always the first argument in the function definition. However, using self is optional in the function call.

    def display (self):
        print("Id is %d \n Name is %s"%(self.id,self.name))

emp = Employee()  #object created for class or creating the instan
emp.display()   #function called through class object '''

#example of non-parameterised constructor
'''class example:
    def __init__(self):
        self.name="nandita"
        self.office="HCL"
    def disp(self):
        print("my name and work location is\n",self.name,self.office)
obj=example()
obj.disp()'''

# Program of parametirized constructor
'''Once the object is created, you can make sure that every variable in the object is correctly initialised by defining an __init__ method in your class,
which pretty much means init-iate.

Thus, it doesn't matter what the class name is, if you want to write a constructor(to initialise your object) for that class,
it has to be the __init__() method. Within this function, you're free to declare a class variable(using self) or initialize them.'''

'''class Employee:  
    def __init__(self,id,name):  #parameterized constructor
        self.id = id;  
        self.name = name;  
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name))

a=int(input("enter the value of a\n"))
b=input("enter the value for name\n")
emp1 = Employee(a,b)  
#accessing display() method to print employee 1 information  
emp1.display(); '''

# table using constructor
'''class employee:
	def __init__(self,num):
		self.num=num
	def table(self):
		for i in range(1,11):
			t=self.num*i
			print(t)

a=int(input("enter the value of a\n"))
emp1=employee(a)
emp1.table()'''

# Table without using constructor
class employee:
	def table(self,num):
		self.num=num
		for i in range(1,11):
			t=self.num*i
			print(t)

a=int(input("enter the value of a\n"))
emp1=employee()
emp1.table(a)


# program of calculator using class, and constructor
'''class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = cal(a, b)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Addition Result: ", obj.add())
    elif choice == 2:
        print("Substraction Result: ", obj.sub())
    elif choice == 3:
        print("Multiplication Result: ", obj.mul())
    elif choice == 4:
        print("Division Result: ", round(obj.div(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
print(getattr(obj, 'a'))  # getattr()
setattr(obj, 'a', 23)
print(getattr(obj, 'a'))
print(hasattr(obj, 'a'))  # hasattr()
# print(delattr(obj,'a')) #delete the attribute()
# print(getattr(obj,'a')) #again to check whether the attribute exist or not
print(obj.__doc__)
print(obj.__dict__)
print(obj.__module__)
##print(obj.__bases__) #it return if tuple in class
# print(obj.__name__) #it is used to acess the class name
print()'''










