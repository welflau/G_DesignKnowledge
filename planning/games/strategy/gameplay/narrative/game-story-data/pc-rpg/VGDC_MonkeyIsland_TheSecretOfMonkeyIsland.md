# 猴岛小英雄 · TheSecretOfMonkeyIsland（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：猴岛小英雄, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
猴岛小英雄系列《TheSecretOfMonkeyIsland》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：猴岛小英雄（MonkeyIsland）
- **游戏**：TheSecretOfMonkeyIsland
- **品类**：冒险游戏
- **说明**：LucasArts经典点击冒险

### 元数据 (meta.json)

```json
{
  "game": "The Secret of Monkey Island",
  "series": "Monkey Island",
  "year": 1990,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/pc/562681-the-secret-of-monkey-island/faqs/23891",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "Not included"
  },
  "notes": "Author states: Due to the overwhelming amount of choices and story paths, I can only put ONE kind of flow that makes the whole story.",
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "2",
    "truePositive_notes": "No choices in source; only one path followed so missing dialogue",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "Stage direction appearing as dialogue - issue #112 raised (and fixed)."
  },
  "parserParameters": {
    "parser": "MonkeyIslandParser",
    "fileType": ".html",
    "textDivId": "faqtext",
    "startText": "Epilogue",
    "endText": "Credits roll"
  },
  "mainPlayerCharacters": [
    "Guybrush"
  ],
  "characterGroups": {
    "male": [
      "Alfredo",
      "Barrel Pirate",
      "Bill",
      "Black Pirate",
      "Blue Pirate",
      "Bob",
      "Citizen",
      "Cook",
      "Estevan",
      "Fat Pirate",
      "Ghost",
      "Green Pirate",
      "Guy",
      "Guy 1",
      "Guybrush",
      "Herman",
      "LeChuck",
      "Loom Pirate",
      "Man",
      "Man 1",
      "Man 2",
      "Mancomb",
      "Meathook",
      "Nick",
      "Old Man",
      "Otis",
      "Pirate",
      "Priest",
      "Sheriff",
      "Smirk",
      "Stan",
      "Storekeeper",
      "Tall Pirate",
      "Troll",
      "Red Headhunter",
      "Lemon Headhunter",
      "Squid Headhunter"
    ],
    "female": [
      "Carla",
      "Elaine",
      "Lady"
    ],
    "neutral": [
      "Bone",
      "Dog",
      "Someone",
      "Tattoo",
      "Monkey",
      "Parrot",
      "Head"
    ]
  },
  "aliases": {
    "Governor": "Elaine",
    "Strkeeper": "Storekeeper",
    "Squid H.": "Squid Headhunter",
    "Lemon H.": "Lemon Headhunter",
    "Red H.": "Red Headhunter",
    "Tall P": "Tall Pirate",
    "Tall P.": "Tall Pirate",
    "Barrel P.": "Barrel Pirate",
    "Black P.": "Black Pirate",
    "Blue P.": "Blue Pirate",
    "Fat P.": "Fat Pirate",
    "Green P.": "Green Pirate",
    "Old man": "Old Man",
    "Door": "ACTION",
    "Person": "Sheriff",
    "Whisper": "Sheriff",
    "All": [
      "Blue Pirate",
      "Black Pirate",
      "Green Pirate"
    ],
    "All P.": [
      "Barrel Pirate",
      "Tall Pirate"
    ],
    "Pirate": {
      "Mancomb": [
        "Ahoy there, stranger. New in town?",
        "Guybrush Threepwood? Ha ha ha!!! That's the stupidest name I've ever heard!",
        "But it's not even a name!",
        "My name is Mancomb Seepgood."
      ],
      "Meathook": [
        "Hey! I don't like visitors!",
        "My name's Meathook"
      ],
      "Loom Pirate": [
        "Aye!",
        "Aye.",
        "So, tell me about LOOM.",
        "(Face brightens)",
        "Sorry, but on some topics I just get carried away."
      ]
    },
    "Man": {
      "Stan": [
        "Howdy! I'm Stan of Stan's Previously"
      ],
      "Otis": [
        "You gotta get me out of here!",
        "Hey, it's hard to keep my breath",
        "Ooooh! Grog-o-Mint! How refreshing!",
        "My name is Otis."
      ],
      "Herman": [
        "Hi! I'm Herman Toothrot!"
      ]
    }
  }
}
```

### 角色列表（共48个）

- "Guybrush" :458,
- "ACTION" :252,
- "Stan" :60,
- "Red Headhunter" :53,
- "Herman" :39,
- "Meathook" :33,
- "Elaine" :33,
- "Blue Pirate" :30,
- "Storekeeper" :28,
- "Carla" :27,
- "Man 1" :27,
- "Otis" :27,
- "Sheriff" :27,
- "Man 2" :26,
- "LeChuck" :25,
- "Green Pirate" :24,
- "Squid Headhunter" :23,
- "Alfredo" :23,
- "Smirk" :22,
- "Bill" :22,
- "Tall Pirate" :21,
- "Bone" :21,
- "Lady" :19,
- "Black Pirate" :17,
- "Troll" :15,
- "Barrel Pirate" :14,
- "Head" :10,
- "Old Man" :10,
- "Ghost" :8,
- "Estevan" :8,
- "Mancomb" :8,
- "Cook" :7,
- "Loom Pirate" :7,
- "Man" :6,
- "Citizen" :6,
- "Nick" :5,
- "Guy 1" :5,
- "Pirate" :5,
- "Lemon Headhunter" :4,
- "Fat Pirate" :4,
- "Priest" :3,
- "Guy" :3,
- "Dog" :3,
- "Bob" :1,
- "Monkey" :1,
- "Parrot" :1,
- "Tattoo" :1,
- "Someone" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MonkeyIsland/TheSecretOfMonkeyIsland/,False,The Secret of Monkey Island,Monkey Island,TOTAL,1221,14619,4169,17362,-0.2083635511743207,102.80209245711794,6.338944175207707,47
../data/MonkeyIsland/TheSecretOfMonkeyIsland/,False,The Secret of Monkey Island,Monkey Island,male,1104,13106,3616,15556,-0.17060579647368002,102.74129245209923,6.315010548975069,37
../data/MonkeyIsland/TheSecretOfMonkeyIsland/,False,The Secret of Monkey Island,Monkey Island,female,79,1123,354,1339,-0.2831617036690446,102.74297064209568,6.099777435843256,3
../data/MonkeyIsland/TheSecretOfMonkeyIsland/,False,The Secret of Monkey Island,Monkey Island,neutral,38,390,198,467,-0.6920745920745919,103.53268065268067,7.904376456876457,7

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

pages = ["https://gamefaqs.gamespot.com/pc/562681-the-secret-of-monkey-island/faqs/23891"]

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
