# 国王密使 · KingsQuest1（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest1》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest1
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest I: Quest for the Crown",
  "series": "King's Quest",
  "year": 1987,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ1SCI_transcript",
  "notes": "See README",
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
    "parser": "KQ1Parser",
    "startText": "id=\"Text.001\">Text.001",
    "endText": "id=\"Vocab\">Vocab"
  },
  "mainPlayerCharacters": [
    "SIR GRAHAM"
  ],
  "characterGroups": {
    "male": [
      "KING EDWARD",
      "SIR GRAHAM",
      "GNOME",
      "RAT",
      "TROLL",
      "WOODCUTTER",
      "ELF",
      "DOCTOR",
      "CASTLE GUARD"
    ],
    "female": [
      "FAIRY GODMOTHER",
      "WITCH"
    ],
    "neutral": [
      "CROWD"
    ]
  },
  "aliases": {
    "KING EDWARD THE BENEVOLENT": "KING EDWARD",
    "SQUEAKY VOICE": "WITCH",
    "KING": "KING EDWARD"
  }
}
```

### 角色列表（共12个）

- "GNOME" :23,
- "KING EDWARD" :17,
- "RAT" :13,
- "WOODCUTTER" :10,
- "TROLL" :10,
- "WITCH" :9,
- "SIR GRAHAM" :9,
- "DOCTOR" :4,
- "FAIRY GODMOTHER" :3,
- "CASTLE GUARD" :2,
- "ELF" :2,
- "CROWD" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest1/,False,King's Quest I: Quest for the Crown,King's Quest,TOTAL,103,1396,276,1656,0.3803164320418606,101.34471242888584,6.387081666043768,12
../data/KingsQuest/KingsQuest1/,False,King's Quest I: Quest for the Crown,King's Quest,male,90,1236,250,1449,0.17165514563106932,102.63771378640779,6.436738581229773,9
../data/KingsQuest/KingsQuest1/,False,King's Quest I: Quest for the Crown,King's Quest,female,12,156,24,203,2.300128205128207,90.14903846153848,6.084476923076923,2
../data/KingsQuest/KingsQuest1/,False,King's Quest I: Quest for the Crown,King's Quest,neutral,1,4,1,4,-2.2299999999999986,118.17500000000001,0.1984,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ1SCI_transcript#Script.000"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
