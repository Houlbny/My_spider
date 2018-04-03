from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

#输入数据的清洗函数

def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(" ")
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


# n-gram函数

def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html5lib")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2-gram count is:" + str(len(ngrams)))

