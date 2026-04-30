# 最终幻想 · FFI（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFI》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFI
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy",
  "series": "Final Fantasy",
  "year": 1987,
  "status": "ready",
  "source": "https://archive.rpgamer.com/games/ff/ff1/info/ff1_script.txt",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "complete",
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
    "parser": "FF1Parser",
    "fileType": ".txt",
    "startText": "~~~~~~~~~~~~~~~~~",
    "endText": "Author's Notes"
  },
  "notes": "See README",
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [
      "Man 1",
      "Man 10",
      "Man 11",
      "Man 12",
      "Man 13",
      "Man 14",
      "Man 15",
      "Man 16",
      "Man 17",
      "Man 18",
      "Man 19",
      "Man 2",
      "Man 20",
      "Man 21",
      "Man 3",
      "Man 4",
      "Man 5",
      "Man 6",
      "Man 7",
      "Man 8",
      "Man 9",
      "Sage",
      "Dwarf",
      "Old Man",
      "Guard 1",
      "Guard 2",
      "Guard 3",
      "Guard 4",
      "Guard 5",
      "Guard 6",
      "Scholar",
      "Bikke",
      "King",
      "Dr. Unne",
      "Dr. Unne's Brother",
      "Prince",
      "Nerrick",
      "Smith",
      "Grounds Keeper",
      "Garland",
      "Pirate",
      "Young Man",
      "Kope",
      "Soldier",
      "Old Sage",
      "Sage Before Lukahn",
      "Lukahn",
      "Jim The Dwarf",
      "Sarda",
      "Vampire",
      "Astos",
      "Elf Prince",
      "King Of Coneria",
      "Queen's Guard",
      "Boy",
      "Titan",
      "First Officer",
      "Bahamut"
    ],
    "female": [
      "Mermaid 1",
      "Mermaid 10",
      "Mermaid 11",
      "Mermaid 2",
      "Mermaid 3",
      "Mermaid 4",
      "Mermaid 5",
      "Mermaid 6",
      "Mermaid 7",
      "Mermaid 8",
      "Mermaid 9",
      "Woman 1",
      "Woman 2",
      "Woman 3",
      "Woman 4",
      "Woman 5",
      "Woman 6",
      "Woman 7",
      "Woman 8",
      "Young Woman",
      "Matoya",
      "Princess",
      "Witch",
      "Queen Jane",
      "Lady",
      "Elderly Lady",
      "Underhill's Daughter",
      "Kary",
      "Old Woman",
      "Elderly Woman",
      "Arylon",
      "Princess's Sister"
    ],
    "neutral": [
      "Elf",
      "Dragon",
      "Person 1",
      "Person 2",
      "Person 3",
      "Person 4",
      "Person 5",
      "Person 6",
      "Person 7",
      "Person 8",
      "Citizen 1",
      "Citizen 2",
      "Citizen 3",
      "Citizen 4",
      "Person 1",
      "Person 2",
      "Person 3",
      "Person 4",
      "Person 5",
      "Person 6",
      "Person 7",
      "Person 8",
      "Bat",
      "Robot",
      "Attendant",
      "Guard Dragon",
      "Kraken",
      "Fairy",
      "Broom",
      "Computer"
    ]
  },
  "aliases": {
    "Dr.Unne": "Dr. Unne",
    "Oldman": "Old Man",
    "Princess' Sister": "Princess's Sister"
  }
}
```

### 角色列表（共115个）

- "LOCATION" :247,
- "ACTION" :211,
- "COMMENT" :33,
- "Sage" :19,
- "Dwarf" :14,
- "Elf" :13,
- "Dragon" :11,
- "Old Man" :11,
- "Bat" :5,
- "Scholar" :5,
- "Robot" :4,
- "Bahamut" :3,
- "Dr. Unne" :3,
- "Attendant" :3,
- "Young Woman" :3,
- "Bikke" :3,
- "Matoya" :3,
- "King" :3,
- "Princess" :3,
- "Dr. Unne's Brother" :2,
- "Witch" :2,
- "Guard Dragon" :2,
- "Prince" :2,
- "Nerrick" :2,
- "Smith" :2,
- "Grounds Keeper" :2,
- "Garland" :2,
- "Queen Jane" :2,
- "Princess's Sister" :2,
- "Computer" :1,
- "Citizen 4" :1,
- "Citizen 3" :1,
- "Citizen 2" :1,
- "Citizen 1" :1,
- "Person 8" :1,
- "Person 7" :1,
- "Person 6" :1,
- "Person 5" :1,
- "Person 4" :1,
- "Person 3" :1,
- "Person 2" :1,
- "Guard 6" :1,
- "Guard 5" :1,
- "Person 1" :1,
- "Man 21" :1,
- "Lady" :1,
- "Man 20" :1,
- "Mermaid 11" :1,
- "Kraken" :1,
- "Mermaid 10" :1,
- ... 共115个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFI/,False,Final Fantasy,Final Fantasy,TOTAL,212,2763,544,3332,0.6208670176811246,99.65762038345468,6.522944656277278,112
../data/FinalFantasy/FFI/,False,Final Fantasy,Final Fantasy,male,117,1563,307,1869,0.5057427772949801,100.50466279455068,6.5358439960320185,58
../data/FinalFantasy/FFI/,False,Final Fantasy,Final Fantasy,female,41,464,98,559,0.47247888810696637,100.10816502463057,6.38957357494722,32
../data/FinalFantasy/FFI/,False,Final Fantasy,Final Fantasy,neutral,54,736,137,904,0.9986607426213912,97.47128371945416,6.584689777054903,22

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path

url = "https://archive.rpgamer.com/games/ff/ff1/info/ff1_script.txt"

html = urlopen(url).read().decode("utf-8", "backslashreplace")
o = open("raw/page01.txt",'w')
o.write(html)
o.close()

```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
