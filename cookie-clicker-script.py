'''
============================================================================
Welcome to this simple Cookie Clicker Script I made myself for fun.
Perhaps I can make it OOP later...
It literally plays itself-- amazing I am no longer addicted to this game !
============================================================================
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions() # Setting Up Selenium
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID, value="cookie")

def get_cookie_count() -> int:
    '''Gets current balance'''
    return int(driver.find_element(By.ID, value="money").text)

def get_cheapest_price() -> int:
    '''Returns index of the most affordable price'''
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    store_prices = [int(item.text.split("- ")[-1].replace(",", "")) for item in store_items if item.text != ""]
    return store_prices.index(min(store_prices))

def buy_upgrade(cookie_index:int) -> None:
    '''Buys most affordable item'''
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
    store_items[cookie_index].click() 
    

game_is_on = True # Main Section
start_time = int(time.time()) # The time that's passed since the epoch just in case it wasn't obvious
while game_is_on:
    time.sleep(0.01) # It crashed unless I made it as such, feel free to prove me wrong 
    now = int(time.time())
    cookie_button.click()
    if (now - start_time) % 5 == 0: # Checks every five seconds-- Yes, I know it may not be efficient late game...
        buy_upgrade(get_cheapest_price())


