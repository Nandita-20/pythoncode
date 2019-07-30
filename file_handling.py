'''file1=open("n3.txt","a")
file1.write("i am learning file handling in python")
file1.close()'''

'''fileread=open("n3.txt","r")
print(fileread.readlines());'''


#create a file

'''file1=open("n1.txt","x")
file1.close()'''

'''file1=open("n1.txt","a")
file1.write("hi, i am new to python")'''

'''file1=open("n1.txt")
print(file1.readline())'''

'''file1=open("n1.txt","w") #'w' mode overwrites the existing file as cursor blinks at the beginning of file
file1.write("i am learning file handling")'''

'''file1=open("n1.txt")
print(file1.readline())'''



'''s1="my name is nandita"
s2="i am learning python"
with open("n2.txt","w") as out:#"a" append from the end of line as cursor blinks at the end of file
    out.write([s1,s2])
#file1.close()'''

'''file1=open("n1.txt")
print(file1.readline())'''

'''line1 = "First line"
line2 = "Second line"
line3 = "Third line"

with open('my_file.txt','w') as out:
    out.writelines('{}\n{}\n{}\n'.format(line1, line2, line3))'''

'''file1=open("my_file.txt","r")
print(file1.readlines(3))'''

'''file1=open("n1.txt","a")
file1.write("hi, i am new to python.\n python is a great language\n")
file1.close()'''

'''file1=open("n1.txt")
print(file1.readline())
print(file1.readlines())'''

#program to read specific lines in file
'''file1=open("n1.txt").readlines()
for i,line in enumerate(file1):
    if i<=2:
        print(i,line)'''

#another method using for loop
'''file1=open("n1.txt").readlines()
for i in range(len(file1)):
    if i<=5:
        print(file1[i])'''

#program using seek and r+
file1=open("write.txt","r+")
seq=["\n This is fourth line in python \n","this is fifth line in python"]
file1.seek(0,2)
output=file1.writelines(seq)
file1.seek(0,0)
for i in file1:
    print(i)

file1.close()

