# 龙腾世纪 · DragonAgeInquisition（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：龙腾世纪, CRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：CRPG


> ⚠️ **数据状态：索引条目** — 本条目仅包含游戏meta信息和角色列表，完整对话数据需运行VideoGameDialogueCorpus的scraper脚本生成。

## 概述
龙腾世纪系列《DragonAgeInquisition》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：龙腾世纪（DragonAge）
- **游戏**：DragonAgeInquisition
- **品类**：CRPG
- **说明**：BioWare奇幻CRPG，对话轮+同伴系统

### 元数据 (meta.json)

```json
{
  "game": "Dragon Age: Inquisition",
  "series": "Dragon Age",
  "year": 1997,
  "status": "in progress",
  "source": "http://www.finalfantasyquotes.com/ff7/script",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "DragonAgeParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [],
    "female": [],
    "neutral": []
  },
  "aliases": {}
}
```

### 角色列表（共12个）

- "Cassandra" :17,
- "PC" :10,
- "CHOICE" :4,
- "Leliana" :3,
- "Dialogue Options" :2,
- "Next" :1,
- "6 - General" :1,
- "5 -  General" :1,
- "4 - General" :1,
- "3 - Investigate" :1,
- "2 - Investigate" :1,
- "1 - Dialogue Options" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/DragonAge/DragonAgeInquisition/,True,Dragon Age: Inquisition,Dragon Age,TOTAL,34,429,93,507,0.1544868035190632,102.17108504398827,6.184111188811189,9
../data/DragonAge/DragonAgeInquisition/,True,Dragon Age: Inquisition,Dragon Age,male,0,NA,NA,NA,NA,NA,NA,0
../data/DragonAge/DragonAgeInquisition/,True,Dragon Age: Inquisition,Dragon Age,female,0,NA,NA,NA,NA,NA,NA,0
../data/DragonAge/DragonAgeInquisition/,True,Dragon Age: Inquisition,Dragon Age,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://daitranscripts.tumblr.com/post/185385333012/the-wrath-of-heaven-pt-1"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
CRPG类型的对话叙事参考。BioWare奇幻CRPG，对话轮+同伴系统
