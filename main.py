import time
from selenium import webdriver
from datetime import datetime, timedelta


driver = webdriver.Firefox()

website = driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')

def check_for_unlocked_content():
    print("checking")
    unlocked_items = driver.find_elements_by_css_selector("#products .enabled")
    if len(unlocked_items) > 0:
        expensive_to_least = reversed(unlocked_items)
        for item in expensive_to_least:
            item.click()




start_time = datetime.now()

play = True

while play:
    try:
        cookie.click()
    except:
        time.sleep(3)
    finally:
        current_time = datetime.now()
        time_waited = timedelta(seconds=current_time.second - start_time.second)   
        if (time_waited.seconds % 5) == 0:
            check_for_unlocked_content()            
