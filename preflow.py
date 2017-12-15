from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_facebook(driver):
    driver.get("https://www.facebook.com.tw")
    elem = driver.find_element_by_id("email")
    i = input("email : ")
    elem.send_keys(i)
    elem = driver.find_element_by_id("pass")
    i = input("pass : ")
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    try:
        elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='q']"))
        )
    except:
        driver.quit()

    return

def go_event_page(driver, domain, path):
    driver.get("https://tixcraft.com/user/changeLanguage/lang/zh_tw")
    driver.get("https://tixcraft.com/login/facebook")
    driver.get(domain + path)
    return

