from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))
print("-------------------------")

wordObj = BeautifulSoup(xml_content.decode('utf-8'), "html5lib")
print(wordObj)
textStrings = wordObj.findAll("w:t")
print(textStrings)
for textElem in textStrings:
    print(textElem.text)

# 打印不出docx内容 待修正
