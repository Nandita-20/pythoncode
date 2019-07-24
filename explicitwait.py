from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")
driver.delete_all_cookies()
driver.implicitly_wait(5)
driver.fullscreen_window()
driver.get("https://www.expedia.com/")


#driver.find_element_by_id("tab-flight-tab-hp").click()

#click on flight button
driver.find_element(By.ID,"tab-flight-tab-hp").click() #another approach to identify the element
time.sleep(1)

driver.find_element(By.ID,"flight-type-roundtrip-label-hp-flight").click() #clcik on round way option button

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO") #origin

time.sleep(2)

driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC") #Destination

driver.find_element(By.ID,"flight-departing-hp-flight").clear()
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("06/08/2019") #pass the travel date
time.sleep(1)
driver.find_element(By.ID,"flight-returning-hp-flight").clear()
time.sleep(1)
driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("06/08/2019")
#time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

#/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]/section[1]/form/div[7]/label/button

wait = WebDriverWait(driver,10)  #webdriver explicit wait definition
element=wait.until(EC.element_to_be_clickable(By.XPATH,"//*[@id='stopFilter_stops-0']"))
element.click() #perform click operation once element gets visible
time.sleep(3)



