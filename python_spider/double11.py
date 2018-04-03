import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver
from selenium.webdriver import ActionChains
import datetime
import requests

#脚本于2017-11-11开始
'''
startDate = datetime.date(2017-11-11)
b = datetime.datetime.now().date()
while b != startDate:
    b = datetime.datetime.now().date()
'''

#create new webdriver
driver = webdriver.Firefox()
driver.get("https://login.taobao.com")
while "iconfont static" in driver.find_element_by_id("J_Quick2Static").get_attribute("class"):
    driver.find_element_by_id("J_Quick2Static").click()
    break

driver.find_element_by_id("TPL_username_1").send_keys("ahh1119")
driver.find_element_by_id("TPL_password_1").send_keys("mm19621022")
time.sleep(2)
simpleBreak = driver.find_element_by_id("nc_1_n1z")
action = ActionChains(driver)
action.click_and_hold(simpleBreak)
action.move_by_offset(130, 0)
action.move_by_offset(100, 0)
action.move_by_offset(100, 0)
action.release().perform()
time.sleep(1)

driver.find_element_by_id("J_SubmitStatic").click()
time.sleep(2)
driver.close()


