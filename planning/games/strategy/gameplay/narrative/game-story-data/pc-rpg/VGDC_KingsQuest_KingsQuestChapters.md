# 国王密使 · KingsQuestChapters（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuestChapters》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuestChapters
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest Chapters",
  "series": "King's Quest",
  "year": 2015,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQC1_transcript",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": false,
    "choices": "NA"
  },
  "notes": "see Readme",
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "A line of dialogue was missing from Chapter 1 re the ridiculous feeding contraption; completeness changed to high.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "KQCParser",
    "optionsForChapters": {
      "page01.html": {
        "startText": "<h3><span class=\"mw-headline\" id=\"Achaka_VO\">Achaka VO",
        "endText": "class=\"mw-headline\" id=\"Graham_Game\"",
        "reForDialogue": "\\(Text=\".+?\""
      },
      "page02.html": {
        "startText": "class=\"mw-headline\" id=\"Chapter_2_Transcript\"",
        "endText": "class=\"page-footer\"",
        "reForDialogue": "=\".+?\""
      },
      "page03.html": {
        "startText": "class=\"mw-headline\" id=\"VO_E3_Acorn",
        "endText": "class=\"page-footer\"",
        "reForDialogue": "Text=\".+?\""
      },
      "page04.html": {
        "startText": "class=\"mw-headline\" id=\"Forest_Rood_Trip_Road",
        "endText": "class=\"page-footer\"",
        "reForDialogue": "=\".+?\""
      },
      "page05.html": {
        "startText": "<span class=\"mw-headline\" id=\"AchakaVO\">AchakaVO",
        "endText": "class=\"page-footer\"",
        "reForDialogue": "=\".*?\""
      },
      "page06.html": {
        "startText": "class=\"mw-headline\" id=\"VO_E6_Gwendolyn",
        "endText": "class=\"page-footer\"",
        "reForDialogue": "Text=\".*?\""
      }
    }
  },
  "mainPlayerCharacters": [
    "Graham",
    "Gwendolyn"
  ],
  "characterGroups": {
    "male": [
      "Chester",
      "Gart",
      "Graham",
      "Kyle",
      "Merchant",
      "Mordon",
      "Olfie",
      "Royal Guard 1",
      "Royal Guard 2",
      "Royal Guard 3",
      "Wente",
      "Whisper",
      "Larry",
      "Alexander",
      "Waddles",
      "Manannan",
      "Royal Knight",
      "Achaka"
    ],
    "female": [
      "Acorn",
      "Amaya",
      "Bramble",
      "Gwendolyn",
      "Muriel",
      "Hagatha",
      "Neese",
      "Valanice",
      "Vee",
      "Icebella",
      "Pillare",
      "Sphinx",
      "Rosella",
      "Taskia"
    ],
    "neutral": [
      "EscRoomPullSwitch08"
    ]
  },
  "aliases": {
    "AC": "Acorn",
    "Give": "Acorn",
    "AB": "Amaya",
    "Ask1": "Amaya",
    "Ask2": "Amaya",
    "Ask3": "Amaya",
    "Ask4": "Amaya",
    "Ask5": "Amaya",
    "Ask6": "Amaya",
    "GiveStarFruit": "Amaya",
    "AK": "Achaka",
    "BF": "Bramble",
    "VBF": "Bramble",
    "CH": "Chester",
    "GA": "Gart",
    "Ga": "Gart",
    "GW": "Gwendolyn",
    "OG": "Graham",
    "Old Graham": "Graham",
    "GG": "Graham",
    "NarGlassSlippers": "Graham",
    "KG": "Graham",
    "Graham": "Graham",
    "P11": "Graham",
    "P12": "Graham",
    "P21": "Graham",
    "P22": "Graham",
    "P31": "Graham",
    "P41": "Graham",
    "P42": "Graham",
    "GrahamAddendumRepeat": "Graham",
    "KB": "Graham",
    "Hi": "Graham",
    "Low": "Graham",
    "Med": "Graham",
    "AKCreedChoiceA3YG": "Graham",
    "Pre": "Graham",
    "SirVerArrows-YG": "Graham",
    "YB": "Graham",
    "YG": "Graham",
    "EscRoomNotGood": "Graham",
    "EscRoomOneTry": "Graham",
    "OldGraham": "Graham",
    "KY": "Kyle",
    "Ky": "Kyle",
    "MM": "Merchant",
    "MO": "Mordon",
    "MH": "Muriel",
    "HobIdleLowF01": "Muriel",
    "OL": "Olfie",
    "RG1": "Royal Guard 1",
    "RG2": "Royal Guard 2",
    "RG3": "Royal Guard 3",
    "RG": "Royal Guard 1",
    "RoyalKnight": "Royal Knight",
    "WF": "Wente",
    "OF": "Wente",
    "WH": "Whisper",
    "I": "Whisper",
    "J": "Whisper",
    "K": "Whisper",
    "HG": "Hagatha",
    "NS": "Neese",
    "VA": "Valanice",
    "VE": "Vee",
    "LA": "Larry",
    "AL": "Alexander",
    "Puz3Spikes03": "Alexander",
    "DA": "Alexander",
    "IC": "Icebella",
    "IG": "Ice Guard",
    "MA": "Manannan",
    "Manny": "Manannan",
    "MR": "Rosella",
    "SP": "Sphinx",
    "TA": "Taskia",
    "ALT": "Taskia",
    "RO": "Rosella",
    "PI": "Pillare",
    "WA": "Waddles",
    "WaddlesPiece": "Waddles",
    "AgendaEnd": "Waddles",
    "E1P2": "Olfie"
  }
}
```

### 角色列表（共35个）

- "Graham" :4036,
- "Gwendolyn" :787,
- "Amaya" :502,
- "Alexander" :437,
- "Acorn" :419,
- "Manannan" :405,
- "Vee" :401,
- "Neese" :380,
- "Whisper" :379,
- "Muriel" :373,
- "Valanice" :353,
- "Chester" :348,
- "Wente" :296,
- "Royal Guard 1" :281,
- "Rosella" :239,
- "Bramble" :232,
- "Merchant" :210,
- "Royal Guard 2" :207,
- "Olfie" :191,
- "Pillare" :182,
- "Hagatha" :134,
- "Sphinx" :117,
- "Gart" :100,
- "Waddles" :99,
- "Mordon" :82,
- "Larry" :78,
- "Kyle" :64,
- "Royal Guard 3" :54,
- "LOCATION" :49,
- "Achaka" :48,
- "Icebella" :27,
- "Taskia" :26,
- "Royal Knight" :8,
- "ACTION" :6,
- "EscRoomPullSwitch08" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuestChapters/,False,King's Quest Chapters,King's Quest,TOTAL,11496,113053,29097,134734,-0.011728250324230416,102.06697562074164,6.185570795326046,33
../data/KingsQuest/KingsQuestChapters/,False,King's Quest Chapters,King's Quest,male,7323,73568,18767,88379,0.11445081565948456,101.22412068198084,6.231587372341349,18
../data/KingsQuest/KingsQuestChapters/,False,King's Quest Chapters,King's Quest,female,4172,39472,10327,46335,-0.24766968577063864,103.64604397952264,6.099854596266731,14
../data/KingsQuest/KingsQuestChapters/,False,King's Quest Chapters,King's Quest,neutral,1,13,2,20,5.098846153846157,70.08365384615385,6.388130769230769,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time

chapters = [
		"https://kingsquest.fandom.com/wiki/KQC1_transcript",
		"https://kingsquest.fandom.com/wiki/KQC2_transcript",
		"https://kingsquest.fandom.com/wiki/KQC3_transcript",
		"https://kingsquest.fandom.com/wiki/KQC4_transcript",
		"https://kingsquest.fandom.com/wiki/KQC5_transcript",
		"https://kingsquest.fandom.com/wiki/KQC6_transcript"]
		
i = 1
for chapter in chapters:
	html = urlopen(chapter).read().decode('utf-8')
	o = open("raw/page0" + str(i) + ".html",'w')
	i += 1
	o.write(html)
	o.close()
	time.sleep(3)
```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
