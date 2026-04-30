# 最终幻想 · FFX（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFX》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFX
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy X",
  "series": "Final Fantasy",
  "year": 2001,
  "status": "superseded",
  "source": "http://www.finalfantasyquotes.com/ffx/script",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "FFQParser",
    "fileType": ".html",
    "characterClassIdentifier": "ff7"
  },
  "mainPlayerCharacters": [
    "Tidus"
  ],
  "characterGroups": {
    "male": [
      "Auron",
      "Barthello",
      "Biran",
      "Bobba",
      "Botta",
      "Braska",
      "Brother",
      "Cid",
      "Clasko",
      "Datto",
      "Gatta",
      "Isaaru",
      "Jassu",
      "Jecht",
      "Jimma",
      "Jyscal",
      "Keepa",
      "Kelk",
      "Keyakku",
      "Kimahri",
      "Kinoc",
      "Letty",
      "Luzzu",
      "Maroda",
      "Mika",
      "Pacce",
      "Rin",
      "Seymour",
      "Tromell",
      "Tidus",
      "Wakka",
      "Yenke"
    ],
    "female": [
      "Calli",
      "Dona",
      "Elma",
      "Lucil",
      "Lulu",
      "Rikku",
      "Shelinda",
      "Tidus' Mother",
      "Yuna",
      "Yunalesca"
    ],
    "neutral": [
      "Aurochs",
      "Fayth",
      "Guado"
    ]
  },
  "aliases": {
    "Main Character": "Tidus",
    "1] Yuna": "Yuna",
    "2] Wakka": "Wakka",
    "3] Rikku": "Rikku",
    "4] Kimahri": "Kimahri",
    "5] Lulu": "Lulu",
    "6] Auron": "Auron",
    "Aurons": "Auron",
    "Kelk Ronso": "Kelk",
    "Young Tidus": "Tidus"
  }
}
```

### 角色列表（共96个）

- "Tidus" :732,
- "ACTION" :716,
- "Yuna" :382,
- "Wakka" :307,
- "Auron" :259,
- "Rikku" :223,
- "Lulu" :162,
- "Seymour" :68,
- "NARRATIVE" :62,
- "Jecht" :54,
- "Cid" :46,
- "Man" :39,
- "Kimahri" :35,
- "Fayth" :33,
- "Woman" :26,
- "Shelinda" :23,
- "Mika" :22,
- "Brother" :21,
- "Kinoc" :21,
- "Tromell" :20,
- "Isaaru" :19,
- "Biran" :19,
- "Braska" :15,
- "Yunalesca" :14,
- "Bobba" :14,
- "Lucil" :13,
- "Dona" :12,
- "Gatta" :11,
- "Datto" :11,
- "Kelk" :10,
- "Crusader" :10,
- "Yenke" :10,
- "Barthello" :9,
- "Aurochs" :9,
- "Girl" :9,
- "Monk" :8,
- "Man 2" :8,
- "Warrior Monk" :7,
- "Clasko" :7,
- "Rin" :7,
- "Elma" :7,
- "CHOICE" :7,
- "Driver" :6,
- "Pacce" :6,
- "Jimma" :6,
- "Young Tidus" :6,
- "Maroda" :5,
- "Al Bhed" :5,
- "Letty" :5,
- "Man 3" :5,
- ... 共96个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFX/,True,Final Fantasy X,Final Fantasy,TOTAL,2818,28059,8429,32514,-0.6182262739753188,105.42404159246823,6.736315345991177,93
../data/FinalFantasy/FFX/,True,Final Fantasy X,Final Fantasy,male,1747,16791,5093,19350,-0.7058612912214421,105.9953687789113,6.7321447400441015,32
../data/FinalFantasy/FFX/,True,Final Fantasy X,Final Fantasy,female,841,8955,2688,10471,-0.4930928389467155,104.53154463724874,6.619431747028795,10
../data/FinalFantasy/FFX/,True,Final Fantasy X,Final Fantasy,neutral,45,522,159,609,-0.5429559748427657,104.80273584905662,6.945238118990819,3

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re

base = "http://www.finalfantasyquotes.com"
indexPage = "http://www.finalfantasyquotes.com/ffx/script/Zanarkand"
index = urlopen(indexPage).read().decode('utf-8')
pages = re.findall("href=['\"](/ffx/script/.*?)['\"]>",index)

pages = [x.replace("&amp;","&") for x in pages]

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
