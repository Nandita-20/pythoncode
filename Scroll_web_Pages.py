from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("https://www.indiaonline.in/")

driver.maximize_window()

#scroll down page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#scroll down till the element i.e Latest News not found

#icon=driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div[1]/div/div[7]/h2/a")
#driver.execute_script("arguments[0].scrollIntoView();",icon)'''

#scroll down till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)
driver.close()
