from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import numpy as np
from slackclient import SlackClient
import os

# TEST_BOT_TOKEN = "xoxb-27173653120-1274574860293-SPQsVMNMQdG7NUh1Tp67ONSU"
#
#
# slack_client = SlackClient(os.environ.get('TEST_BOT_TOKEN'))
# test_bot_id = None
#
# RTM_READ_DELAY


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://cityofla.ezlinksgolf.com/index.html#/preSearch")
#print(driver.title)

search_button = driver.find_element_by_xpath("//button[@type = 'submit']")
#search_button
search_button.click()

time.sleep(1)

find_date_input = driver.find_element_by_id("dateInput")
find_date_input.clear()
# TO DO: Have this date be an input
time.sleep(2)
find_date_input.send_keys("08/03/2020") # Need to change this to an input
find_date_input.send_keys(Keys.TAB)
time.sleep(2)
find_num_players = driver.find_element_by_id("pc")
find_num_players.click()

# TO DO: allow to select number of players
find_num_players.send_keys(Keys.ARROW_UP) ## Need to do to select num players
find_num_players.send_keys(Keys.RETURN) ## close the dialogue box
#time.sleep(2)
# TO DO Creating a lookup dictionary for courses
#course_dict = {"Griffith Park - Harding": 5997, "Griffith Park - Wilson": 5998}

# TO DO need to iterate amongst length of list of inputs and feed to value field


course_select = driver.find_elements_by_xpath("//input[@title='Select a course' and @value='5998']")[0]
course_select.click()
time.sleep(2)
course_select = driver.find_elements_by_xpath("//input[@title='Select a course' and @value='5997']")[0]
course_select.click()

search_button = driver.find_element_by_xpath("//button[@type = 'submit']")
#search_button
search_button.click()

#wait for page to load
#try:
    #element = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.LINK_TEXT, "SOME LINK TEXT")) # TO.DO need to change link text info
    #)
##    driver.quit()

##########################

# Pulling times from the site for each course
time.sleep(4)
tee_time = driver.find_element_by_class_name("tee-time-block")
tee_txt = tee_time.text

tee_text_list = tee_txt.split("\nVIEW") #Splitting on the view string to get list of times

tee_list_list = [i.split("\n") for i in tee_text_list if i]
tee_list_list

for list in tee_list_list:
    if list[0] == '':
        list[:] = list[1:] # for item in list if item]

print(tee_list_list)

tee_times_df = pd.DataFrame(tee_list_list, columns = ['Course', 'Time', 'Price', 'Players'])

tee_times_df.astype(tee_types)


# ID, class, name, tag
# Hierarchy of properties to search by
# ID -> Name -> class
# When do you want to play (ID = "dateInput")

time.sleep(5)

driver.quit()
