class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

        # defining class methods

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

      #end of superclass definition


# definition of subclass starts here
class Student(Person):  # Person is the  superclass and Student is the subclass
    studentId = ""

    def __init__(self, studentName, studentAge, studentId):
        Person.__init__(self, studentName,studentAge)  # Calling the superclass constructor and sending values of attributes.
        self.studentId = studentId

    def getId(self):
        return self.studentId  # returns the value of student id


# end of subclass definition


# Create an object of the superclass
person1 = Person("Richard", 23)
# call member methods of the objects
person1.showAge()
# Create an object of the subclass
student1 = Student("Max", 22, "102")
print(student1.getId())
student1.showName()

#***************************************************************************************************

'''class maths:
    def __init__(self,x): #defining constructor
        self.x=x

    def cube(self): #defining function to get cube
        result=self.x**2
        print("the cube is==>",result)

    def sqr(self): #defining function to get square
        res=self.x*2
        print("the square is==>",res)

class maths2(maths):  #child class starts here and inheriting parent class
    #y=""
    def __init__(self,x,y): #child class constructor
        self.y = y
        maths.__init__(self,x) #calling parent class constructor inside the child class and sending values of attributes

    def table(self):  #defining function for table
        print("The table is as given\n")
        for i in range(1,11):
            t=self.y*i
            print(t)


num=int(input("enter the value to get the cube"))
num1=int(input("enter the value to get the square"))
num2=int(input("enter the value to get the table"))
obj=maths(num) #parent class object creation
obj.cube()  #calling parent class object using parent class object

obj1=maths2(num1,num2) #child class object created
obj1.sqr()    #calling parent class function using child class object (here inheritance done)
obj1.table()  #calling child class function using child class object'''

