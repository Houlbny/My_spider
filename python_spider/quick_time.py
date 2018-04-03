from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://202.121.199.138/Course/Index.asp?System=CSCI")
driver.implicitly_wait(2)
driver.find_element_by_xpath("/html/body/table/tbody/tr[1]/td/p/map/area[1]").click()
driver.find_element_by_name("id").send_keys("17721796")
driver.implicitly_wait(2)
driver.find_element_by_name("pwd").send_keys("Houl1202")
time.sleep(2)
driver.find_element_by_name("enter").click()
driver.implicitly_wait(1)

count = 0
while count <= 130:
    driver.refresh()
    count += 1
    time.sleep(1)

driver.close()
