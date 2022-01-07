import time
from utils import find_element, get_driver

driver = get_driver()

driver.get("https://office.com/login")
time.sleep(3)
find_element(driver, "input[type=email]").send_keys("amoud@amoud.ca")
find_element(driver, "input[type=submit]").click()
try:
    time.sleep(3)
    find_element(driver, '#usernameError')
    print("notfound")
except:
    print("found")