# 猴岛小英雄 · MonkeyIsland2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：猴岛小英雄, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
猴岛小英雄系列《MonkeyIsland2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：猴岛小英雄（MonkeyIsland）
- **游戏**：MonkeyIsland2
- **品类**：冒险游戏
- **说明**：LucasArts经典点击冒险

### 元数据 (meta.json)

```json
{
  "game": "Monkey Island 2: LeChuck's Revenge",
  "series": "Monkey Island",
  "year": 1991,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/pc/562680-monkey-island-2-lechucks-revenge/faqs/79490",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "Not included"
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
  "notes": "See Readme",
  "parserParameters": {
    "parser": "MonkeyIsland2Parser",
    "fileType": ".html",
    "textDivId": "faqtext",
    "startText": "LOCATION:",
    "endText": ""
  },
  "mainPlayerCharacters": [
    "Guybrush"
  ],
  "characterGroups": {
    "male": [
      "Barkeep",
      "Bart",
      "Bernard",
      "Captain Dread",
      "Chef",
      "Costume shopkeeper",
      "Dad",
      "Delivery man",
      "Dog",
      "Door guard",
      "Filbert",
      "Fink",
      "Fisherman",
      "Governor Phatt",
      "Guard",
      "Guybrush",
      "Herman",
      "Innkeeper",
      "Largo",
      "LeChuck",
      "Man watching spit contest",
      "Marty",
      "Ralphie",
      "Rapp",
      "Retired pirate",
      "Rich",
      "Shopkeeper",
      "Sleeping pirate1",
      "3rd sleeping pirate",
      "Spitmaster",
      "Stan",
      "Wally",
      "Wheel operator",
      "Woodsmith"
    ],
    "female": [
      "Captain Kate Capsize",
      "Costumed woman",
      "Elaine",
      "Librarian",
      "Mom",
      "Voodoo Lady",
      "Woman 1 watching spit contest",
      "Woman 2 watching spit contest"
    ],
    "neutral": [
      "Clown costume",
      "Moose costume",
      "NARRATOR",
      "Parrot",
      "Pig costume",
      "Voodoo Priest"
    ]
  },
  "aliases": {
    "Mom and Dad": [
      "Mom",
      "Dad"
    ]
  }
}
```

### 角色列表（共50个）

- "Guybrush" :341,
- "LOCATION" :88,
- "ACTION" :65,
- "LeChuck" :63,
- "Barkeep" :46,
- "Largo" :46,
- "Voodoo Lady" :37,
- "Wally" :27,
- "Captain Kate Capsize" :26,
- "Captain Dread" :24,
- "Elaine" :21,
- "Fink" :16,
- "Shopkeeper" :15,
- "Wheel operator" :15,
- "Bart" :14,
- "Fisherman" :13,
- "Librarian" :13,
- "Guard" :13,
- "Rapp" :11,
- "Dad" :11,
- "Door guard" :11,
- "Governor Phatt" :11,
- "Mom" :9,
- "Herman" :7,
- "Parrot" :7,
- "Retired pirate" :7,
- "Filbert" :7,
- "Spitmaster" :7,
- "Ralphie" :7,
- "Costumed woman" :6,
- "NARRATOR" :6,
- "Marty" :5,
- "Rich" :4,
- "Delivery man" :4,
- "Stan" :4,
- "Chef" :3,
- "Sleeping pirate1" :3,
- "Man watching spit contest" :2,
- "Bernard" :2,
- "Woman 2 watching spit contest" :1,
- "Woman 1 watching spit contest" :1,
- "3rd sleeping pirate" :1,
- "Woodsmith" :1,
- "Pig costume" :1,
- "Clown costume" :1,
- "Dog" :1,
- "Moose costume" :1,
- "Costume shopkeeper" :1,
- "Voodoo Priest" :1,
- "Innkeeper" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MonkeyIsland/MonkeyIsland2/,False,Monkey Island 2: LeChuck's Revenge,Monkey Island,TOTAL,872,9285,2696,10835,-0.47699963766899955,104.6165703603256,6.28168383244728,48
../data/MonkeyIsland/MonkeyIsland2/,False,Monkey Island 2: LeChuck's Revenge,Monkey Island,male,743,7454,2217,8670,-0.5537616660488354,105.02123889792746,6.313481169582702,34
../data/MonkeyIsland/MonkeyIsland2/,False,Monkey Island 2: LeChuck's Revenge,Monkey Island,female,112,1509,418,1803,-0.08307537549820587,102.08809765807072,6.033901646896927,8
../data/MonkeyIsland/MonkeyIsland2/,False,Monkey Island 2: LeChuck's Revenge,Monkey Island,neutral,17,322,60,362,-0.23116149068322933,106.27851656314701,6.746848157349897,6

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

pages = ["https://gamefaqs.gamespot.com/pc/562680-monkey-island-2-lechucks-revenge/faqs/79490"]

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
