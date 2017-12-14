from preflow import *
from buy_ticket import *
import time

domain = "https://tixcraft.com"
#event_path = "/activity/detail/2018_Mayn"
event_path = "/activity/detail/2018_GLAY"

driver = get_driver()

time.sleep(10)

get_ready(driver, domain, domain + event_path)
link = buy_ticket(driver, domain, domain + event_path)
confirm_ticket(driver, domain, domain + link)

