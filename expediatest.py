
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver")

driver.get("https://www.expedia.com/Flights-Search?flight-type=on&starDate=06%2F06%2F2019&endDate=06%2F08%2F2019&mode=search&trip=roundtrip&leg1=from%3ASan+Francisco%2C+CA+%28SFO-San+Francisco+Intl.%29%2Cto%3ANew+York+%28NYC-All+Airports%29%2Cdeparture%3A06%2F06%2F2019TANYT&leg2=from%3ANew+York+%28NYC-All+Airports%29%2Cto%3ASan+Francisco%2C+CA+%28SFO-San+Francisco+Intl.%29%2Cdeparture%3A06%2F08%2F2019TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY")

driver.implicitly_wait(5)

drp=Select(driver.find_element_by_id("sortDropdown"))
drp.select_by_index(2)

print(len(drp.options))

all_opt=drp.options
for i in all_opt:
    print(i.text)