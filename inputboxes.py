from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.naukri.com/account/register/basicdetails")
driver.find_element(By.CLASS_NAME,'fresherCont').click()

#how to get the status of various test boxes
firstname=driver.find_element(By.ID,"fname").is_displayed()
print(" first name display or not",firstname)
print("enabled or not",driver.find_element(By.ID,"email").is_enabled())
print(" email is enabled or not",driver.find_element(By.NAME,"password").send_keys("P@wer45"))

#how to provide values in text boxes
driver.find_element(By.ID,"fname").send_keys("Pawan")
driver.find_element(By.ID,"email").send_keys("pawan.pwer@rediffmail.com")
driver.find_element(By.NAME,"password").send_keys("P@wer45")
