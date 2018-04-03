from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("div")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out")
            print(count)
            return
        time.sleep(.5)
        try:
            elem ==driver.find_element_by_tag_name("div")
        except StaleElementReferenceException:
            print(count)
            return

driver = webdriver.Firefox()
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
