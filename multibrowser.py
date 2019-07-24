from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#calling chrome web driver
#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

#calling IE driver
driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_x64_3.14.0\IEDriverServer")

# calling some methods through driver as we are working with chrome driver

driver.get("http://www.appdynamics.com/")
print(driver.title,driver.current_url) #display the title of the browser and URL of Applicaton
#print(driver.current_url)
driver.close() #close the browser





