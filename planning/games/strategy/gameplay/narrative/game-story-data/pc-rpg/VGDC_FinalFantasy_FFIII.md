# 最终幻想 · FFIII（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFIII》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFIII
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy III",
  "series": "Final Fantasy",
  "year": 1990,
  "status": "in progress",
  "source": "https://www.romhacking.net/utilities/1226/",
  "alternativeMeasure": true,
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "complete",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "notes": "This is a fan tralsation of the NES, derived from a patch. We're currently excluding it from the main analysis.",
  "parserParameters": {
    "parser": "FF3TranslationParser",
    "fileType": ".txt"
  },
  "mainPlayerCharacters": [
    "Luneth",
    "Arc",
    "Refia",
    "Ingus"
  ],
  "characterGroups": {
    "male": [
      "Luneth",
      "Arc",
      "Ingus",
      "Cid",
      "Desch",
      "Alus",
      "Djinn",
      "Doga",
      "Gigameth",
      "Gill",
      "Goldor",
      "Hein",
      "King Gorn",
      "King Sasune",
      "King Argus",
      "Man",
      "Odin",
      "Pops",
      "Shelco",
      "Takka",
      "Topapa",
      "Xande"
    ],
    "female": [
      "Refia",
      "Sara",
      "Aria",
      "Cloud",
      "Delilah",
      "Kate",
      "Mrs.Cid",
      "Nina",
      "Salina",
      "Salina's mom",
      "Unei"
    ],
    "neutral": [
      "Elder Tree",
      "Giant Rat",
      "Leviathan"
    ]
  },
  "aliases": {
    "???": {
      "Desch": [
        "Didn't expect to see",
        "Huh? Oh. I'm Desch."
      ]
    },
    "of the four orphans": "Nina",
    "Gigameth,the king's aide": "Gigameth",
    "King Alus": "Alus",
    "King": {
      "King Gorn": [
        "Die, sweet prince!",
        "Ughn ...",
        "I ... won't be controlled ...",
        "I'd rather die than kill my beloved son! Your plans are foiled!",
        "Alus ... my son! Gigameth had me under his spell ...",
        "I thought you'd never forgive me for exiling you ... But you came back. That is what gave me the strength to break free ... My son ... Please bring peace back to Saronia. Ungh ...",
        "I love you, Alus ..."
      ],
      "King Sasune": [
        "Princess Sara! You're safe!",
        "I'm worried about your safety ...",
        "I'm King Sasune. The Djinn cursed everyone ... To lift the curse, the Djinn must be resealed.",
        "In the Sealed Cave up north. We need a Mythril Ring to seal him.",
        "Oh! A Mythril Ring from Kazus was made for her! But where is she now? Did the Djinn take her? Oh no ...",
        "Such Warriors, you are! There's a secret path in the Sealed Cave. Find the skeleton key. Seal the Djinn, and save us all!",
        "Thank you, warriors. You have sealed the Djinn and rescued Princess Sara."
      ],
      "King Argus": [
        "I am King Argus, ruler of the lands north of the desert ... But now it's an empty kingdom. Hein has cursed my soldiers. I trusted Hein ... Cough ...",
        "I'm fine. Please, you must defeat Hein!",
        "Thank you, Warriors. Take this. It's the Argus family heirloom, the Time Wheel, a box created by the Ancients. Bring it to Cid in Canaan. You know him? That's great!",
        "Off to Canaan! Bring the Time Wheel to Cid!",
        "Cid built that airship? Now you can go anywhere, even off the continent!"
      ]
    }
  }
}
```

### 角色列表（共66个）

- "NPC" :484,
- "Luneth" :115,
- "ACTION" :53,
- "Desch" :44,
- "Unei" :34,
- "Doga" :31,
- "Sara" :30,
- "Alus" :27,
- "Cid" :27,
- "Aria" :25,
- "Arc" :19,
- "Old man" :13,
- "Refia" :12,
- "Ingus" :9,
- "Gill" :8,
- "King Sasune" :7,
- "Salina" :7,
- "King Gorn" :7,
- "Guard" :7,
- "Old men" :7,
- "Elder Tree" :6,
- "???" :6,
- "King Argus" :5,
- "Topapa" :5,
- "Cloud" :5,
- "Delilah" :5,
- "Girl" :5,
- "Parrot" :4,
- "Gigameth" :4,
- "Shelco" :4,
- "Thug" :4,
- "Takka" :3,
- "Nina" :3,
- "Soldier" :3,
- "Goldor" :3,
- "Servant" :2,
- "Old man 1" :2,
- "Man" :2,
- "Pops" :2,
- "Mrs.Cid" :2,
- "Xande" :2,
- "Others" :2,
- "Dark Warriors" :2,
- "Odin" :2,
- "The Legendary Excalibur" :1,
- "The Mystic Masamune" :1,
- "The Moonring of Darkness" :1,
- "The mirror spoke" :1,
- "Magic Knight" :1,
- "Everyone" :1,
- ... 共66个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFIII/,True,Final Fantasy III,Final Fantasy,TOTAL,1018,9801,3038,11546,-0.43089903933570994,103.89802974233326,6.793088104920572,65
../data/FinalFantasy/FFIII/,True,Final Fantasy III,Final Fantasy,male,328,2554,1004,2966,-0.8943844824304978,106.00571957276611,6.724071512540285,22
../data/FinalFantasy/FFIII/,True,Final Fantasy III,Final Fantasy,female,125,1100,418,1263,-1.0151387559808587,107.02776555023924,6.695353588516746,11
../data/FinalFantasy/FFIII/,True,Final Fantasy III,Final Fantasy,neutral,8,101,37,115,-1.0897618410489684,107.73759165105702,6.11694409954509,3

```


### 数据来源脚本 (scraper.py)

```python
#from urllib.request import *

page = "https://www.romhacking.net/download/utilities/1226/"
tmpFile = 'raw/OnionText.zip'

print("""
Final Fantasy III source:
(data/FinalFantasy/FFIII/)

Download Onion Text from this site: https://www.romhacking.net/utilities/1226/
Unzip the file, then from the folder "English FFIII Script (2019 Translation)",
Copy the files data_bank1.txt to data_bank4.txt into the 'raw' folder.
""")

input("Press Enter to continue...")
```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
