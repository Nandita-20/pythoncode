#implicit wait is based on time , sometime if in defined time page is not uploaded then erroe might be happened like
# element not found, so we have an option of using explicit wait because explicit wait is based on condition not time.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.amazon.in/")
driver.fullscreen_window()
print(driver.title)

#assert is used for debugging process, here used to verfiy that given title match with driver.title, if matches then
#wait for 10 second to synchronize code and application response, so that we can avoid error like element not found.

assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" in driver.title

#it will wait for 10 second and it will be applied on all the elements of driver as it is defined at the beginning
driver.implicitly_wait(10)

driver.find_element_by_id('a-autoid-0-announce').click()
user_ele=driver.find_element_by_id('ap_email').send_keys('ravisheee@gmail.com')

continue_ele=driver.find_element_by_id('continue')
continue_ele.click()
pass_ele=driver.find_element_by_id('ap_password').send_keys('yaadrakho@19')

check_ele=driver.find_element_by_css_selector("input[value=true]")#will give the status of checkbox whether selected or not
print(check_ele.is_selected())
sign_in=driver.find_element_by_id('signInSubmit')
sign_in.click()

driver.quit()