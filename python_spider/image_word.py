import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

#create new webdriver
driver = webdriver.Firefox()

driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

#click_button
driver.find_element_by_id("img-canvas").click()
imageList = set()

time.sleep(5)

while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
    driver.find_element_by_id("sitbReaderRightPageTurner").click()
    time.sleep(2)
    pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)


driver.quit()

#deal with URL of Images
for image in sorted(imageList):
    urlretrieve(image, "/Users/apple/Downloads/XLDownload/page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())

