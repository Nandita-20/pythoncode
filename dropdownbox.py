from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
ele=driver.find_element_by_id("select-demo")
drp=Select(ele) #select class object to call the elements

#select by index number
drp.select_by_index(5)
time.sleep(2)

#select by value
drp.select_by_value("Monday")
time.sleep(1)

#select by visible test
drp.select_by_visible_text('Wednesday')

#count all the items in drop down and print

print(len(drp.options))

#capture all the options from drop down and print then
all_options=drp.options
#here we stored all th option in variable but since there are multiple options we need to print so will use for loop

for i in all_options:
    print(i.text)

driver.close()