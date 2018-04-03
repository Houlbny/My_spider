from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps


def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x < 143 else 255)
    borderImage = ImageOps.expand(image, border=20, fill="white")
    borderImage.save(imagePath)

html = urlopen("http://www.pythonscraping.com/humans-only")
bsObj = BeautifulSoup(html, "html5lib")

#收集需要处理的表单数据
imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
formBuildId = bsObj.find("input", {"name", "form_build_id"})["value"]
captchaSid = bsObj.find("input", {"name", "captcha_sid"})["value"]
captchaToken = bsObj.find("input", {"name", "captcha_token"})["value"]

captchaUrl = "http://pythonscraping.com" + imageLocation
urlretrieve(captchaUrl, "captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(["tesseract", "captch.jpg", "captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt", "r")

#清理识别结果中的空格和换行符
captchaResponse = f.read().replace(" ", "").replace("\n", "")
print("captcha solution attempt:" + captchaResponse)

if len(captchaResponse) == 5:
    params = {"captcha_token": captchaToken, "capthca_sid": captchaSid, "form_id": "comment_node_page_form", "form_build_id": formBuildId, "captcha_response": captchaResponse, "name": "Ryan", "subject": "I come to seek the Grail", "comment_body[und][0][value]": "and i am...."}
    r = requests.post("http://www.pythonscraping.com/comment/reply/10", data=params)
    responseObj = BeautifulSoup(r.tetx)
    if responseObj.find("div", {"class": "messages"}) is not None:
        print(responseObj.find("div", {"class": "messages"}).get_text())
else:
    print("there was a problem")

