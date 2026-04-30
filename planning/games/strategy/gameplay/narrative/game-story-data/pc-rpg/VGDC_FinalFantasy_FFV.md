# 最终幻想 · FFV（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFV》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFV
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy V",
  "series": "Final Fantasy",
  "year": 1992,
  "status": "ready",
  "source": "http://www.finalfantasyquotes.com/ff5/script",
  "notes": "See README",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "NA"
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
  "parserParameters": {
    "parser": "FFQParser",
    "fileType": ".html",
    "characterClassIdentifier": "ff7",
    "replaceFixes": [
      [
        "Lix, Tycoon and the Ancient Library.",
        "Across The World Slowly Begins To Recede As Well, From: Lix, Tycoon and the Ancient Library.",
        "The Spirits Of Heroes That Rest In The Pieces Of The Crystal"
      ],
      [
        "Berserker, Red Mage, Summoner, Mystic Knight, Time Mage. As the last piece is gained the room begins to shake!",
        "The spirits of heroes that rest in the Pieces of the Crystal: Berserker, Red Mage, Summoner, Mystic Knight, Time Mage. As the last piece is gained the room begins to shake!"
      ]
    ]
  },
  "mainPlayerCharacters": [
    "Butz",
    "Lenna",
    "Galuf",
    "Faris",
    "Cara"
  ],
  "characterGroups": {
    "male": [
      "Apanda",
      "Apocalypse",
      "Atmos",
      "Butz",
      "Cid",
      "Dorgan",
      "Enkidou",
      "Exdeath",
      "Galuf",
      "Gilgamesh",
      "Gogo",
      "Guido",
      "Halikarnassos",
      "Kelgar",
      "King Tycoon",
      "King Worus",
      "Mid",
      "Necrofobia",
      "Neo-exdeath",
      "Zeza",
      "Zokk",
      "Butz's Dad",
      "Bahamut",
      "Boco",
      "Byblos",
      "Carbuncle",
      "Ifrit",
      "Odin",
      "King",
      "Old Man",
      "Chancellor",
      "Guard",
      "Guard 2",
      "Guards",
      "Man",
      "Man 2",
      "Minister",
      "Pirate",
      "Pirates",
      "Scholar",
      "Scholar 2",
      "Scholar 3",
      "Scholar 4",
      "Soldier",
      "Soldiers",
      "Warrior",
      "Wolf"
    ],
    "female": [
      "Calofisteri",
      "Cara",
      "Faris",
      "Jenica",
      "Lenna",
      "Magisa",
      "Queen Karnak",
      "Siren",
      "Stella",
      "Butz's Mom",
      "Lady",
      "Maid",
      "Woman"
    ],
    "neutral": [
      "Chocobo",
      "Leviathan",
      "Moogle",
      "Twin Tania",
      "Book",
      "Book From 1000 Years Ago",
      "Book From A Wizard",
      "Bookshelf",
      "Left Tower",
      "Right Tower",
      "Monster",
      "Monster 2",
      "Monster 3",
      "Monsters",
      "People",
      "Werewolves"
    ]
  },
  "aliases": {
    "Across The World Slowly Begins To Recede As Well, From": "ACTION",
    "The Spirits Of Heroes That Rest In The Pieces Of The Crystal": "ACTION",
    "Tablet": "ACTION",
    "Four Warriors Of Dawn": [
      "Dorgan",
      "Galuf",
      "Zeza",
      "Kelgar"
    ],
    "Cara [to Mid]": "Cara",
    "Girl [cara]": "Cara",
    "Galuf [in Communicator On The Top Of The Tower]": "Galuf",
    "King [of Tycoon]": "King Tycoon",
    "Lenna [sleep Talking]": "Lenna",
    "Lenna [to Faris]": "Lenna",
    "Mid [entering Room]": "Mid",
    "Zeza [through Communicator]": "Zeza",
    "*ugh* *unnh* Voice": "Galuf",
    "Solider": "Soldier",
    "Turtle": "Guido",
    "Voice": {
      "King Tycoon": [
        "Le... Lenna"
      ],
      "Faris": [
        ""
      ]
    },
    "Carbunkle": "Carbuncle"
  }
}
```

### 角色列表（共77个）

- "ACTION" :571,
- "Butz" :389,
- "Galuf" :232,
- "Lenna" :216,
- "Faris" :175,
- "Cara" :128,
- "Cid" :93,
- "Mid" :63,
- "Exdeath" :51,
- "Zeza" :33,
- "Guido" :31,
- "Kelgar" :29,
- "Gilgamesh" :26,
- "King Tycoon" :21,
- "Soldier" :20,
- "Moogle" :15,
- "Pirates" :9,
- "Dorgan" :8,
- "Boco" :8,
- "Wolf" :7,
- "Minister" :7,
- "Guard" :7,
- "Man" :7,
- "Monster" :6,
- "Zokk" :6,
- "Book" :5,
- "Chancellor" :5,
- "Warrior" :5,
- "Necrofobia" :4,
- "King Worus" :4,
- "Magisa" :4,
- "King" :4,
- "Werewolves" :3,
- "Scholar" :3,
- "Queen Karnak" :3,
- "Siren" :3,
- "Halikarnassos" :2,
- "Jenica" :2,
- "Left Tower" :2,
- "Right Tower" :2,
- "Bahamut" :2,
- "Chocobo" :2,
- "Ifrit" :2,
- "Lady" :2,
- "Pirate" :2,
- "Old Man" :2,
- "Neo-exdeath" :1,
- "Twin Tania" :1,
- "Woman" :1,
- "Apocalypse" :1,
- ... 共77个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFV/,False,Final Fantasy V,Final Fantasy,TOTAL,1681,12408,3563,14432,-0.5070184500669814,104.90030451866407,6.545247032425278,76
../data/FinalFantasy/FFV/,False,Final Fantasy V,Final Fantasy,male,1099,8693,2385,10156,-0.3826064461610468,104.29759376215618,6.511012377866864,47
../data/FinalFantasy/FFV/,False,Final Fantasy V,Final Fantasy,female,538,3209,1084,3695,-0.8483716950366773,106.41767332335604,6.6126406680243175,13
../data/FinalFantasy/FFV/,False,Final Fantasy V,Final Fantasy,neutral,44,506,93,581,0.0809473415784776,104.17300119002083,6.777275757575757,16

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re

base = "http://www.finalfantasyquotes.com"
indexPage = "http://www.finalfantasyquotes.com/ff5/script/Part_1"
index = urlopen(indexPage).read().decode('utf-8')
pages = re.findall("href=['\"](/ff[0-9]+/script/[^'\"]+)['\"]",index)


pageNum = 0
for page in pages:
	print(page)
	pageNum += 1
	fileName = "raw/page_"+str(pageNum).zfill(3)+".html"
	if not path.exists(fileName):
		html = urlopen(base+page).read().decode('utf-8')
		o = open(fileName,'w')
		o.write(html)
		o.close()
		time.sleep(2)


```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
