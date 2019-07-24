from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.facebook.com/")
driver.fullscreen_window()
time.sleep(1)


user_ele = driver.find_element_by_id('email')

user_ele.send_keys('9650249700')
print("User_Email_Id_Entered")
time.sleep(1)
pass_ele = driver.find_element_by_id('pass')
pass_ele.send_keys('testing123')
print("Password is entered")
time.sleep(1)

login_click = driver.find_element_by_id("loginbutton")
login_click.click()

print("Login Done")
input("Press anything to quit")
driver.quit()
print("Finished")