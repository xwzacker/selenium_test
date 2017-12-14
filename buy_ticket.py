import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def get_ready(driver, domain, url):
    driver.get("https://tixcraft.com/user/changeLanguage/lang/zh_tw")
    driver.get("https://tixcraft.com/login/facebook")


def buy_ticket(driver, domain, url):
    driver.get(url)
    elems = driver.find_elements_by_css_selector("a[target='_new']")
    href = ""
    for elem in elems:
        if "/activity/game" in elem.get_attribute("href"):
            href = elem.get_attribute("href")
            break

    response = requests.get(href)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons = soup.find_all("input", type="button")
    driver.get(domain + buttons[1].get("data-href"))
    elem = driver.find_element_by_css_selector("li[class='select_form_b'] > a")
    return driver.execute_script("return areaUrlList[$(\"li[class='select_form_b'] > a\").attr(\"id\")]")


def confirm_ticket(driver, domain, url):
    driver.get(url)
    select = Select(driver.find_element_by_css_selector("select"))
    select.select_by_index(1)
    driver.find_element_by_id("TicketForm_agree").click()
    i = input("verify code : ")
    elem = driver.find_element_by_id("TicketForm_verifyCode")
    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    return


