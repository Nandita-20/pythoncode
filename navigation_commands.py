#requirement; we have to open one application then another application in same tab,
# then open first app then again open the second app on same tab.
# for navigation we can use Back() and Forward methods

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.amazon.in/")
driver.fullscreen_window()
print(driver.title)
driver.get("https://www.flipkart.com/")
driver.fullscreen_window()
print(driver.title)
time.sleep(5)
driver.back() #again open www.amazon.com
driver.fullscreen_window()
print(driver.title)
time.sleep(5)
driver.forward() #again open www.myhcl.com
driver.fullscreen_window()
time.sleep(5)
print(driver.title)

driver.close()