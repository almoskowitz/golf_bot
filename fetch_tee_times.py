from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://cityofla.ezlinksgolf.com/index.html#/preSearch")
print(driver.title)

find_date_input = driver.find_element_by_id("dateInput")
find_date_input.clear()
find_date_input.send_keys("08/03/2020")
find_date_input.send_keys(Keys.RETURN)

# ID, class, name, tag
# Hierarchy of properties to search by
# ID -> Name -> class
# When do you want to play (ID = "dateInput")

time.sleep(5)


driver.quit()
