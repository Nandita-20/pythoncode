from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.amazon.in/")
driver.fullscreen_window()
time.sleep(1)

driver.find_element_by_id('a-autoid-0-announce').click()
user_ele=driver.find_element_by_id('ap_email')
user_ele.send_keys('ravisheee@gmail.com')
time.sleep(1)
continue_ele=driver.find_element_by_id('continue')
continue_ele.click()
pass_ele=driver.find_element_by_id('ap_password')
pass_ele.send_keys('yaadrakho@19')
time.sleep(1)
check_ele=driver.find_element_by_css_selector("input[value=true]")#will give the status of checkbox whether selected or not
print(check_ele.is_selected())
sign_in=driver.find_element_by_id('signInSubmit')
sign_in.click()
time.sleep(1)
driver.quit()