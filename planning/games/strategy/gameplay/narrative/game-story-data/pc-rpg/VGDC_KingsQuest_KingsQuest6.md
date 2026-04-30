# 国王密使 · KingsQuest6（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest6》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest6
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest VI",
  "series": "King's Quest",
  "year": 1992,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ6_transcript",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "complete",
    "dialogueOrder": true,
    "choices": "NA"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "Error checking revealed coding error (mix-up of two ferrymen - Charon and Hassan). Rectified. ",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "KQ6Parser",
    "startTextPt1": "span class=\"mw-headline\" id=\"0.msg",
    "startTextPt2": "<span class=\"mw-headline\" id=\"By_Character\">By Character</span>",
    "endText": "id=\"KQ6CD_transcript\">KQ6CD transcript",
    "characterCues": {
      "6": {
        "730.msg 1 0 7": "Mite",
        "730.msg 1 0 2": "Wolf",
        "820.msg 1 0 11": "Howel",
        "820.msg 1 0 13": "Howel",
        "820.msg 1 0 1": "Guard Dog",
        "850.msg 1 0 1": "Wolf",
        "850.msg 1 0 9": "Bay",
        "860.msg 1 0 3": "Jowels",
        "870.msg 1 0 3": "Mite",
        "880.msg 1 0 2": "Bay",
        "880.msg 1 0 3": "Bay",
        "880.msg 1 0 6": "Bay",
        "880.msg 1 0 5": "Bay"
      },
      "7": {
        "730.msg 1 0 2": "Bay",
        "820.msg 1 0 11": "Rolf",
        "820.msg 1 0 13": "Rolf",
        "820.msg 1 0 1": "Shrew",
        "850.msg 1 0 1": "Bay",
        "850.msg 1 0 9": "Wolf",
        "860.msg 1 0 3": "Mite",
        "870.msg 1 0 3": "Jowels",
        "880.msg 1 0 2": "Wolf",
        "880.msg 1 0 3": "Wolf",
        "880.msg 1 0 6": "Wolf",
        "880.msg 1 0 5": "Wolf"
      }
    }
  },
  "mainPlayerCharacters": [
    "Alexander",
    "Narrator"
  ],
  "characterGroups": {
    "male": [
      "Alexander",
      "Alhazred",
      "Ali",
      "Beast",
      "Bookworm",
      "Bump-on-a-log",
      "Captain Saladin",
      "Hassan",
      "Cook",
      "Gardener",
      "Ghost Child",
      "Graham",
      "Growlf",
      "Gruff",
      "Howel",
      "Mite",
      "Wolf",
      "Bay",
      "Jowels",
      "Rolf",
      "Shrew",
      "Guard Dog",
      "Jollo",
      "King Caliphim",
      "Lampseller",
      "Lord Azure",
      "Minotaur",
      "Old Man",
      "Pawn Shop Owner",
      "Rolf",
      "Rotten Tomato",
      "Samhain",
      "Sense Gnomes",
      "Shamir Shamazel",
      "Sight Gnome",
      "Smell Gnome",
      "Sound Gnome",
      "Stick-in-the-mud",
      "Swimming Child",
      "Taste Gnome",
      "Touch Gnome",
      "Waiter",
      "Woof",
      "Winged One Guard 1",
      "Winged One Guard 2",
      "Druid 1",
      "Druid 2",
      "Narrator",
      "Charon"
    ],
    "female": [
      "Beauty",
      "Black Widow",
      "Cassima",
      "Lady Aeriel",
      "Lady Celeste",
      "Mother Ghost",
      "Old Woman",
      "Queen Allaria",
      "Red Chess Queen",
      "Rosella",
      "Serving Women",
      "Stepmother",
      "The Oracle",
      "Valanice",
      "Wallflowers",
      "White Chess Queen",
      "Winged One Girl"
    ],
    "neutral": [
      "Clinging Vines",
      "Gate",
      "Dangling Participle",
      "Tomato Vines",
      "Sour Grapes",
      "Oyster",
      "Red Chess Knight",
      "White Chess Knight",
      "Townsfolk",
      "Ticket Taker",
      "Diphthong",
      "Oxymoron",
      "Guard Dog Statue",
      "Undead",
      "Hole-in-the-wall",
      "Baby's Tears",
      "Spirits"
    ]
  },
  "aliases": {
    "1": "Winged One Girl",
    "2": "Alexander",
    "3": "Minotaur",
    "4": "Lady Celeste",
    "5": "Jollo",
    "6": "Howel",
    "7": "Rolf",
    "8": "Guard Dog Statue",
    "9": "Dangling Participle",
    "10": "Stepmother",
    "11": "King Caliphim",
    "12": "Valanice",
    "13": "Captain Saladin",
    "14": "Gruff",
    "15": "Woof",
    "16": "Lampseller",
    "17": "Beauty",
    "18": "Winged One Guard 1",
    "19": "The Oracle",
    "20": "Lord Azure",
    "21": "Lady Aeriel",
    "22": "Swimming Child",
    "23": "Hassan",
    "24": "Alhazred",
    "28": "Cassima",
    "29": "Shamir Shamazel",
    "30": "Old Woman",
    "31": "Winged One Guard 2",
    "32": "Shamir Shamazel",
    "33": "Ali",
    "34": "Old Man",
    "35": "Pawn Shop Owner",
    "36": "Sense Gnomes",
    "37": "Oyster",
    "38": "Hole-in-the-wall",
    "39": "Wallflowers",
    "40": "Mother Ghost",
    "41": "Undead",
    "43": "Bookworm",
    "44": "Oxymoron",
    "45": "Diphthong",
    "46": "Black Widow",
    "47": "Stick-in-the-mud",
    "48": "Bump-on-a-log",
    "49": "Cook",
    "50": "Rotten Tomato",
    "51": "Tomato Vines",
    "52": "White Chess Queen",
    "53": "Red Chess Queen",
    "55": "Gardener",
    "56": "Beast",
    "57": "Waiter",
    "58": "Gate",
    "59": "Druid 1",
    "60": "Druid 2",
    "62": "Queen Allaria",
    "6
```

### 角色列表（共82个）

- "ACTION" :3181,
- "Narrator" :3069,
- "Alexander" :685,
- "Pawn Shop Owner" :101,
- "Cassima" :95,
- "Captain Saladin" :67,
- "Alhazred" :66,
- "Jollo" :59,
- "Ali" :43,
- "Hassan" :42,
- "Beauty" :33,
- "Shamir Shamazel" :33,
- "Bookworm" :32,
- "Gruff" :28,
- "Howel" :26,
- "Bay" :25,
- "Samhain" :25,
- "Beast" :24,
- "White Chess Queen" :24,
- "Red Chess Queen" :23,
- "Bump-on-a-log" :22,
- "Wolf" :21,
- "Gate" :21,
- "Stick-in-the-mud" :20,
- "Black Widow" :17,
- "The Oracle" :17,
- "Old Woman" :17,
- "Queen Allaria" :15,
- "Lord Azure" :14,
- "Dangling Participle" :13,
- "Lampseller" :13,
- "King Caliphim" :13,
- "Rolf" :12,
- "Gardener" :12,
- "Rotten Tomato" :12,
- "Old Man" :12,
- "Sense Gnomes" :11,
- "Winged One Guard 1" :11,
- "Ghost Child" :10,
- "Valanice" :10,
- "Spirits" :9,
- "Stepmother" :9,
- "Swimming Child" :9,
- "Clinging Vines" :8,
- "Minotaur" :8,
- "Lady Celeste" :8,
- "Woof" :8,
- "Mite" :7,
- "White Chess Knight" :7,
- "Red Chess Knight" :7,
- ... 共82个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest6/,False,King's Quest VI,King's Quest,TOTAL,4968,72074,12381,88630,1.1908808605489263,96.89301390556747,6.521341038530302,81
../data/KingsQuest/KingsQuest6/,False,King's Quest VI,King's Quest,male,4582,66597,11292,82198,1.2743745842859564,96.4304398691811,6.575749048633079,47
../data/KingsQuest/KingsQuest6/,False,King's Quest VI,King's Quest,female,288,4585,867,5388,0.3390652534026657,102.05079193599308,5.74814352189012,17
../data/KingsQuest/KingsQuest6/,False,King's Quest VI,King's Quest,neutral,98,892,222,1044,-0.21221064113440669,103.74056821395388,6.4910627519896575,17

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ6_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
