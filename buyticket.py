import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

def find_game_path(driver, domain):
    elems = driver.find_elements_by_css_selector("a[target='_new']")
    url = ""
    for elem in elems:
        if "/activity/game" in elem.get_attribute("href"):
            url = elem.get_attribute("href")
            break
    return url

def buy_ticket(driver, domain, path):
    buttons = []
    while len(buttons) == 0:
        print("accessing buttons...")
        time.sleep(0.001)
        response = requests.get(domain + path)
        soup = BeautifulSoup(response.content, "html.parser")
        buttons = soup.find_all("input", type="button")
    button = buttons[0] if len(buttons) == 1 else buttons[1]
    driver.get(domain + button.get("data-href"))
    return driver.execute_script("return areaUrlList[$(\"li[class='select_form_b'] > a:last\").attr(\"id\")]")

def confirm_ticket(driver, domain, path):
    driver.get(domain + path)
    select = Select(driver.find_element_by_css_selector("select"))
    select.select_by_index(1)
    driver.find_element_by_id("TicketForm_agree").click()
    i = input("verify code : ")
    while i == "q":
        elem = driver.find_element_by_id("yw0")
        elem.click()
        i = input("verify code : ")
    elem = driver.find_element_by_id("TicketForm_verifyCode")
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    return


