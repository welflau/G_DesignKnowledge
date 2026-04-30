# 火焰纹章 · FireEmblemThreeHouses（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：火焰纹章, SRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：SRPG

## 概述
火焰纹章系列《FireEmblemThreeHouses》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：火焰纹章（FireEmblem）
- **游戏**：FireEmblemThreeHouses
- **品类**：SRPG
- **说明**：任天堂SRPG，支援对话+分支剧情

### 元数据 (meta.json)

```json
{
  "game": "Fire Emblem: Three Houses",
  "series": "Fire Emblem",
  "year": 2019,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "https://houses.fedatamine.com",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "parserParameters": {
    "parser": "FireEmblem3HParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Byleth"
  ],
  "characterGroups": {
    "male": [
      "Byleth",
      "Dimitri",
      "Hanneman",
      "Raphael",
      "Lorenz",
      "Yuri",
      "Gilbert",
      "Linhardt",
      "Balthus",
      "Jeritza",
      "Hubert",
      "Ashe",
      "Seteth",
      "Cyril",
      "Felix",
      "Dedue",
      "Ignatz",
      "Sylvain",
      "Caspar",
      "Claude",
      "Ferdinand",
      "Alois",
      "Jeralt"
    ],
    "female": [
      "Annette",
      "Anna",
      "Flame Emperor",
      "Flayn",
      "Judith",
      "Shamir",
      "Hapi",
      "Leonie",
      "Edelgard",
      "Cornelia",
      "Ingrid",
      "Rhea",
      "Sothis",
      "Catherine",
      "Monica",
      "Kronya",
      "Mercedes",
      "Marianne",
      "Hilda",
      "Manuela",
      "Constance",
      "Lysithea",
      "Dorothea",
      "Petra",
      "Bernadetta"
    ]
  },
  "aliases": {}
}
```

### 角色列表（共167个）

- "ACTION" :8953,
- "Byleth" :6043,
- "LOCATION" :5050,
- "CHOICE" :2872,
- "Claude" :2331,
- "Dimitri" :2068,
- "Edelgard" :1831,
- "Seteth" :1493,
- "Hilda" :1206,
- "Ferdinand" :1118,
- "Linhardt" :1098,
- "Mercedes" :1088,
- "Bernadetta" :1080,
- "Dorothea" :1066,
- "Annette" :1065,
- "Sylvain" :1057,
- "Ingrid" :1048,
- "Lysithea" :1043,
- "Lorenz" :1002,
- "Ashe" :1002,
- "Caspar" :972,
- "Yuri" :971,
- "Constance" :946,
- "Hubert" :944,
- "Catherine" :934,
- "Ignatz" :927,
- "Leonie" :925,
- "Flayn" :923,
- "Felix" :921,
- "Petra" :897,
- "Raphael" :884,
- "Rhea" :884,
- "Hanneman" :861,
- "Marianne" :860,
- "Manuela" :859,
- "Balthus" :850,
- "Monk" :837,
- "Shamir" :807,
- "Alois" :790,
- "Gilbert" :763,
- "Hapi" :737,
- "Dedue" :732,
- "Cyril" :655,
- "Anna" :489,
- "Sothis" :375,
- "Knight of Seiros" :305,
- "Jeritza" :244,
- "Soldier" :227,
- "Rodrigue" :220,
- "Jeralt" :219,
- ... 共167个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FireEmblem/FireEmblemThreeHouses/,True,Fire Emblem: Three Houses,Fire Emblem,TOTAL,51372,617131,148689,755538,0.4751318804117233,99.04860343669826,6.3070767417104605,164
../data/FireEmblem/FireEmblemThreeHouses/,True,Fire Emblem: Three Houses,Fire Emblem,male,27878,315819,75628,386501,0.47952561556545525,99.06246987228403,6.336927277641099,23
../data/FireEmblem/FireEmblemThreeHouses/,True,Fire Emblem: Three Houses,Fire Emblem,female,19345,245291,59735,299870,0.437048941460926,99.24298119712768,6.2239522688878965,25

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re,time
import os


def openPage(url):
	req = Request(
		url, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)
	html = urlopen(req).read().decode('utf-8')
	html = BeautifulSoup(html, 'lxml')
	html = html.find("main")
	return(html)
	


# Dummy file for parser
with open("raw/dummyFile.html", "w") as file:
	file.write("dummy")

# Download scenarios
baseURL = "https://houses.fedatamine.com/en-uk/"
rawFolder = "raw/en-uk/"

pageCategories = [("scenarios",370),("monastery",84)]

for cat,maxi in pageCategories:
	folder = rawFolder + cat+"/"
	if not os.path.exists(folder):
		os.mkdir(folder)
	for i in range(maxi):
		fileName = folder + str(i)+".html"
		print(fileName)
		if not os.path.exists(fileName):
			pageURL = baseURL + cat + "/"+ str(i)
			try:
				data = openPage(pageURL)
				with open(fileName, "w") as file:
					file.write(str(data))
			except HTTPError:
				print("ERROR " + pageURL)
				with open(fileName, "w") as file:
					file.write("")				
			time.sleep(2)
	
# Support conversations
allLinks = []
supportLinksFile = "raw/en-uk/links/supportLinks.txt"
if not os.path.exists(supportLinksFile):
	supportIndex = openPage("https://houses.fedatamine.com/en-uk/supports/")
	links = supportIndex.find_all("a")
	links = [x["href"] for x in links if x["href"].startswith("/en-uk/supports/")]
	links = list(set(links))

	allLinks = []
	for link in links:
		html = ""
		blinkFileName = "raw/en-uk/links/"+link.replace("/","_")[1:]
		if os.path.exists(blinkFileName):
			p = open(blinkFileName).read()
			linkIndex = BeautifulSoup(p, 'lxml')
			linkIndex = linkIndex.find("main")
		else:
			print("https://houses.fedatamine.com" + link)
			linkIndex = openPage("https://houses.fedatamine.com" + link)
			time.sleep(2)
			with open(blinkFileName, "w") as file:
				file
```


## 策划参考价值
SRPG类型的对话叙事参考。任天堂SRPG，支援对话+分支剧情
