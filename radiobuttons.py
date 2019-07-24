from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("http://admser.chd.nic.in/rlaapt/home.aspx")

#working with radio button
print("Male is selected or not=>",driver.find_element_by_id("MainContent_rblGender_0").is_selected()) #verify that male check box is selected and return the value

#verify thar whether female radio button is selcted or not
print("female is selected or not =>",driver.find_element_by_id("MainContent_rblGender_1").is_selected())

#after verify, click on the female radio button
driver.find_element_by_id("MainContent_rblGender_1").click()

#after clcik on female radion button display the status
print("female is selected or not =>",driver.find_element_by_id("MainContent_rblGender_1").is_selected())

drp=Select(driver.find_element_by_id("MainContent_ddlServiceList"))
drp.select_by_index(2)
