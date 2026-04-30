# 国王密使 · KingsQuest5（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest5》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest5
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest V",
  "series": "King's Quest",
  "year": 1992,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ5NES_transcript",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": false,
    "choices": "NA"
  },
  "notes": "This is the NES release",
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "One line missing from source (Cedric: See! Dead end! Let's go back now); I suspect this is oversight, as it appears in the floppy disc transcript.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "KQ5ParserNES",
    "startText": "<h2><span class=\"mw-headline\" id=\"Narrator\">Narrator",
    "endText": "<span class=\"mw-headline\" id=\"Credits\">Credits</span>",
    "characterTags": [
      "h2"
    ],
    "locationTags": [
      "h3"
    ]
  },
  "mainPlayerCharacters": [
    "Alexander",
    "Narrator",
    "Cedric"
  ],
  "characterGroups": {
    "male": [
      "Alexander",
      "Cedric",
      "Crispin",
      "Dink",
      "Eagle",
      "Elf",
      "Gnome",
      "Graham",
      "Herbert",
      "Hermit",
      "Mordack",
      "Shoemaker",
      "Tailor",
      "Toymaker",
      "Man fixing Wagon",
      "Manannan",
      "Baker",
      "Yeti",
      "Antony",
      "Arabian Knights/Bandits",
      "Irate Customer"
    ],
    "neutral": [
      "Wolf",
      "Rat",
      "Narrator"
    ],
    "female": [
      "Willow Tree/Alicia",
      "Beetrice",
      "Madame Mushka",
      "Cassima",
      "Harpy 1",
      "Harpy 2 (Minotta)",
      "Harpy 3 (Cruleena)",
      "Icebella",
      "Shoemaker's Wife"
    ]
  },
  "aliases": {
    "Shoesmaker's Wife": "Shoemaker's Wife",
    "Narrator": {
      "Cedric": [
        "Mooaaann!"
      ]
    },
    "Harpies": {
      "Harpy 1": [
        "Where did you find HIM, Minotta?",
        "What is he doing?"
      ],
      "Harpy 2 (Minotta)": [
        "We found him on the beach",
        "Don't be so picky."
      ],
      "Harpy 3 (Cruleena)": [
        "I don't know"
      ],
      "Harpies 1 and 2": [
        "Hey, that's not fair!"
      ]
    },
    "Harpies 1 and 2": [
      "Harpy 1",
      "Harpy 2 (Minotta)"
    ]
  }
}
```

### 角色列表（共34个）

- "Narrator" :524,
- "LOCATION" :77,
- "Cedric" :32,
- "Graham" :31,
- "Hermit" :28,
- "Crispin" :19,
- "Cassima" :16,
- "Icebella" :12,
- "Willow Tree/Alicia" :11,
- "Irate Customer" :11,
- "Toymaker" :9,
- "Shoemaker's Wife" :8,
- "Tailor" :7,
- "Antony" :6,
- "Eagle" :5,
- "Shoemaker" :5,
- "Arabian Knights/Bandits" :4,
- "Wolf" :4,
- "Herbert" :3,
- "Harpy 2 (Minotta)" :3,
- "Harpy 1" :3,
- "Man fixing Wagon" :3,
- "Baker" :3,
- "Rat" :2,
- "Harpy 3 (Cruleena)" :2,
- "Manannan" :2,
- "Madame Mushka" :2,
- "Elf" :2,
- "Dink" :1,
- "Beetrice" :1,
- "Alexander" :1,
- "Mordack" :1,
- "Gnome" :1,
- "Yeti" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest5/,False,King's Quest V,King's Quest,TOTAL,763,10833,1958,13495,1.2673692285526759,95.83051132562548,6.753208701168176,33
../data/KingsQuest/KingsQuest5/,False,King's Quest V,King's Quest,male,175,2513,561,2891,-0.26806429028942524,104.96295840595042,6.177230796932598,21
../data/KingsQuest/KingsQuest5/,False,King's Quest V,King's Quest,neutral,530,7277,1180,9397,2.05279053227839,91.32912638205353,7.056115733620905,3
../data/KingsQuest/KingsQuest5/,False,King's Quest V,King's Quest,female,58,1043,215,1207,-0.042629445472586625,104.00867283551474,6.087414893977569,9

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ5NES_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
