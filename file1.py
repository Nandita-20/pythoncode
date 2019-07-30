class maths:
    def odd(self,num):
       self.num=num
       if self.num%2==0:
           print("even")
       else:
           print("odd")


    def table(self,num):
        self.num = num
        for i in range(1,11):
            t=self.num*i
            print(t)

    def cube(self,num):
        self.num=num
        res=self.num**2
        print("the cube is",res)


obj=maths()
num = int(input("enter the number to check whether it is even or odd\n"))
obj.odd(num)
num1 = int(input("enter the number to print table\n"))
obj.table(num1)
obj.cube(num1)
