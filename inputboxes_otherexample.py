from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("https://www.indiaonline.in/")
driver.find_element(By.ID,'signinuser').click()

#how to count number of text boxes having same class in web page
#find.elements is used to identigy multiple elements of same class
ele=driver.find_elements(By.CLASS_NAME,"floating-label")
print(len(ele))



