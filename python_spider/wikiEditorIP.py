from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random
from urllib.error import HTTPError, URLError
import json

random.seed(datetime.datetime.now())

#返回词条所有内部链接
def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile(r"^(/wiki/)((?!:).)*$"))

#编辑历史IP地址主函数
def getHistoryIps(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "https://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("History URL is:" + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    ipAdresses = bsObj.findAll("a", {"class": "mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipAdress in ipAdresses:
        addressList.add(ipAdress.get_text())
    return addressList
'''
links = getLinks("/wiki/Python_(programming_language)")

while (len(links) > 0):
    for link in links:
        print("-------------------------------")
        historyIps = getHistoryIps(link.attrs['href'])
        for historyIp in historyIps:
            print(historyIp)

    newLink = links[random.randint(0, len(links)-1)].attrs["href"]
    links = getLinks(newLink)
'''

def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("-----------------------")
        historyIPs = getHistoryIps(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + " is from " + country)
    newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
    links = getLinks(newLink)