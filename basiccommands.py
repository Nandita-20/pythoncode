# Requirement: this program is used to call child windows using xpath and click button by inspect element of button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.get("https://www.amazon.in")
driver.fullscreen_window() #open the application in full screen mode
print(driver.title)
print(driver.current_url)
#open the child window by click on Sign in secyrely button and pass xpath by inpect element
driver.find_element_by_xpath("//*[@id='a-autoid-0-announce']").click()
time.sleep(5) #just in wait mode for child window
#driver.close() #focus only on current browser
driver.quit() #quits all the browser including parent and child

