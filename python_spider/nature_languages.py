from urllib.request import  urlopen
from bs4 import BeautifulSoup
import re
import string
import operator
from random import randint

def cleanInput(input):
    input = re.sub('\n+', " ", input).lower()
    input = re.sub("\[[0-9]*\]", "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
        # 这里统计频率 没有则新建
    return output

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)

#生成马尔科夫链组成的句子
def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum

def retrieveRandomWord(wordList):

    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(text):
    #剔除换行符和引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " "+symbol+" ")

    words = text.split(" ")
    words = [word for word in words if word != ""]

    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1

    return wordDict

text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), "utf-8")
wordDict = buildWordDict(text)

#生成链长为100的马尔科夫链
length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord+" "
    currentWord = retrieveRandomWord(wordDict[currentWord])
print("\n")
print(chain)
