
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

#check the single element
driver.find_element_by_id("isAgeSelected").click()

#check all the elements at once in one frame
driver.find_element_by_id("check1").click()
time.sleep(4)

#Radio Button demos

driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
driver.find_element_by_css_selector("input[value='Male']").click()
time.sleep(1)
driver.find_element_by_css_selector("input[value='Female']").click()
driver.find_element_by_id("buttoncheck").click()
