from selenium import webdriver
from preflow import *
from buyticket import *
import time
import sched, time

s = sched.scheduler(time.time, time.sleep)

domain = "https://tixcraft.com"
event_path = "/activity/detail/2018_Mayn"
#event_path = "/activity/detail/2018_GLAY"

def waited_funcs(url):
    href = buy_ticket(driver, domain, url[len(domain):])
    print(domain + href)
    confirm_ticket(driver, domain, href)


driver = webdriver.Firefox()
login_facebook(driver)
go_event_page(driver, domain, event_path)
url = find_game_path(driver, domain)
print(url)

formattime = "2017 12 16 10:59:55"
timestamp = time.mktime(time.strptime(formattime,"%Y %m %d %H:%M:%S"))

s.enterabs(timestamp, 100, waited_funcs, kwargs={'url': url})
s.run()

