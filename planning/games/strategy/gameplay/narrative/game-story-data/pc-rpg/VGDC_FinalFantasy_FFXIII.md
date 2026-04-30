# 最终幻想 · FFXIII（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXIII》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXIII
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy XIII",
  "series": "Final Fantasy",
  "year": 2009,
  "status": "ready",
  "source": "https://en.wikiquote.org/wiki/Final_Fantasy_XIII#Dialogue",
  "sourceFeatures": {
    "type": "wiki",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "NA"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "4",
    "truePositive_notes": "This source is only a sample of dialogue; various main and optional conversations are omitted.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "sampleOnly": true,
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "WikiquoteParser",
    "fileType": ".html",
    "scriptStartCue": "<h2><span class=\"mw-headline\" id=\"Lightning_-_Battle\">",
    "scriptMidCue": "<h2><span class=\"mw-headline\" id=\"Dialogue\">",
    "scriptEndCue": "<span class=\"mw-headline\" id=\"External_Links\">External Links</span>",
    "lineNode": "li",
    "characterNameNode": "b",
    "narrativeLineRegexp": "^\\["
  },
  "mainPlayerCharacters": [
    "Lightning",
    "Snow",
    "Vanille",
    "Fang",
    "Hope",
    "Sazh"
  ],
  "characterGroups": {
    "male": [
      "Amodar",
      "Barthandelus",
      "Cid",
      "Commander",
      "Dajh",
      "Gadot",
      "Galenth",
      "Hope",
      "Maqui",
      "PSICOM Marauder",
      "PSICOM soldier",
      "Rygdea",
      "Sazh",
      "Snow",
      "Titan",
      "Yaag",
      "Yuj",
      "staff 2",
      "staff 3"
    ],
    "female": [
      "Lightning",
      "Fang",
      "Jihl",
      "Lebreau",
      "Nora",
      "Serah",
      "Vanille",
      "Reporter",
      "staff 1"
    ],
    "neutral": [
      "Orphan",
      "PSICOM Soldier"
    ]
  },
  "aliases": {
    "'Sazh": "Sazh",
    "Sazh'": "Sazh",
    "Vanille (narrating)": "Vanille",
    "Galenth's Voice": "Galenth",
    "Lebrau": "Lebreau",
    "Lightning:": "Lightning",
    "Marqui": "Maqui",
    "Yaag Rosch": "Yaag",
    "Snow Villiers": "Snow",
    "Sazh Katzroy": "Sazh",
    "Oerba Dia Vanille": "Vanille",
    "Hope Estheim": "Hope",
    "Oerba Yun Fang": "Fang",
    "Cid Raines": "Cid",
    "Galenth Dysley/Barthandelus": "Galenth"
  }
}
```

### 角色列表（共31个）

- "ACTION" :402,
- "Lightning" :173,
- "Vanille" :153,
- "Sazh" :149,
- "Snow" :149,
- "Hope" :114,
- "Fang" :92,
- "Galenth" :58,
- "Cid" :29,
- "Serah" :19,
- "Yaag" :13,
- "Orphan" :12,
- "Jihl" :10,
- "Gadot" :8,
- "Yuj" :6,
- "Maqui" :5,
- "Nora" :5,
- "Dajh" :5,
- "Lebreau" :4,
- "Amodar" :4,
- "Commander" :3,
- "Titan" :2,
- "Rygdea" :2,
- "PSICOM Marauder" :2,
- "Reporter" :2,
- "PSICOM soldier" :1,
- "Barthandelus" :1,
- "staff 3" :1,
- "staff 2" :1,
- "staff 1" :1,
- "PSICOM Soldier" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXIII/,False,Final Fantasy XIII,Final Fantasy,TOTAL,1025,12674,3037,14981,-0.01454397344122782,102.5997886798706,6.6217531676313,30
../data/FinalFantasy/FFXIII/,False,Final Fantasy XIII,Final Fantasy,male,553,7109,1656,8414,0.050348458577717636,102.3477001345678,6.6102888572898335,19
../data/FinalFantasy/FFXIII/,False,Final Fantasy XIII,Final Fantasy,female,459,5173,1320,6079,-0.19495985712528174,103.44041975891722,6.541399401671851,9
../data/FinalFantasy/FFXIII/,False,Final Fantasy XIII,Final Fantasy,neutral,13,392,60,488,1.6477959183673487,94.88529931972789,7.948333945578231,2

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://en.wikiquote.org/wiki/Final_Fantasy_XIII"

req = Request(
    page, 
    headers={
        'User-Agent': 'XYZ/3.0'
    }
)

html = urlopen(req, timeout=10).read().decode('utf-8')
o = open("raw/Final Fantasy XIII - Wikiquote.html",'w')
o.write(html)
o.close()
```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
