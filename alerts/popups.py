from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/button').click()
time.sleep(2)
driver.switch_to_alert().accept()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/button').click()
time.sleep(1)
driver.switch_to_alert().dismiss()
