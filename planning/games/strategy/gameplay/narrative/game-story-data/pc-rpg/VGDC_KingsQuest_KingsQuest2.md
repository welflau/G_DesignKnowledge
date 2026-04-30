# 国王密使 · KingsQuest2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest2
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest II: Romancing the Throne",
  "series": "King's Quest",
  "year": 1987,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ2_transcript",
  "notes": "See Readme",
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
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "KQ4Parser",
    "startText": "<span class=\"mw-headline\" id=\"Logic.000\">Logic.000</span>",
    "endText": "<span class=\"mw-headline\" id=\"Logic.180\">Logic.180</span>",
    "splitString": "(\\\\\".+?\\\\\")",
    "quoteRecogniser": "\\\"",
    "characterCues": {
      "genie": "Genie",
      "muffled": "Grandma",
      "old": "Antique Shop Lady",
      "cheery": "Antique Shop Lady",
      "Grandma": "Grandma",
      "fairy": "Fairy",
      "monk": "Monk",
      "Hood": "Little Red Riding Hood"
    },
    "skipLines": [
      "%w1",
      "%w2",
      "%w3",
      "closed.",
      "open.",
      "breaking and entering.",
      "Where am I?",
      "King's Quest III--To heir is human, to really foul things up takes a computer"
    ]
  },
  "mainPlayerCharacters": [
    "Graham"
  ],
  "characterGroups": {
    "male": [
      "Genie",
      "Graham",
      "Monk"
    ],
    "neutral": [
      "Winged Horse",
      "Fish"
    ],
    "female": [
      "Antique Shop Lady",
      "Fairy",
      "Grandma",
      "Valanice",
      "Little Red Riding Hood"
    ]
  },
  "aliases": {
    "Unknown": {
      "Winged Horse": [
        "Thank you, kind sir",
        "SSSsssssss!"
      ],
      "Graham": [
        "YECCHHH!!"
      ],
      "Valanice": [
        "My name is Valanice",
        "Oh, Graham, I am forever",
        "Yes, of course I will!",
        "I love you, too!",
        "Come closer, kind sir."
      ],
      "Fish": [
        "In return for saving my life, I wish to offer you a ride across this ocean"
      ]
    }
  }
}
```

### 角色列表（共11个）

- "SYSTEM" :1000,
- "Antique Shop Lady" :16,
- "Grandma" :11,
- "Genie" :7,
- "Valanice" :5,
- "Monk" :5,
- "Graham" :4,
- "Fairy" :2,
- "Little Red Riding Hood" :2,
- "Winged Horse" :2,
- "Fish" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest2/,False,King's Quest II: Romancing the Throne,King's Quest,TOTAL,55,402,70,469,0.41638095238095296,102.306,5.453211385927505,10
../data/KingsQuest/KingsQuest2/,False,King's Quest II: Romancing the Throne,King's Quest,male,16,69,19,81,-0.32151029748283655,103.8359038901602,5.189669794050342,3
../data/KingsQuest/KingsQuest2/,False,King's Quest II: Romancing the Throne,King's Quest,neutral,3,60,7,69,1.3228571428571438,100.84500000000003,6.16697619047619,2
../data/KingsQuest/KingsQuest2/,False,King's Quest II: Romancing the Throne,King's Quest,female,36,273,42,319,0.7332783882783893,101.38255494505496,5.404870695970695,5

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ2_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
