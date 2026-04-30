# 最终幻想 · FFXV（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXV》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXV
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy XV",
  "series": "Final Fantasy",
  "year": 2016,
  "status": "ready",
  "source": "https://thelifestream.net/final-fantasy-xv-lore/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development/",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "2",
    "truePositive_notes": "Previous errors fixed. Some optional/incidental dialogue missing from source file.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "No errors noted."
  },
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "TheLifestreamParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Noctis",
    "Ignis",
    "Gladiolus",
    "Prompto"
  ],
  "characterGroups": {
    "male": [
      "Ardyn",
      "Biggs",
      "Caligo",
      "Cid",
      "Cor",
      "Dave",
      "Dino",
      "Drautos",
      "Dustin",
      "Gladiolus",
      "Iedolas",
      "Ignis",
      "Jared",
      "Loqi",
      "Navyth",
      "Noctis",
      "Prompto",
      "Randolph",
      "Ravus",
      "Regis",
      "Takka",
      "Talcott",
      "Tony",
      "Verstael",
      "Vyv",
      "Wedge",
      "Weskham",
      "Wiz",
      "Bahamut",
      "Gilgamesh",
      "Man",
      "Melusine Hunter",
      "Old Man",
      "Boy",
      "Altissian Guard",
      "Proprietor (Wishing Birds)",
      "Proprietor (Delivery)",
      "Gatekeeper",
      "Boyfriend",
      "Receptionist",
      "Server",
      "Estate Guard",
      "Vendor",
      "Staff",
      "Assassin",
      "Hunter1",
      "Hunter2"
    ],
    "female": [
      "Aranea",
      "Camelia",
      "Coctura",
      "Cindy",
      "Ezma",
      "Holly",
      "Iris",
      "Kimya",
      "Luna",
      "Maria",
      "Monica",
      "Sania",
      "Gentiana",
      "Shiva",
      "Leviathan",
      "Melusine",
      "Woman",
      "Announcement",
      "Old Woman",
      "Girl",
      "Newscaster",
      "Girlfriend",
      "Radio Narrator",
      "Radio Interviewer"
    ],
    "neutral": [
      "Naga",
      "Soul",
      "NARRATIVE",
      "SYSTEM",
      "Broadcast",
      "Attendant"
    ]
  },
  "aliases": {
    "Gladio": "Gladiolus",
    "Gladiols": "Gladiolus",
    "Lunafreya": "Luna",
    "Noct Gar": "Noctis",
    "Noct": "Noctis",
    "Prompmto": "Prompto",
    "Giglamesh": "Gilgamesh",
    "Suspicious Stranger": "Ardyn",
    "Suspcious Stranger": "Ardyn",
    "Research log": "Verstael",
    "Gatekeepr": "Gatekeeper",
    "Hunter": {
      "Hunter1": [
        "I just don't know what to make of it.",
        "Not just that—what if you slip up?"
      ],
      "Hunter2": [
        "Not worth the risk."
      ],
      "Gladiolus": [
        "So, you my backup?",
        "Anyway, place is crawling with daemons.",
        "Save the talk. We got hunting to do. Now, if we're done with the introductions, follow me.",
        "There they are. You ready to rumble?",
        "Some pretty fancy moves you've got there. Reminds me of a certain king I know.",
        "You think so?",
        "I ain't one to leave unfinished business. Can't speak for him, though.",
        "Well, how 'bout you prove it?",
        "Think so.",
        "When have I ever?",
        "Will do. Now, let's scram."
      ],
      "Melusine Hunter": [
        "Hey there, \"brother.\"",
        "Don't act so surprised. I know a fellow Hunter when I see one.",
        "And, as my \"brother\"... I was hoping you might take care of a little problem for me—a problem named \"Melusine.\"",
        "A real pretty lady who appears at the Vesperpool",
        "Attaboy. Good luck!",
        "Damn, that was quick. I knew I could count on you, \"brother.\"",
        "... Sadly, it does.",
        "Because I'm the one who wrote it.",
        "Ex-partner. We had it out a couple of times, and one night she just up and left.",
        "Now I know why she never wrote back.",
        "Well, what's done is done—and thanks to you, her killer has been brought to justice."
      ]
    },
    "???": {
      "Talcott": [
        "Uh..."
      ],
      "Iedolas": [
        "The ring...",
        "Thieves cannot escape the hand of justice."
      ]
    },
    "Proprietor": {
      "Proprietor (Wishing Birds)": [
        "They're launching wishing birds. Would you boys like to give it a try?",
        "They're an old Altissian tradition."
      ],
      "Proprietor (Delivery)": [
        "Y'all came all the way out here to deliver the goods?"
      ]
    },
    "SYSTEM": {
      "Cor": [
        "\"Do you dare risk all"
      ],
      "Sania": [
        "\"Ooh, this specimen is ",
        "\"Back so soon?",
        "\"There you are"
      ],
      "Luna": [
        "If you know of any who are bed
```

### 角色列表（共78个）

- "NARRATIVE" :2584,
- "Noctis" :1939,
- "Prompto" :1527,
- "CHOICE" :1340,
- "Gladiolus" :1218,
- "SYSTEM" :1092,
- "Ignis" :1050,
- "Ardyn" :206,
- "Man" :148,
- "Cindy" :141,
- "Aranea" :139,
- "Iris" :115,
- "Cor" :106,
- "Vyv" :83,
- "Woman" :76,
- "Dino" :63,
- "Luna" :62,
- "Cid" :61,
- "Camelia" :59,
- "Talcott" :59,
- "Takka" :58,
- "Sania" :51,
- "Holly" :48,
- "Dave" :44,
- "Navyth" :36,
- "Wiz" :34,
- "Ravus" :28,
- "Loqi" :26,
- "Shiva" :25,
- "Gentiana" :25,
- "Soul" :23,
- "Announcement" :22,
- "Verstael" :22,
- "Gilgamesh" :19,
- "Randolph" :19,
- "Biggs" :19,
- "Monica" :19,
- "Weskham" :18,
- "Coctura" :16,
- "Ezma" :13,
- "Regis" :13,
- "Kimya" :12,
- "Jared" :12,
- "Melusine Hunter" :11,
- "Old Woman" :11,
- "Old Man" :11,
- "Newscaster" :11,
- "Maria" :9,
- "Wedge" :9,
- "Caligo" :9,
- ... 共78个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXV/,False,Final Fantasy XV,Final Fantasy,TOTAL,7805,74792,19124,87926,-0.1925872541300837,103.40908561794491,6.462921275236467,75
../data/FinalFantasy/FFXV/,False,Final Fantasy XV,Final Fantasy,male,6898,59815,16289,69863,-0.37565858790862094,104.29630954898506,6.410134274293885,47
../data/FinalFantasy/FFXV/,False,Final Fantasy XV,Final Fantasy,female,876,14524,2733,17504,0.7036756996482012,99.48295068646487,6.698455072548328,24
../data/FinalFantasy/FFXV/,False,Final Fantasy XV,Final Fantasy,neutral,3707,46625,4628,61181,3.8229507816971413,85.59780527121313,7.958986126225493,6

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import time


# test: https://ffxiv.gamerescape.com/wiki/A_Final_Temptation#Dialogue

def getPage(url):
	req = Request(
		page, 
		headers={
			'User-Agent': 'XYZ/3.0'
		}
	)

	html = urlopen(req, timeout=10).read().decode('utf-8')
	return(html)

pages = ["https://thelifestream.net/final-fantasy-xv-lore/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development-part-1/","https://thelifestream.net/final-fantasy-xv-lore/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development-part-2/","https://thelifestream.net/final-fantasy-xv-lore/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development-part-3/","https://thelifestream.net/final-fantasy-xv-lore/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development/final-fantasy-xv-chapter-by-chapter-lore-exposition-and-development-part-4/"]
pageNum = 0
print("  downloading pages ...")
for page in pages:
	pageNum += 1
	print(page)
	#html = urlopen(page).read().decode('utf-8')
	html = getPage(page)
	fileName = "raw/page_"+str(pageNum).zfill(3)+".html"
	o = open(fileName,'w')
	o.write(html)
	o.close()
	time.sleep(2)

```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
