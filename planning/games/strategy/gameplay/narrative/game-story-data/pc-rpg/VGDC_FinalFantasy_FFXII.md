# 最终幻想 · FFXII（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXII》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXII
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy XII",
  "series": "Final Fantasy",
  "year": 2006,
  "status": "superseded",
  "alternativeMeasure": true,
  "source": "http://www.finalfantasyquotes.com/ff12/script",
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "FFQParser",
    "fileType": ".html",
    "characterClassIdentifier": "ff7"
  },
  "mainPlayerCharacters": [
    "Vaan"
  ],
  "characterGroups": {
    "male": [
      "Al-cid",
      "Anastasis",
      "Ba'gamnan",
      "Balthier",
      "Basch",
      "Havharo",
      "Kytes",
      "Larsa",
      "Migelo",
      "Nono",
      "Raz",
      "Reddas",
      "Reks",
      "Rikken",
      "Tomaj",
      "Vaan",
      "Vayne",
      "Vossler",
      "Zargabaath",
      "Bwagi",
      "Doctor Cid",
      "Judge Bergan",
      "Judge Gabranth",
      "Judge Ghis",
      "Judge Zargabaath",
      "Jules",
      "Lamont",
      "Old Dalan",
      "Rasler",
      "War-chief Supinelu"
    ],
    "female": [
      "Amalia",
      "Ashe",
      "Drace",
      "Fran",
      "Jote",
      "Mjrn",
      "Penelo",
      "Elza",
      "Judge Drace"
    ],
    "genderless": [
      "Venat"
    ],
    "neutral": [
      "Bangaa",
      "???",
      "Occuria",
      "Occurian",
      "Rabanastrans",
      "Tonberry"
    ]
  },
  "aliases": {
    "Ashe": "Amalia",
    "Gabranth": "Judge Gabranth",
    "Vayne Novus": "Vayne"
  }
}
```

### 角色列表（共114个）

- "ACTION" :667,
- "Vaan" :270,
- "Balthier" :235,
- "Ashe" :155,
- "Basch" :125,
- "Penelo" :100,
- "Fran" :90,
- "Vayne" :52,
- "Larsa" :48,
- "Vossler" :43,
- "Man" :36,
- "Marquis" :35,
- "Reddas" :31,
- "Judge Gabranth" :27,
- "Judge Ghis" :27,
- "Imperial Soldier" :27,
- "Doctor Cid" :26,
- "Al-cid" :24,
- "Judge" :24,
- "Reks" :19,
- "Jules" :17,
- "Migelo" :17,
- "Old Dalan" :16,
- "Emperor" :15,
- "Resistance Pilot" :14,
- "Gabranth" :14,
- "???" :14,
- "Blonde-haired Man" :14,
- "Ba'gamnan" :13,
- "Lamont" :12,
- "Anastasis" :11,
- "Judge Drace" :11,
- "Amalia" :11,
- "Kytes" :11,
- "Jote" :10,
- "Raz" :9,
- "Elza" :9,
- "Rikken" :9,
- "Mjrn" :9,
- "Senate Member" :9,
- "Judge Zargabaath" :8,
- "Soldier" :8,
- "Assistant" :7,
- "Grey-haired Man" :7,
- "Occuria" :6,
- "Great-chief" :6,
- "War-chief Supinelu" :6,
- "Havharo" :6,
- "Imperial" :5,
- "Boy" :5,
- ... 共114个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXII/,True,Final Fantasy XII,Final Fantasy,TOTAL,1817,25785,6273,30698,0.061422829606595286,101.94342790468252,6.461329648325227,113
../data/FinalFantasy/FFXII/,True,Final Fantasy XII,Final Fantasy,male,1072,16107,3826,19166,0.0928787513236049,101.8949576918647,6.4421753746435195,30
../data/FinalFantasy/FFXII/,True,Final Fantasy XII,Final Fantasy,female,396,4960,1264,5814,-0.22792670477745958,103.68587893017559,6.260118798489179,9
../data/FinalFantasy/FFXII/,True,Final Fantasy XII,Final Fantasy,genderless,4,101,22,128,1.1549099909991014,94.95938568856887,7.30361503150315,1
../data/FinalFantasy/FFXII/,True,Final Fantasy XII,Final Fantasy,neutral,29,568,118,652,-0.1676414418715666,104.83796968250181,6.821977894485557,6

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re

base = "http://www.finalfantasyquotes.com"
indexPage = "http://www.finalfantasyquotes.com/ff12/script/The__Prologue"
index = urlopen(indexPage).read().decode('utf-8')
pages = re.findall("href=['\"](/ff12/script/.*?)['\"]>",index)

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
