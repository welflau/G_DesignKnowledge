# 猴岛小英雄 · TheCurseOfMonkeyIsland（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：猴岛小英雄, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
猴岛小英雄系列《TheCurseOfMonkeyIsland》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：猴岛小英雄（MonkeyIsland）
- **游戏**：TheCurseOfMonkeyIsland
- **品类**：冒险游戏
- **说明**：LucasArts经典点击冒险

### 元数据 (meta.json)

```json
{
  "game": "The Curse of Monkey Island",
  "series": "Monkey Island",
  "year": 1997,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/pc/29083-the-curse-of-monkey-island/faqs/60819",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "notes": "The CHOICE components here are only for alternative dialogue options (the player only has one chance to make a choice). Parallel options (e.g. list of questions that can all be asked in any order) are not represented",
  "parserParameters": {
    "parser": "MonkeyIsland3Parser",
    "fileType": ".html",
    "textDivId": "faqtext",
    "startText": "Monkey grunts are heard",
    "endText": "*3.2f. End Credits"
  },
  "mainPlayerCharacters": [
    "Guybrush"
  ],
  "characterGroups": {
    "male": [
      "Assistant",
      "Bartender",
      "Bill",
      "Blondebeard",
      "Boyle",
      "Charles",
      "Cruff",
      "Dinghy Dog™",
      "Fat Pirate",
      "Father Pirate",
      "Fossey",
      "Gravedigger",
      "Griswold",
      "Guybrush",
      "Haggis",
      "Hideous Pirate",
      "Kenny",
      "LaFoot",
      "LeChuck",
      "Lemonhead",
      "Lost Welshman",
      "Mort",
      "Murray",
      "Palido",
      "Rottingham",
      "Skully",
      "Slappy",
      "Smuggler King",
      "Snowcone Guy",
      "Soldier",
      "Son Pirate",
      "Stan",
      "Thin Pirate",
      "Cabaña Boy",
      "Van Helgen",
      "Walk-Thru Speaker",
      "Wally",
      "Wharf Rat™",
      "Pirate #1"
    ],
    "female": [
      "Elaine",
      "Minnie",
      "Xima",
      "Voodoo Lady"
    ],
    "neutral": [
      "Skeleton Pirate #1",
      "Skeleton Pirate #2",
      "Skeleton Pirate #3",
      "Skeleton Pirate #4"
    ]
  },
  "aliases": {
    "Chorus": [
      "Bill",
      "Haggis",
      "Van Helgen"
    ],
    "Voice": "Mort",
    "Skull": "Murray",
    "Lechuck": "LeChuck",
    "Fortuneteller": "Xima",
    "Ghost Bride": "Minnie",
    "Operator": "LaFoot",
    "Proprietor": "Blondebeard",
    "Small Pirate": "Kenny",
    "Sunbather": "Palido",
    "Actor": "Slappy"
  }
}
```

### 角色列表（共49个）

- "Guybrush" :1423,
- "ACTION" :956,
- "LeChuck" :119,
- "Haggis" :95,
- "Murray" :84,
- "Van Helgen" :79,
- "Bill" :67,
- "Voodoo Lady" :63,
- "Griswold" :62,
- "Blondebeard" :55,
- "Rottingham" :54,
- "Wally" :52,
- "Lemonhead" :46,
- "Slappy" :40,
- "Stan" :37,
- "Mort" :34,
- "Xima" :30,
- "Wharf Rat™" :29,
- "Fossey" :29,
- "Kenny" :29,
- "Palido" :29,
- "Dinghy Dog™" :28,
- "Pirate #1" :28,
- "LaFoot" :26,
- "Minnie" :26,
- "CHOICE" :23,
- "Elaine" :21,
- "Lost Welshman" :19,
- "Cabaña Boy" :18,
- "Bartender" :15,
- "Cruff" :14,
- "Smuggler King" :9,
- "Charles" :9,
- "Thin Pirate" :6,
- "Gravedigger" :6,
- "Fat Pirate" :4,
- "Walk-Thru Speaker" :4,
- "Boyle" :4,
- "Snowcone Guy" :3,
- "Skully" :3,
- "Hideous Pirate" :2,
- "Skeleton Pirate #4" :2,
- "Skeleton Pirate #3" :2,
- "Father Pirate" :1,
- "Son Pirate" :1,
- "Assistant" :1,
- "Skeleton Pirate #2" :1,
- "Skeleton Pirate #1" :1,
- "Soldier" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MonkeyIsland/TheCurseOfMonkeyIsland/,False,The Curse of Monkey Island,Monkey Island,TOTAL,2711,30577,8834,36917,0.006577122714185535,101.18037474862119,6.876119410482747,47
../data/MonkeyIsland/TheCurseOfMonkeyIsland/,False,The Curse of Monkey Island,Monkey Island,male,2565,28499,8295,34346,-0.02913507919791769,101.39081367959764,6.884682838007429,39
../data/MonkeyIsland/TheCurseOfMonkeyIsland/,False,The Curse of Monkey Island,Monkey Island,female,140,2036,530,2526,0.5480708010527504,97.97535711902734,6.750825704859694,4
../data/MonkeyIsland/TheCurseOfMonkeyIsland/,False,The Curse of Monkey Island,Monkey Island,neutral,6,42,9,45,-1.1271428571428554,111.45547619047619,7.251538095238095,4

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

pages = ["https://gamefaqs.gamespot.com/pc/29083-the-curse-of-monkey-island/faqs/60819"]

pageNum = 0
for page in pages:
	pageNum += 1
	fileName = "raw/page_"+str(pageNum).zfill(3)+".html"
	req = Request(
		page, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)


	html = urlopen(req).read().decode('utf-8')#.encode('utf-8')#.decode('ISO-8859-1')
	o = open(fileName,'w')
	o.write(html)
	o.close()
	time.sleep(3)
	#with codecs.open(fileName, "w", "utf-8") as targetFile:
	#	targetFile.write(html)

```


## 策划参考价值
冒险游戏类型的对话叙事参考。LucasArts经典点击冒险
