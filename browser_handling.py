from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

print(driver.current_window_handle) # parent window: CDwindow-C81C88F4C071DD632343F441662DF417

handle=driver.window_handles # returns all the handle values for opened browser windows

for i in handle:
    driver.switch_to_window(i)
    print(driver.title)
    if driver.title=="Frames & windows": #close only parent window
        driver.close()

#driver.close() # it will close  last opened browser