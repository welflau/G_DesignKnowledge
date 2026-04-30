# 最终幻想 · FFXIV（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXIV》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXIV
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy XIV",
  "series": "Final Fantasy",
  "year": 2010,
  "status": "ready",
  "source": "https://ffxiv.gamerescape.com",
  "sourceFeatures": {
    "type": "wiki",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "Dialogue varies based on PC origin; not all variations captured.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "characterInfoSource": "https://ffxiv.gamerescape.com",
  "parserParameters": {
    "parser": "GamerescapeParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "The Adventurer"
  ],
  "characterGroups": {
    "playerChoice": [
      "The Adventurer"
    ],
    "male": [
      "Latgar",
      "Amelain",
      "Komuxio",
      "Rolfe Hawthorne",
      "Brass Blade",
      "Draggle-tailed Refugee",
      "Hahasako",
      "Boorish Banneret",
      "Gegeruju",
      "Serpent Herald",
      "Fearful Citizen",
      "Moren",
      "Lamberteint",
      "Drunken Duskwright",
      "Wood Wailer",
      "Asgeir",
      "Nathelain",
      "Marcechamp",
      "Willfort",
      "Todden",
      "Gisilbehrt",
      "Distressed Soldier",
      "House Durandaire Knight",
      "Stupefied Citizen",
      "Imperial Magitek Engineer",
      "Bubukkuli",
      "Zanthael",
      "Atharn",
      "Owen",
      "House Haillenarte Knight",
      "Ishgardian Priest",
      "Spectral Swordsman",
      "Glaumunt",
      "Roger",
      "House Fortemps Guard",
      "Ga Bu",
      "Beggarly Fellow",
      "Distressed Ancient One",
      "Gallant Guardsman",
      "Furious Man",
      "Artoirel",
      "Rammbroes",
      "Wauter",
      "Guthjon",
      "Emmanellain",
      "Koko",
      "Panicked Son",
      "Lionnellais",
      "Haldrath",
      "Gundobald",
      "Eudestand",
      "Rhitskylt",
      "Isse",
      "Aymeric",
      "Symme",
      "House Durendaire Knight",
      "Bewildered Man",
      "Skyfryn",
      "Yuyutazi",
      "Nenebaru",
      "Drillemont",
      "Hopeful Citizen",
      "Tristechambel",
      "Faramund",
      "Hourlinet",
      "Flame Herald",
      "Manager of Suites",
      "Glagg",
      "Landebert",
      "Immigration Officer",
      "Simeonard of the Holiest Flame",
      "Airship Attendant",
      "Dying Guard",
      "Parsemontret",
      "Beltardois",
      "Ihanami",
      "Aergmhus",
      "Desperate Refugee",
      "Hardened Man",
      "Marcelain",
      "Sevrin",
      "Brunadier",
      "Arenvald",
      "Eyrimhus",
      "Storm Officer (The Waking Sands)",
      "Storm Officer (Floating City of Nym)",
      "Storm Officer (MSQ)",
      "Theodore",
      "Alliance Herald",
      "Resistance Herald",
      "Eginolf",
      "Karaku",
      "Motojiro",
      "Robed Giant",
      "Thancred",
      "Wayward Warrior",
      "Wheiskaet",
      "Loupard",
      "Haustefort",
      "Glynard",
      "Seseroga",
      "Eylgar",
      "Wrenden",
      "Hancock",
      "Adelstan",
      "Kaidate",
      "Crystarium Gatekeep",
      "Gaius",
      "Maxima",
      "Tescelingeon",
      "Vortefaurt",
      "Vaincannet",
      "Keeled-over Knight",
      "Meffrid",
      "Cravellin",
      "Grithil",
      "Trachtoum",
      "Magus of Darkness",
      "Flavien de Fortemps",
      "Josseloux",
      "Baderon",
      "Talebot",
      "Charibert",
      "Hrotmar",
      "House Fortemps Knight",
      "Myrcant",
      "Pierremons",
      "Wymond",
      "Expedition Leader",
      "Kokosamu",
      "Paiyo Reiyo",
      "Hiun",
      "Midlander Engineer",
      "Nunuzofu",
      "Gagaruna",
      "Stone Torch",
      "Anguished Guard",
      "Immortal Flames Pilot",
      "Lewin",
      "Redwald",
      "Grinnaux",
      "Chadden",
      "Ivaurault",
      "Bitter Knight",
      "Carvallain",
      "Leofric",
      "Resolute Citizen",
      "Convalescent Guard",
      "Alestan",
      "Hyuran Coachman",
      "Wyrkrhit",
      "Hoary Boulder",
      "Unnerved Fisher",
      "Baensyng",
      "Saint Coinach Ferryman",
      "Free Citizen",
      "Ossine",
      "Owyne",
      "Nawashiro",
      "Irvithe",
      "Bragi",
      "Godbert",
      "Eulmoran Adjutant",
      "Gibrillont",
      "Brawny Knight",
      "Ignemortel",
      "Firkmann",
      "Sundhimal",
      "Biggs",
      "Ardent Attendant",
      "Storm Personnel Officer",
      "Temple Herald",
      "Drest",
      "Composed Fisher",
      "Astidien",
      "Runar",
      "Byrglaent",
      "Staelwyrn",
      "Wystan",
      "Junghbhar",
      "Lue-Reeq",
      "Flame Officer (The Waking Sands)",
      "Sentry",
      "Proud Patriot",
      "Raubahn",
      "Granson",
      "Ahtbyrm",
      "Beves",
      "Wercrata",
      "Riol",
      "Thoarich",
      "Grehfarr",
      "Swaenhylt",
      "Ludovoix",
      "Asahi",
      "Wald
```

### 角色列表（共1171个）

- "STATUS" :3972,
- "Alphinaud" :2526,
- "CHOICE" :2248,
- "ACTION" :2110,
- "Alisaie" :1249,
- "LOCATION" :1177,
- "Y'shtola" :977,
- "SYSTEM" :956,
- "Thancred" :893,
- "Lyse" :740,
- "Urianger" :612,
- "G'raha Tia" :552,
- "The Adventurer" :536,
- "Ryne" :461,
- "Tataru" :411,
- "Estinien" :315,
- "Yugiri" :308,
- "Hien" :266,
- "Raubahn" :261,
- "Aymeric" :260,
- "Minfilia Warde" :243,
- "Cid" :210,
- "Krile" :190,
- "Lucia" :181,
- "Chai-Nuzz" :181,
- "Gosetsu" :167,
- "Ysayle" :129,
- "Papalymo" :125,
- "Pipin" :120,
- "Beq Lugg" :112,
- "Lyna" :111,
- "Almet" :110,
- "Emmanellain" :110,
- "Kan-E-Senna" :109,
- "Elidibus" :106,
- "Arenvald" :105,
- "Haurchefant" :103,
- "Dulia-Chai" :103,
- "M'naago" :101,
- "Runar" :97,
- "Emet-Selch" :96,
- "Cirina" :95,
- "Artoirel" :88,
- "Merlwyb" :87,
- "Ardbert" :80,
- "Ran'jit" :79,
- "Count Edmont de Fortemps" :75,
- "Jeryk" :74,
- "Ilberd" :73,
- "Wedge" :73,
- ... 共1171个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXIV/,False,Final Fantasy XIV,Final Fantasy,TOTAL,20364,689360,107994,860743,1.633112579581697,94.72337810106163,6.935772454487245,1166
../data/FinalFantasy/FFXIV/,False,Final Fantasy XIV,Final Fantasy,playerChoice,536,3582,1351,4204,-0.7069430589083261,104.85340784232045,6.126369170757149,1
../data/FinalFantasy/FFXIV/,False,Final Fantasy XIV,Final Fantasy,male,12367,446516,68399,558313,1.7104014895948794,94.42714081856276,7.0067178031337445,771
../data/FinalFantasy/FFXIV/,False,Final Fantasy XIV,Final Fantasy,female,6893,224083,35402,279001,1.5705017719136727,95.07671507954223,6.803084705968773,277
../data/FinalFantasy/FFXIV/,False,Final Fantasy XIV,Final Fantasy,genderless,296,8516,1380,10445,1.2895702411828367,96.80826857543516,6.647797208460119,17
../data/FinalFantasy/FFXIV/,False,Final Fantasy XIV,Final Fantasy,neutral,272,6663,1461,8780,1.737776263597958,90.72650269455184,7.635431517303716,100

```


### 数据来源脚本 (scraper.py)

```python
# The https://ffxiv.gamerescape.com wiki has quest logs 
#  for Main Scenario Quests listed on a category page.
#  Load the category pages, then download each link within it.

from urllib.request import *
import time
from os import path
import re

from bs4 import BeautifulSoup

def loadPage(page):
	req = Request(
		page, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)

	html = urlopen(req).read().decode('utf-8')
	return(html)


# test: https://ffxiv.gamerescape.com/wiki/A_Final_Temptation#Dialogue

base = "https://ffxiv.gamerescape.com"
# downloaded view-source:https://ffxiv.gamerescape.com/wiki/Category:Main_Scenario_Quest

indexPages = [
	"https://ffxiv.gamerescape.com/wiki/Category:Main_Scenario_Quest",
	"https://ffxiv.gamerescape.com/w/index.php?title=Category:Main_Scenario_Quests&pagefrom=Devourer+of+Worlds#mw-pages",
	"https://ffxiv.gamerescape.com/w/index.php?title=Category:Main_Scenario_Quests&pagefrom=Migrant+Marauders#mw-pages",
	"https://ffxiv.gamerescape.com/w/index.php?title=Category:Main_Scenario_Quests&pagefrom=The+Key+to+Victory#mw-pages"]


# Save all category pages to single index file
if not path.exists("raw/indexPage.txt"):
	print("Downloading index pages ...")
	iText= ""
	for iPage in indexPages:
		iText += loadPage(iPage)
		time.sleep(2)
	o = open("raw/indexPage.txt",'w')
	o.write(iText)
	o.close()

# Open index page
o = open("raw/indexPage.txt")
categoryPage = o.read()
o.close()

catSoup = BeautifulSoup(categoryPage, "html.parser")
catSoup = catSoup.find_all("div",{"id":"mw-pages"})
catSoup = "\n".join([str(x) for x in catSoup])

pages = re.findall('href="(/wiki/.+?)"',catSoup)
pages = list(set(pages))

for page in pages:
	print(page)
	fileName = "raw/page_"+page.replace("/","#")+".html"
	if not path.exists(fileName):
		html = loadPage(base+page)
		time.sleep(3)
		dialogue = ""
		if html.count('class="bubble"')>0:
			sou
```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
