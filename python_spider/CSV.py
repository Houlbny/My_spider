#忽略一些HTML元素之后写入CSV

import csv
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup

html = urlopen(quote("https://baike.baidu.com/item/文本编辑器/8853160", safe='/:'))
bsObj = BeautifulSoup(html, "html5lib")


table = bsObj.find("table", {"class": "table-view log-set-param"})
rows = table.findAll("tr")

csvFile = open("/Users/apple/Downloads/XLDownload/editor.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll("td"):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

