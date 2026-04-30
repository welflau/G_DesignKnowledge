# 最终幻想 · FFIV_B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFIV_B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFIV_B
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy IV",
  "series": "Final Fantasy",
  "year": 1991,
  "source": "http://www.finalfantasyquotes.com/ff4/script",
  "status": "superseded",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "FFQParser",
    "fileType": ".html",
    "characterClassIdentifier": "ff7"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [
      "Baigan",
      "Cagnazzo",
      "Cecil",
      "Cid",
      "Corio",
      "Edge",
      "Edward",
      "Fusoya",
      "Giott",
      "Golbez",
      "Gramps",
      "Kain",
      "Milon",
      "Palom",
      "Rubicant",
      "Rydia",
      "Tellah",
      "Yang",
      "Zemus",
      "King",
      "Man",
      "Old Man"
    ],
    "female": [
      "Anna",
      "Asura",
      "Calbrinas",
      "Cindy",
      "Luca",
      "Mindy",
      "Porom",
      "Rosa",
      "Sandy",
      "Valvalis",
      "Asura",
      "Queen",
      "Yang's Wife"
    ],
    "neutral": [
      "Zeromus"
    ]
  },
  "aliases": {
    "Voice Of Cagnazzo": "Cagnazzo",
    "Voice Of Cid": "Cid",
    "Voice Of Golbez": "Golbez",
    "Voice Of Kain": "Kain",
    "Palom & Porom": [
      "Palom",
      "Porom"
    ]
  }
}
```

### 角色列表（共77个）

- "Cecil" :333,
- "ACTION" :284,
- "Kain" :112,
- "Rosa" :101,
- "Cid" :87,
- "Edge" :79,
- "Yang" :76,
- "Tellah" :76,
- "Golbez" :69,
- "Edward" :67,
- "Rydia" :60,
- "Porom" :46,
- "Palom" :43,
- "Fusoya" :38,
- "Elder" :37,
- "Giott" :32,
- "King" :28,
- "Rubicant" :15,
- "Girl" :14,
- "Baigan" :13,
- "???" :12,
- "Doctor" :10,
- "Gramps" :9,
- "Milon" :9,
- "Anna" :7,
- "Crew 1" :7,
- "Luca" :6,
- "Valvalis" :6,
- "Voice" :6,
- "Queen" :5,
- "Dark Elf" :5,
- "Yang's Wife" :5,
- "Crew 2" :5,
- "Zeromus" :4,
- "Dark Imp 1" :4,
- "Cagnazzo" :4,
- "Bard" :4,
- "Kids" :3,
- "Cid's Assistant" :3,
- "Dwarf" :3,
- "Cindy" :3,
- "Sandy" :3,
- "Cap'n" :3,
- "Old Man" :3,
- "General" :3,
- "Innkeeper" :3,
- "Researcher" :2,
- "Dwarves" :2,
- "Summon Kid" :2,
- "Asura" :2,
- ... 共77个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFIV_B/,True,Final Fantasy IV,Final Fantasy,TOTAL,1505,11774,4292,14331,-0.1574886258774466,101.07773567732845,7.227214091975448,76
../data/FinalFantasy/FFIV_B/,True,Final Fantasy IV,Final Fantasy,male,1158,8839,3315,10721,-0.23766148685970379,101.51560636879921,7.196855562276535,22
../data/FinalFantasy/FFIV_B/,True,Final Fantasy IV,Final Fantasy,female,187,1150,448,1418,-0.038970885093167595,99.91405298913045,7.388656211180124,12
../data/FinalFantasy/FFIV_B/,True,Final Fantasy IV,Final Fantasy,neutral,4,74,45,100,0.9972792792792795,90.84156456456459,9.906037417417418,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re

base = "http://www.finalfantasyquotes.com"
indexPage = "http://www.finalfantasyquotes.com/ff4/script/Part_1"
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
