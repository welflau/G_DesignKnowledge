# 最终幻想 · FFX2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFX2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFX2
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy X-2",
  "series": "Final Fantasy",
  "year": 2003,
  "status": "ready",
  "source": "https://www.ffcompendium.com/h/faqs/ffx2scriptaschthehated.txt",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "Previous error has been addressed.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "FF10_2Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Yuna",
    "Paine",
    "Rikku"
  ],
  "characterGroups": {
    "male": [
      "Ayde",
      "Auron",
      "Barthello",
      "Bayra",
      "Botta",
      "Baralai",
      "Braska",
      "Brother",
      "Beclem",
      "Benzo",
      "Buddy",
      "Borra",
      "Cid",
      "Clasko",
      "Chappu",
      "Datto",
      "Daraya",
      "Donga",
      "Garik",
      "Gippal",
      "Isaaru",
      "Jassu",
      "Jecht",
      "Keepa",
      "Lian",
      "Logos",
      "Ormi",
      "Kimahri",
      "Kinoc",
      "Maroda",
      "Maechen",
      "Maroda",
      "Nooj",
      "O'aka",
      "Pacce",
      "Rin",
      "Shinra",
      "Shuyin",
      "Tromell",
      "Taro",
      "Tidus",
      "Tobli",
      "Wakka",
      "Wantz",
      "Yaibal",
      "Male Al Bhed 1",
      "Male Al Bhed 2",
      "Man",
      "Man 1",
      "Man 2",
      "Man 3",
      "Man 4",
      "Man with Two Guns",
      "Boy",
      "Bulky Man",
      "Fayth",
      "Hypello",
      "Guado",
      "Elderly Guado",
      "Al Bhed 1",
      "Al Bhed 2",
      "Al Bhed (male voice)",
      "Al Bhed (wounded)",
      "Al Bhed (outside temple)",
      "Al Bhed running The Experiment",
      "Al Bhed (Thunder Plains)",
      "Al Bhed (Hovercraft)",
      "Balloon Vendor",
      "Barkeep",
      "Citizen",
      "Vuroja",
      "Prophet",
      "Goon",
      "Goon 1",
      "Goon 2",
      "Guard",
      "Guard 1",
      "Guard 2",
      "Kid",
      "Pilot",
      "Temple Priest",
      "Youth League Member 1",
      "Youth League Member 2",
      "Youth League Member 3",
      "New Yevon Member 1 at concert",
      "New Yevon Member 2 at concert",
      "Youth League Member 2 at concert",
      "Yaibal's Youth League Member 1",
      "Elma's Youth League Member 1",
      "Elma's Youth League Member 2"
    ],
    "female": [
      "Calli",
      "Dona",
      "Elma",
      "Hana",
      "Lucil",
      "Lulu",
      "Lenne",
      "Rikku",
      "Shelinda",
      "Nhadala",
      "Paine",
      "Yuna",
      "Darling",
      "Leblanc",
      "Fem-Goon 1",
      "Fem-Goon 2",
      "Female Al Bhed",
      "Female Ronso",
      "Old Woman",
      "Woman",
      "Girl",
      "Pukara",
      "Pukutak",
      "Clerk",
      "Youth League Member 1 at concert",
      "Yaibal's Youth League Member 2"
    ],
    "genderless": [
      "Picket"
    ],
    "neutral": [
      "Youth League Member"
    ]
  },
  "aliases": {
    "Lian & Ayde": [
      "Lian",
      "Ayde"
    ],
    "Logos & Ormi": [
      "Logos",
      "Ormi"
    ],
    "Ormi & Logos": [
      "Logos",
      "Ormi"
    ],
    "Paine & Yuna": [
      "Paine",
      "Yuna"
    ],
    "Rikku & Paine": [
      "Rikku",
      "Paine"
    ],
    "Yuna & Rikku": [
      "Yuna",
      "Rikku"
    ],
    "Yuna, Rikku, And Paine": [
      "Yuna",
      "Rikku",
      "Paine"
    ],
    "Pacce & Hana": [
      "Pacce",
      "Hana"
    ],
    "Rikku, Lian & Ayde": [
      "Rikku",
      "Lian",
      "Ayde"
    ],
    "Taro & Hana": [
      "Taro",
      "Hana"
    ],
    "The Kinderguardians": [
      "Pacce",
      "Taro",
      "Hana"
    ],
    "All the Gullwings": [
      "Buddy",
      "Brother",
      "Rikku",
      "Paine",
      "Shinra"
    ],
    "Brother, Buddy & Shinra": [
      "Buddy",
      "Brother",
      "Shinra"
    ],
    "Yuna, Rikku and Paine": [
      "Yuna",
      "Rikku",
      "Paine"
    ],
    "Yuna, Rikku, and Paine": [
      "Yuna",
      "Rikku",
      "Paine"
    ],
    "Voice of Auron": "Auron",
    "Voice of Jecht": "Jecht",
    "Voice of Braska": "Braska",
    "Voice of Fayth": "Fayth",
    "Ex-Prophet": "Prophet",
    "Man's Voice": "Kinoc",
    "Guado": {
      "Elderly Guado": [
        "My, I certainly have a lot of visitors today, don't I?",
        "Oh, dear. I don't think I was supposed to say that.",
        "I was supposed to say, \"Don't walk over there!\""
      ]
    },
    "Al Bhed": {
      "Al Bhed (male voice)": [
        "Gippal!"
      ],
      "Al Bhed 2": [
        "Dra vunafusyh ec fyedehk ujan drana. (The forewoman is waiting over there.)"
      ],
      "Al Bhed 1": [
        "Cra'c pylg! (She's back!)"
      ],
      "Al Bhed (wounded)": [
        "(dying) Fryd fyc ed? Dryd rika cryba, taab 
```

### 角色列表（共119个）

- "ACTION" :1047,
- "Yuna" :771,
- "Rikku" :502,
- "Paine" :360,
- "Brother" :120,
- "Buddy" :83,
- "Rin" :77,
- "Leblanc" :74,
- "Wakka" :64,
- "Gippal" :63,
- "Shinra" :63,
- "Nooj" :60,
- "Logos" :43,
- "Lucil" :40,
- "Dona" :39,
- "Baralai" :39,
- "Tobli" :37,
- "Ormi" :34,
- "Kimahri" :31,
- "Isaaru" :30,
- "Beclem" :28,
- "Lulu" :27,
- "Shuyin" :25,
- "Elma" :25,
- "Garik" :24,
- "Nhadala" :24,
- "Yaibal" :24,
- "Clasko" :23,
- "Benzo" :21,
- "Cid" :20,
- "O'aka" :20,
- "Maroda" :20,
- "Hypello" :19,
- "Shelinda" :18,
- "CHOICE" :17,
- "Maechen" :16,
- "Barthello" :15,
- "Guard" :13,
- "Pacce" :13,
- "Tromell" :13,
- "Calli" :12,
- "Man 1" :12,
- "Barkeep" :12,
- "Tidus" :11,
- "Man" :10,
- "Fayth" :9,
- "Wantz" :9,
- "Goon" :9,
- "Lian" :8,
- "Bayra" :8,
- ... 共119个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFX2/,False,Final Fantasy X-2,Final Fantasy,TOTAL,3199,31635,8234,37527,-0.09387832004434493,102.57867359378992,6.77442987185823,117
../data/FinalFantasy/FFX2/,False,Final Fantasy X-2,Final Fantasy,male,1258,16315,3716,19587,0.28879406197352075,100.81200055825387,7.097435742003419,89
../data/FinalFantasy/FFX2/,False,Final Fantasy X-2,Final Fantasy,female,1936,15294,4506,17909,-0.448696356560113,104.32486239088043,6.423094464222499,26
../data/FinalFantasy/FFX2/,False,Final Fantasy X-2,Final Fantasy,genderless,4,25,10,29,-0.9269999999999996,106.16150000000003,15.129299999999999,1
../data/FinalFantasy/FFX2/,False,Final Fantasy X-2,Final Fantasy,neutral,1,1,1,2,8.400000000000002,36.62000000000003,0.0496,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re


html = urlopen("https://www.ffcompendium.com/h/faqs/ffx2scriptaschthehated.txt").read().decode("utf-8", "backslashreplace")

o = open("raw/page001.html",'w')
o.write(html)
o.close()




```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
