# 传说系列 · TalesOfVesperia（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：传说系列, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
传说系列系列《TalesOfVesperia》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：传说系列（Tales）
- **游戏**：TalesOfVesperia
- **品类**：JRPG
- **说明**：万代南梦宫的JRPG

### 元数据 (meta.json)

```json
{
  "game": "Tales of Vesperia",
  "series": "Tales",
  "year": 2008,
  "status": "in progress",
  "source": "https://hyouta.com/vesperia/",
  "alternativeMeasure": true,
  "sourceFeatures": {
    "type": "wiki",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "None"
  },
  "parserParameters": {
    "parser": "TalesOfVesperiaParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Yuri",
    "Repede",
    "Estelle",
    "Karol",
    "Rita",
    "Raven",
    "Judith",
    "Patty",
    "Flynn"
  ],
  "characterGroups": {
    "male": [
      "Adecor",
      "Alexei",
      "Alph",
      "Ba'ul",
      "Barbos",
      "Boccos",
      "Clay",
      "Clint",
      "Cumore",
      "Don Whitehorse",
      "Drake",
      "Duke",
      "Dyne",
      "Efreet",
      "Erungar",
      "Flynn",
      "Gnome",
      "Hanks",
      "Ioder",
      "Irmine",
      "Johann",
      "Joshua",
      "Jugem",
      "Karol",
      "Leblanc",
      "Markham",
      "Natz",
      "Nobis",
      "Pauly",
      "Ragou",
      "Raven",
      "Regaey",
      "Repede",
      "Sebastian",
      "Shel",
      "Teagle",
      "Ted",
      "Tison",
      "Tokunaga",
      "Tort",
      "Witcher",
      "Yeager",
      "Yu",
      "Yuri",
      "Zagi",
      "Agueron",
      "Astal",
      "Cruz",
      "Daniel",
      "Misomiso",
      "Cotton",
      "Dedecchi",
      "Giovanni",
      "Harry",
      "Jim",
      "Karolow X",
      "Lewis",
      "Miska",
      "Ohma",
      "Phaeroh",
      "Rich",
      "Seifer",
      "Shiva",
      "Sicily",
      "Sordeth",
      "Male Resident (Lower Quarter)",
      "Knight 1 (Zaphias)",
      "Knight 2 (Zaphias)",
      "Jail Knight",
      "Patrolling Knight (Zaphias)",
      "Castle Knight 1 (Zaphias)",
      "Castle Knight 2 (Zaphias)",
      "Castle Knight 3 (Zaphias)",
      "Castle Knight 4 (Zaphias)",
      "Zagi's Lackey",
      "Male Resident 2 (Lower Quarter)",
      "Male Resident 3 (Lower Quarter)",
      "Old Man (Lower Quarter)",
      "Merchant (Deidon Hold)",
      "Knight 1 (Deidon Hold)",
      "Knight 2 (Deidon Hold)",
      "Knight 3 (Deidon Hold)",
      "Knight 4 (Deidon Hold)",
      "Injured Boy (Deidon Hold)",
      "Harangued Knight (Deidon Hold)",
      "Knight 5 (Deidon Hold)",
      "Kaufman's Bodyguard",
      "Mayor of Halure",
      "Kid 1 (Halure)",
      "Kid 2 (Halure)",
      "Kid 3 (Halure)",
      "Shopkeeper (Halure)",
      "Male Resident 1 (Halure)",
      "Male Resident 2 (Halure)",
      "Male Resident 3 (Halure)",
      "Gate Knight 1 (Aspio)",
      "Gate Knight 2 (Aspio)",
      "Mage with Glasses (Aspio)",
      "Thief (Shaikos Ruins)",
      "Researcher (Ehmead Hill)",
      "Researcher 2 (Ehmead Hill)",
      "Knight 1 (Ehmead Hill)",
      "Knight 2 (Ehmead Hill)",
      "Man in Orange (Halure)",
      "Mercenary (Capua Nor)",
      "Accountant (Capua Nor)",
      "Mansion Guard (Capua Nor)",
      "Horned Helmet Mercenary (Capua Nor)",
      "Man in Inn (Capua Torim)",
      "Imperial Guard (Capua Torim)",
      "Innkeeper (Heliord)",
      "Man in red and blue (Heliord)",
      "Man in orange (Heliord)",
      "Hachette",
      "Drunk Man (Heliord)",
      "Wonder Chef",
      "Wonder Reporter",
      "Guy with Bandana (Dahngrest)",
      "Guy with Horned Helmet (Dahngrest)",
      "Man 1 (Dahngrest)",
      "Man 2 (Dahngrest)",
      "Man 3 (Dahngrest)",
      "Red Eye Thug (Dahngrest)",
      "Guild Member (HQ entrance)",
      "Blond Guild Member (Altosk)",
      "Brown-Haired Guild Member (Altosk)",
      "Spear-Wielding Guild Member (Altosk)",
      "Jail Guard (Barbos's)",
      "Old Man in Jail",
      "Jail Guard 2 (Barbos's)",
      "Ragou's Lackey",
      "Royal Escort",
      "Knight Guarding Labor Camp (Heliord)",
      "Shopkeeper (Heliord)",
      "Imperial Knight (Heliord)",
      "Scared Imperial Knight (Heliord)",
      "Labour Camp Guard 1 (Heliord)",
      "Labour Camp Prisoner 1 (Heliord)",
      "Knight reporting to Cumore (Heliord)",
      "Running Man 1 (Torim)",
      "Running Man 2 (Torim)",
      "Warehouse Man (Deidon Hold)",
      "Dice Master",
      "Dedecchi's Customer",
      "Little Wolf",
      "Warehouse Man (Torim)",
      "Batangi Fan",
      "Armed Man (Nordopolica)",
      "Interrupting Customer (Nordopolica)",
      "Street Brawler 1 (Nordopolica)",
      "Street Brawler 2 (Nordopolica)",
      "Man on the Docks (Nordopolica)",
      "Attacked Man on the Docks (Nordopolica)",
      "Coliseum Announcer",
      "Guild Member with Yellow Bandana",
      "Innkeeper (Mantaic)",
      "Imperial Knight (Mantaic)",
      "Imperial Knight 2 (Mantaic)",
      "Imperial Knight 3 (Mantaic)",
      "Alph and Layla's Dad",
      "Conscripted Man (Mantaic)",
      "Knight with Cumore (Mantaic)",
      "Kowz",
      "Ant Lion Man",
      "Desert Merchant",
      "Imperial Knight 1 (Weasand Blockade)",
      "Imperial Knight 2 (Weasand Blockade)",
      "Imperial Knight 3 (Weasand Blockade)
```

### 角色列表（共376个）

- "Yuri" :6594,
- "Karol" :3928,
- "Estelle" :3547,
- "Rita" :3546,
- "LOCATION" :3194,
- "Raven" :2385,
- "Judith" :2289,
- "Patty" :1396,
- "Flynn" :1206,
- "Repede" :445,
- "Duke" :269,
- "SYSTEM" :265,
- "Coliseum Announcer" :260,
- "Kaufman" :198,
- "Sicily" :145,
- "Leblanc" :143,
- "Alexei" :143,
- "Sodia" :140,
- "Ioder" :124,
- "Rich" :122,
- "Kowz" :118,
- "Don Whitehorse" :111,
- "Drake" :105,
- "Nan" :102,
- "Hanks" :100,
- "Krityan Elder" :96,
- "Lewis" :88,
- "Wonder Chef" :85,
- "Witcher" :81,
- "Karen" :79,
- "Coliseum Registration" :77,
- "Zagi" :77,
- "Cumore" :76,
- "Nobis" :75,
- "Natz" :75,
- "Spa Owner" :72,
- "Barbos" :68,
- "Adecor" :67,
- "Union Outpost (Dahngrest Tavern)" :66,
- "Mayor of Halure" :62,
- "Boccos" :62,
- "Sylph" :61,
- "Agueron" :60,
- "Yeager" :55,
- "Ragou" :54,
- "Krityan Child" :51,
- "Clint" :51,
- "Doctor" :50,
- "Barkeeper (Waitress Challenge)" :49,
- "Mimula" :49,
- ... 共376个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Tales/TalesOfVesperia/,True,Tales of Vesperia,Tales,TOTAL,32029,292007,87900,345241,-0.34322038525982634,103.44022743364292,6.5052997584716055,373
../data/Tales/TalesOfVesperia/,True,Tales of Vesperia,Tales,male,19626,181055,53223,213148,-0.3716754275666254,103.78633611059038,6.60496714139012,278
../data/Tales/TalesOfVesperia/,True,Tales of Vesperia,Tales,female,12260,109557,34273,130453,-0.2926919876697447,102.85454579046036,6.342620466638734,76
../data/Tales/TalesOfVesperia/,True,Tales of Vesperia,Tales,neutral,143,1395,403,1640,-0.36759856630824395,103.86347394540944,6.377604494072235,19

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
from bs4 import BeautifulSoup
import re,time
from os import path

baseURL = 'https://hyouta.com/vesperia/'

def openPage(url):
	req = Request(
		url, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)
	html = urlopen(req).read().decode('utf-8')
	return(html)

# MAIN STORY

mainStoryIndexURL = "https://hyouta.com/vesperia/?version=ps3p&locale=jp&compare=c2&section=scenario-index"
mainStoryIndexFileName = "raw/mainStoryIndex.txt"

if not path.exists(mainStoryIndexFileName):
	mainStoryIndexPage = openPage(mainStoryIndexURL)
	time.sleep(2)
	with open(mainStoryIndexFileName,'w') as wx:
		wx.write(mainStoryIndexPage)
else:
	mainStoryIndexPage = open(mainStoryIndexFileName).read()

soup = BeautifulSoup( mainStoryIndexPage, 'html5lib')

mainStoryIndexList = soup.find("div",{"class":"scenario-index"}, recursive=True)
mainStoryHREFs = mainStoryIndexList.find_all("a",recursive=True,href=True)
pnum = 1
for href in mainStoryHREFs:
	#print(href)
	hName = href['href']
	hName = hName[hName.index("name=")+5:].strip()
	print(hName)
	#fileName = "raw/page_"+str(pnum).zfill(5)+".html"
	fileName = "raw/page_"+ str(pnum).zfill(5)+"_"+ hName + ".html"
	if not path.exists(fileName):
		url = baseURL+href['href']
		page = openPage(url)
		time.sleep(2)
		with open(fileName, 'w') as fx:
			fx.write(page)
	pnum += 1

# SKITS
print("SKITS")

skitIndexURL = "https://hyouta.com/vesperia/?version=ps3p&locale=jp&compare=c2&section=skit-index"
skitIndexFileName = "raw/skitIndex.txt"
if not path.exists(skitIndexFileName):
	skitIndexPage = openPage(skitIndexURL)
	time.sleep(2)
	with open(skitIndexFileName,'w') as wx:
		wx.write(skitIndexPage)
else:
	skitIndexPage = open(skitIndexFileName).read()
	
	
soup = BeautifulSoup( skitIndexPage, 'html5lib')

skitTable = soup.find("div",{"id":"content"}).find("table").find("tbody")
skitIndexList = []
for row in ski
```


## 策划参考价值
JRPG类型的对话叙事参考。万代南梦宫的JRPG
