from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("https://freecrm.com/")

driver.find_element_by_xpath("/html/body/div[1]/header/div/nav/div[2]/div/div[3]/ul/a").click()

driver.find_element_by_name("email").send_keys("nanditasrivastava87@gmail.com")
driver.find_element_by_name("password").send_keys("Test@123")
driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div/div[3]").click()
