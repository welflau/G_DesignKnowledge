# 最终幻想 · FFVI_C（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFVI_C》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFVI_C
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy VI",
  "series": "Final Fantasy",
  "year": 1994,
  "status": "superseded",
  "source": "http://www.finalfantasyquotes.com/ff3/script",
  "alternativeMeasure": true,
  "note1": "Note that the site link suggests FF3, but this is in fact the script for FF6",
  "parserParameters": {
    "parser": "FFQParser",
    "fileType": ".html",
    "characterClassIdentifier": "ff7"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [
      "Arvis",
      "Banon",
      "Baram",
      "Cid",
      "Clyde",
      "Curley",
      "Cyan",
      "Daryl",
      "Draco",
      "Duane",
      "Duncan",
      "Edgar",
      "Esper",
      "Gau",
      "Gerad",
      "Gestahl",
      "Gogo",
      "Gungho",
      "Kefka",
      "King",
      "Larry",
      "Leo",
      "Locke",
      "Lone Wolf",
      "Maduin",
      "Moe",
      "Mog",
      "Nerapa",
      "Owain",
      "Owzer",
      "Sabin",
      "Setzer",
      "Sigfried",
      "Shadow",
      "Umaro",
      "Vargas",
      "Wedge"
    ],
    "female": [
      "Celes",
      "Chadarnook",
      "Elayne",
      "Katarin",
      "Lola",
      "Madonna",
      "Rachel",
      "Relm",
      "Terra",
      "Yura"
    ],
    "neutral": [
      "Atma",
      "Chupon",
      "Esper",
      "Ifrit",
      "Odin",
      "Ramuh",
      "Shiva",
      "Ultros",
      "Wrexsoul"
    ]
  },
  "aliases": {
    "Ziegfried": "Sigfried"
  }
}
```

### 角色列表（共127个）

- "ACTION" :421,
- "Locke" :210,
- "Sabin" :164,
- "Edgar" :145,
- "Terra" :124,
- "NARRATIVE" :124,
- "Celes" :121,
- "Cyan" :119,
- "Kefka" :115,
- "Stragos" :89,
- "Man" :65,
- "Gestahl" :57,
- "Setzer" :55,
- "Relm" :51,
- "Banon" :45,
- "Gau" :42,
- "Leo" :38,
- "Shadow" :37,
- "Cid" :33,
- "Soldier" :30,
- "Ultros" :27,
- "Impresario" :24,
- "Maduin" :22,
- "Guard" :22,
- "Ramuh" :21,
- "Wedge" :20,
- "Baram" :18,
- "Elder" :16,
- "Old Man" :16,
- "Gerad" :15,
- "Gungho" :15,
- "Mog" :15,
- "Girl" :15,
- "Aged Man" :14,
- "Henchman" :13,
- "Woman" :13,
- "Child" :12,
- "Clyde" :12,
- "Vargas" :12,
- "Yura" :11,
- "Madonna" :11,
- "Arvis" :11,
- "Doma Sentry" :10,
- "Owzer" :9,
- "Rachel" :9,
- "Trooper" :9,
- "Letter" :8,
- "Elayne" :7,
- "Soldier A" :7,
- "Diary" :6,
- ... 共127个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFVI_C/,True,Final Fantasy VI,Final Fantasy,TOTAL,2141,20696,9403,24858,-0.5586105109764965,102.98778470535582,6.823407311272287,125
../data/FinalFantasy/FFVI_C/,True,Final Fantasy VI,Final Fantasy,male,1263,11556,5363,13813,-0.6449864012531012,103.52470569083309,6.846447432457579,37
../data/FinalFantasy/FFVI_C/,True,Final Fantasy VI,Final Fantasy,female,344,2887,1618,3466,-0.7275827127530903,103.45704782810117,6.700325225307771,10
../data/FinalFantasy/FFVI_C/,True,Final Fantasy VI,Final Fantasy,neutral,67,1066,486,1291,-0.4439487642739657,102.15221033207483,7.196578593874258,9

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re

base = "http://www.finalfantasyquotes.com"
indexPage = "http://www.finalfantasyquotes.com/ff3/script/Part_1"
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
