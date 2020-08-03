from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os

#Find the browser and make it not open
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")

def navigate(siteName, PATH, chrome_options):
    """Opens webbrowser per the definitions above and navigates to site
    sitename = "https://cityofla.ezlinksgolf.com/index.html#/preSearch" """
    # open browser silently
    driver = webdriver.Chrome(PATH, options=chrome_options)
    # navigate to the proper website
    driver.get(siteName)
    time.sleep(2)
    if (!driver.title):
        print("Site failed to load")

def click_search():
    """ Method to click the search button. Need to do once upon entering site
    and another time to search after selecting options """

    search_button = driver.find_element_by_xpath("//button[@type = 'submit']")
    #search_button
    search_button.click()

def change_date(date):
    #Finds and clears date
    find_date_input = driver.find_element_by_id("dateInput")
    find_date_input.clear()
    find_date_input.send_keys(date) # Need to change this to an input
    find_date_input.send_keys(Keys.TAB)

def change_players(players):
    find_num_players = driver.find_element_by_id("pc")
    find_num_players.click()
    clicks = 4 - players
    direction = 'up'
    if clicks < 0:
        clicks = -clicks
        direction = 'down'
    click(clicks, direction)
    # close the dialogue box
    find_num_players.send_keys(Keys.RETURN)

def click(num, direction = 'up'):
    if direction == 'up':
        for i in range(num):
            find_num_players.send_keys(Keys.ARROW_UP)
    else:
        for i in range(num):
            find_num_players.send_keys(Keys.ARROW_DOWN)

def select_courses(*args):
    for i in args:
        xpath = "//input[@title='Select a course' and @value='" + str(i) + "']"
        course_select = driver.find_elements_by_xpath(xpath)[0]
        course_select.click()


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

tee_times_df = pd.DataFrame(tee_list_list, columns = ['Course', 'Time', 'Price', 'Players'])
tee_times_df


# ID, class, name, tag
# Hierarchy of properties to search by
# ID -> Name -> class
# When do you want to play (ID = "dateInput")

time.sleep(5)

driver.quit()
