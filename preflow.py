from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_driver():
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com.tw")
    elem = driver.find_element_by_id("email")
    i = input("email : ")
    elem.send_keys(i)
    elem = driver.find_element_by_id("pass")
    i = input("pass : ")
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    return driver


