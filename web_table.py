from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")

#find xpath comoon for columns and rows remove index value and pass inside the len() function
#count total rows and col by using len()

rows=len(driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr"))

cols=len(driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/thead/tr/th"))
print("Total rows in table",rows)
print("Total Columns in Table",cols)


print("Name"+"   	"+"Position"+"       	"+"Office"+"        	"+"Age"+" 	          "+"Start date"+"         	"+"Salary")
'''for r in range(2,rows+1): #outer loop for rows excluding heading
    for c in range(1,cols+1): #inner loop for col start with 1 col till end as cols+1
        result=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(result,end='           ')
    print()'''

#code to display only specfic value
for r in range(2,rows+1): #outer loop for rows excluding heading
    result=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr["+str(r)+"]/td["+str(4)+"]").text
    print(result)

print(max(result))
driver.close()

#note: In the above program we have passed the parameters in Xpath and also did type casting because r & c are integer values as defined for range