from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内部链接的列表
def getInternalLinks(bsObj, includerUrl):
    includerUrl = urlparse(includerUrl).scheme + "://" + urlparse(includerUrl).netloc
    internalLinks = []
    #找出所有”/“开头的链接
    for link in bsObj.findAll("a", href=re.compile(r"^(/|.*"+includerUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includerUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


#获取页面所有外部链接列表
def getExternalLinks(bsObj, excluderUrl):
    externalLinks = []
    #找出所有以”http“或”www“开头且不含当前URl的链接
    for link in bsObj.findAll("a", href=re.compile(r"^(http|www)((?!"+excluderUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html5lib")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No externalLinks, look for the site for me")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is:" + externalLink)
    followExternalOnly(externalLink)

allExtLinks = set()
allIntLinks = set()

def getAllLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取URl：" + link)
            allIntLinks.add(link)
            getAllLinks(link)


getAllLinks("http://www.hao123.com/")