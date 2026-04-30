# 最终幻想 · FFII（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFII》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFII
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy II",
  "series": "Final Fantasy",
  "year": 1988,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/ps/916670-final-fantasy-ii/faqs/61436",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "complete",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "Previous issues fixed.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "notes": "See README",
  "parserParameters": {
    "parser": "FF2Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Firion",
    "Gus",
    "Maria",
    "Leon"
  ],
  "characterGroups": {
    "male": [
      "Cid",
      "Firion",
      "Gareth",
      "Gordon",
      "Gottos",
      "Gus",
      "Josef",
      "King",
      "Leon",
      "Mindu",
      "Pavel",
      "Scott",
      "Tobul",
      "Boy",
      "Boy by Soldier",
      "Boy by Wizard",
      "Boys",
      "Husband",
      "Husband by Inn",
      "Man",
      "Man by Pub",
      "Man in Armor",
      "Old Man",
      "Borghen",
      "Boy at Northwest",
      "Boy by Flower Patch",
      "Boy by Fountain",
      "Boy by Weapons Shop",
      "Boy near White Magic Shop",
      "Child",
      "Cid's buddy",
      "Emperor",
      "Giant Beaver",
      "Imperial Soldier",
      "Man at Entrance",
      "Man at Northeast",
      "Man at Northwest",
      "Man by Fountain",
      "Master",
      "Pirate",
      "Pirate above Inn",
      "Pirate above Weapon Shop",
      "Pirate above Weapons Shop",
      "Pirate by Forest",
      "Pirate by Fountain",
      "Pirate by House",
      "Pirate by Inn",
      "Pirate by Item Shop",
      "Pirate in Field",
      "Pirate near Weapons Shop",
      "Pirates",
      "Rebel Soldier",
      "Rebel Soldiers",
      "Secret Soldier",
      "Sergeant",
      "Slaves",
      "Soldier",
      "Soldier at Bottom Left Corner",
      "Soldier at Entrance",
      "Soldier at Left",
      "Soldier at Left of Castle Entrance",
      "Soldier at Left of Entrance",
      "Soldier at Left of Stairway",
      "Soldier at Lower Left",
      "Soldier at North Stairway",
      "Soldier at Right",
      "Soldier at Right of Castle Entrance",
      "Soldier at Right of Entrance",
      "Soldier at Right of Stairway",
      "Soldiers at Door",
      "Spy",
      "Townsperson",
      "Villagers and Soldiers",
      "Wandering Mage near Armor Shop",
      "Wandering Rebel Soldier",
      "Wandering Soldier",
      "Wandering Soldier at Left",
      "Wandering Soldier at Right",
      "Wizard"
    ],
    "female": [
      "Elena",
      "Hilda",
      "Leila",
      "Maria",
      "Molly",
      "Girl",
      "Mom",
      "Mother",
      "Wandering Wife",
      "Wife",
      "Woman",
      "Woman 1",
      "Girl 1",
      "Wives by Inn",
      "Girl at Entrance",
      "Girl below Armor Shop",
      "Girl in Josef's House",
      "Various Villagers",
      "Woman by Armor Shop",
      "Woman by Josef's House",
      "Woman by Inn",
      "Woman at Entrance"
    ],
    "neutral": [
      "Mage",
      "Mage at Bottom Left Corner (Higher)",
      "Mage at Bottom Left Corner (Lower)",
      "Mage at Bottom Right Corner (Left)",
      "Mage at Bottom Right Corner (Right)",
      "Mage at Entrance",
      "Mage at Lower Left Corner (Left)",
      "Mage at Lower Left Corner (Right)",
      "Mage at Lower Right Corner (Left)",
      "Mage at Lower Right Corner (Right)",
      "Mage by Water",
      "Mage near Armor Shop",
      "Mage near Inn",
      "Mage near Item Shop",
      "Numerous NPCs",
      "Several NPCs",
      "Tropical Islander",
      "Wind Drake"
    ]
  },
  "aliases": {
    "Woman and Girl": [
      "Woman 1",
      "Girl 1"
    ],
    "Dark Knight": "Leon",
    "Dragoon": "Gareth",
    "Knight": "Scott",
    "Man by Inn": "Woman by Inn",
    "Man at Entrance": {
      "Woman at Entrance": [
        "The men of Salamand have been enslaved to work in the cavern behind the Semitt Falls.",
        "Please help us!"
      ]
    }
  }
}
```

### 角色列表（共123个）

- "ACTION" :208,
- "LOCATION" :142,
- "Hilda" :115,
- "CHOICE" :86,
- "SYSTEM" :79,
- "Gordon" :52,
- "Firion" :44,
- "Soldier" :28,
- "King" :28,
- "Mindu" :28,
- "Man" :24,
- "Wizard" :24,
- "Pavel" :23,
- "Emperor" :21,
- "Maria" :21,
- "Leila" :20,
- "Josef" :19,
- "Girl" :17,
- "Gareth" :16,
- "Leon" :16,
- "Scott" :14,
- "Soldiers at Door" :14,
- "Boy" :13,
- "Cid" :12,
- "Gus" :10,
- "Child" :9,
- "Borghen" :9,
- "Townsperson" :9,
- "Pirate by Item Shop" :9,
- "Cid's buddy" :8,
- "Wandering Soldier" :7,
- "Spy" :7,
- "Tobul" :7,
- "Mom" :6,
- "Molly" :6,
- "Mother" :5,
- "Man in Armor" :5,
- "Wind Drake" :5,
- "Woman" :5,
- "Pirate above Weapons Shop" :5,
- "Pirate by House" :5,
- "Rebel Soldier" :5,
- "Soldier at Right of Entrance" :4,
- "Tropical Islander" :4,
- "Wandering Soldier at Right" :4,
- "Wandering Soldier at Left" :4,
- "Soldier at Right of Stairway" :4,
- "Soldier at Left of Stairway" :4,
- "Master" :4,
- "Soldier at Bottom Left Corner" :3,
- ... 共123个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFII/,False,Final Fantasy II,Final Fantasy,TOTAL,800,8689,2040,10393,0.18523063812934737,101.3208885239733,6.691742856169283,119
../data/FinalFantasy/FFII/,False,Final Fantasy II,Final Fantasy,male,560,5848,1373,7001,0.19762641942564407,101.23196811081012,6.709833100652309,79
../data/FinalFantasy/FFII/,False,Final Fantasy II,Final Fantasy,female,211,2478,577,2959,0.1753808698522743,101.45440356943533,6.6595982639602855,22
../data/FinalFantasy/FFII/,False,Final Fantasy II,Final Fantasy,neutral,29,363,89,433,0.07615625096728174,101.78111895254901,6.6227129693255335,18

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/ps/916670-final-fantasy-ii/faqs/61436"

req = Request(
    page, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

html = urlopen(req).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()



```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
