'''try:
    print(1+'i')
    print("sum does not exist")
    print(1/0)

except NameError:
    print("sum does not exist")

except ZeroDivisionError:
    print("cannot divide by zero")

except Exception as e:
    raise

except Exception  as e:
    print("something wrong==",e)


finally:
    print("Good Bye")'''

#*************use of Raise**************

'''a,b=int(input("enter the value of a\n")),int(input("enter the balue of b\n"))
try:
        print(a+'45')
        raise TypeError("value for b must be non-zero")

finally:
    print("Good Bye")'''

#********assert****************
'''try:
    print(1)
    assert 2 + 2 == 4
    print(2)
    assert 1 + 2 == 4,"here sum is wrong"
    print(3)
except:
    print("An assert failed.")
    raise
finally:
    print("Okay")
    print("Bye")'''

'''class MyError(Exception):
    print("This is a problem")

try:
    raise MyError("MyError happened")
except MyError as e:
    print("wrong output",e)'''


#*************Custom Exception**********
'''class newerror(Exception):
    print("this is a problem")

try:
    c=50
    if c>5:
        raise newerror

except:
    print("rasing issue")'''



'''class tooshortname(Exception):
    print("length should be more than 10 characters")
try:
    
    if len("joe")<5:
            raise tooshortname()
except:
    print("error displayed")
else:
    print("correct length")'''


'''try:
    def validate(name):
        if len(name)<5:
            raise tooshortname
except:
    print("error displayed")
validate("joe")'''

'''a=2
b=7
try:
    c=b+d
    print(c)
except NameError as e:
    print("wrong input",e)'''

