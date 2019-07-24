from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://www.expedia.com/")

links=driver.find_elements(By.TAG_NAME,"a")

print("No of links present in web page",len(links))

for i in links:
    print(i.text)

#driver.find_element(By.LINK_TEXT,"Add your property").click()

driver.find_element(By.PARTIAL_LINK_TEXT,"Ad").click() #it must be part of link text and is case sensitive also.