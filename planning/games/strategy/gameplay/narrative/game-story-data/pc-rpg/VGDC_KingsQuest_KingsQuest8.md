# 国王密使 · KingsQuest8（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest8》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest8
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest VIII",
  "series": "King's Quest",
  "year": 1998,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ8_transcript#Connor",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "complete",
    "dialogueOrder": false,
    "choices": "NA"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "The source doesn't give structure/order to the dialogue, but all tested lines were included.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "KQ5Parser",
    "startText": "ALMOST ANGRY AT THE TAUNTING BEAST",
    "endText": "printfooter",
    "characterTags": [
      "h2"
    ]
  },
  "mainPlayerCharacters": [
    "Connor"
  ],
  "characterGroups": {
    "male": [
      "Connor",
      "Graham",
      "Wizard",
      "Azriel",
      "James",
      "Archons",
      "Mudge",
      "Hector",
      "Lucreto",
      "Thork",
      "King Gryph",
      "Henchmen",
      "Lad",
      "Old/Young Guy",
      "Oracle of the Tree",
      "Ferryman",
      "Weirdling Tradesman",
      "Hillmen",
      "Armorer Gnome",
      "Daventry Official",
      "Sage Gnome",
      "Skeletons",
      "Weapon Gnome",
      "Gryphs",
      "Fire Dwarves",
      "Ice Orcs"
    ],
    "female": [
      "Sarah",
      "Lady of the Lake",
      "Unicorn/Ugly Beast",
      "Swamp Witch",
      "Crystal Dragon",
      "Frost Nymphs",
      "Freesa",
      "Gwennie",
      "Sylph",
      "Apothecary Gnome",
      "Shaman"
    ],
    "neutral": [
      "Gnome",
      "Unseen Voice",
      "Raven",
      "Whispering Weeds",
      "Wisps"
    ]
  },
  "aliases": {
    "Old/young guy": "Old/Young Guy"
  }
}
```

### 角色列表（共42个）

- "Connor" :865,
- "Apothecary Gnome" :59,
- "Hillmen" :44,
- "Skeletons" :44,
- "Wizard" :40,
- "Weirdling Tradesman" :37,
- "Archons" :33,
- "Wisps" :32,
- "Freesa" :30,
- "Armorer Gnome" :25,
- "Weapon Gnome" :23,
- "Oracle of the Tree" :22,
- "Sage Gnome" :21,
- "King Gryph" :20,
- "Unicorn/Ugly Beast" :19,
- "Old/Young Guy" :17,
- "Lucreto" :17,
- "Ferryman" :16,
- "Sylph" :16,
- "Gwennie" :14,
- "Henchmen" :14,
- "Fire Dwarves" :12,
- "Ice Orcs" :11,
- "Gnome" :10,
- "Azriel" :9,
- "Frost Nymphs" :8,
- "Gryphs" :8,
- "Crystal Dragon" :8,
- "Shaman" :7,
- "Thork" :7,
- "Unseen Voice" :6,
- "Hector" :6,
- "James" :6,
- "Mudge" :4,
- "Daventry Official" :4,
- "Sarah" :4,
- "Lad" :3,
- "Graham" :3,
- "Whispering Weeds" :1,
- "Swamp Witch" :1,
- "Lady of the Lake" :1,
- "Raven" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest8/,False,King's Quest VIII,King's Quest,TOTAL,1528,15880,4050,19181,0.19206931616755263,100.66926554093979,7.161994841558602,42
../data/KingsQuest/KingsQuest8/,False,King's Quest VIII,King's Quest,male,1311,13266,3362,16017,0.1958798780958677,100.68625582271973,7.126856873394461,26
../data/KingsQuest/KingsQuest8/,False,King's Quest VIII,King's Quest,female,167,2199,561,2657,0.1963791514373341,100.63622611639227,7.37810647450348,11
../data/KingsQuest/KingsQuest8/,False,King's Quest VIII,King's Quest,neutral,50,415,125,507,0.12070361445783284,100.1105012048193,7.149412963855421,5

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ8_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
