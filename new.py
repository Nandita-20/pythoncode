from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.naukri.com/account/register/basicdetails")
driver.find_element(By.CLASS_NAME,'fresherCont').click()

driver.find_element_by_css_selector("input[for='Outside India']").click()

#driver.find_element_by_css_selector("input[value='Female']").click()