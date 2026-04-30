# 最终幻想 · FFIV_DS（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFIV_DS》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFIV_DS
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy IV",
  "series": "Final Fantasy",
  "year": 1991,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/ds/939425-final-fantasy-iv/faqs/53978",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "Plot dialogue included but optional chat with background NPCs missing from source",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "notes": "The script here is for the DS version from 2007.",
  "parserParameters": {
    "parser": "FF4Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Cecil",
    "Kain",
    "Rosa",
    "Rydia",
    "Tellah",
    "Edward",
    "Yang",
    "Palom",
    "Porom",
    "Cid",
    "Edge",
    "Fusoya"
  ],
  "characterGroups": {
    "male": [
      "Baigan",
      "Cagnazzo",
      "Cecil",
      "Cid",
      "Corio",
      "Edge",
      "Edward",
      "Fusoya",
      "Giott",
      "Golbez/Theodor",
      "Kain",
      "Palom",
      "Rubicante",
      "Rydia",
      "Tellah",
      "Yang",
      "Zemus",
      "Zeromus",
      "Bahamut",
      "Barnabas",
      "Dark Elf",
      "Dr Lugae",
      "King Giott",
      "Elder",
      "Former King",
      "King Of Baron",
      "King Of Eblan",
      "King Of Fabul",
      "Kluya",
      "Rubicante",
      "Scarmiglione",
      "Whyt",
      "Whyt's Father",
      "Kokkol",
      "Monks",
      "Pigmy",
      "Soldier",
      "Soldiers",
      "Leviathan",
      "General",
      "Captain",
      "Sailor",
      "Sailors",
      "Fabul Guard",
      "Fabul Guards",
      "Guards",
      "Dwarf",
      "Dwarves",
      "Goblin",
      "Engineer",
      "Engineers",
      "Ninja",
      "Seneschal",
      "Observer",
      "Innkeeper"
    ],
    "female": [
      "Anna",
      "Asura",
      "Cindy",
      "Luca",
      "Mindy",
      "Porom",
      "Rosa",
      "Sandy",
      "Yang's Wife",
      "Barbariccia",
      "Cecilia",
      "Queen Of Eblan",
      "Troia Maidens",
      "Maid",
      "Midwife",
      "Sylph",
      "Epopt",
      "Nurse"
    ],
    "neutral": [
      "Narration",
      "Calcabrina",
      "Sahagin",
      "Mist Dragon",
      "Townfolk",
      "Crystals",
      "Eidolon",
      "Damcyan Child"
    ]
  },
  "aliases": {
    "Barbariccia's Voice": "Barbariccia",
    "Palom And Porom": [
      "Palom",
      "Porom"
    ],
    "Magus Sisters": [
      "Cindy",
      "Sandy",
      "Mindy"
    ],
    "Female Voice": "Rydia",
    "Edward's Voice": "Edward",
    "Eidolon King": "Leviathan",
    "Kain's Voice": "Kain",
    "Baby": "Cecil",
    "Mysterious Man": "Golbez/Theodor",
    "Seneschal's Voice": "Seneschal",
    "Creature": "Scarmiglione",
    "Zemus's Spirit": "Zeromus",
    "Bard": "Edward",
    "Lugae": "Dr Lugae",
    "Doctor": "Dr Lugae",
    "Mechanics": "Engineers",
    "Dwarf Girl": "Luca",
    "Dwarven King": "King Giott",
    "Golbes": "Golbez/Theodor",
    "Golbez's Voice": "Golbez/Theodor",
    "Dolls": "Calcabrina",
    "Golbez": "Golbez/Theodor",
    "Theodor": "Golbez/Theodor",
    "Theodore": "Golbez/Theodor",
    "Heavy Girl": "Cindy",
    "Small Girl": "Mindy",
    "Tall Girl": "Sandy",
    "King": "King Of Eblan",
    "Queen": "Queen Of Eblan",
    "Mysterious Voice": "Kluya",
    "Monk": "Yang",
    "Yan": "Yang",
    "Girl": {
      "Porom": [
        "Did you need something?",
        "Oh, that brother of mine... !",
        "Your name is Cecil, right? Pleased to meet you."
      ],
      "Rydia": [
        "Mother, you can't die! Just because your dragon did...",
        "!",
        "You - you're the ones who killed her dragon?",
        "No!",
        "Stay away!",
        "Leave me alone! I hate you!!!!!",
        "...",
        "I'm sorry, it's all my fault.",
        "But... you protected me.",
        "My name's Rydia."
      ]
    },
    "Man": {
      "Tellah": [
        "You, knight! You wield the dark sword, do you not? I beg you, lend me your aid!",
        "My daughter Anna was tricked by a silver-tongued bard. He's taken her to Damcyan Castle. I fear I've little time. I sense something sinister."
      ],
      "Fusoya": [
        "I am Fusoya, and I am charged with watching over the slumber of the Lunarians."
      ]
    },
    "Voice": {
      "Scarmiglione": [
        "Such pleasure I will take in delivering"
      ],
      "Kain": [
        "Your Majesty!",
        "I see you have the Crystal.",
        "This way!",
        "So you're Cecil!"
      ],
      "Mist Dragon": [
        "Leave this place.",
        "Return whence you came.",
        "Men of Baron...",
        "Leave at once, and no harm will befall you. I will abide no further trespass.",
        "You mean to ignore my warning?",
      
```

### 角色列表（共83个）

- "ACTION" :418,
- "Cecil" :370,
- "Kain" :137,
- "LOCATION" :133,
- "Rosa" :115,
- "Golbez/Theodor" :97,
- "Rydia" :95,
- "Yang" :93,
- "Cid" :90,
- "Edge" :87,
- "Edward" :80,
- "Tellah" :72,
- "Fusoya" :40,
- "Elder" :37,
- "Porom" :36,
- "King Giott" :33,
- "Palom" :33,
- "Kluya" :19,
- "Cagnazzo" :18,
- "Soldier" :18,
- "Cecilia" :16,
- "Baigan" :15,
- "Rubicante" :13,
- "Dr Lugae" :12,
- "Seneschal" :11,
- "King Of Fabul" :10,
- "Yang's Wife" :9,
- "King Of Baron" :8,
- "Barbariccia" :8,
- "Scarmiglione" :8,
- "Zemus" :7,
- "Luca" :7,
- "Dark Elf" :7,
- "Anna" :7,
- "Mist Dragon" :6,
- "Narration" :6,
- "Zeromus" :5,
- "Asura" :5,
- "Queen Of Eblan" :5,
- "King Of Eblan" :5,
- "Dwarf" :5,
- "Mindy" :5,
- "Cindy" :5,
- "Sandy" :5,
- "Townfolk" :4,
- "Leviathan" :4,
- "Goblin" :4,
- "Barnabas" :4,
- "Kokkol" :3,
- "Whyt" :3,
- ... 共83个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFIV_DS/,False,Final Fantasy IV,Final Fantasy,TOTAL,1737,17822,4745,20876,-0.3031154629571251,103.92554624758426,6.311523276974185,80
../data/FinalFantasy/FFIV_DS/,False,Final Fantasy IV,Final Fantasy,male,1480,15683,4082,18352,-0.2834497474038784,103.93779119385569,6.264580359678807,54
../data/FinalFantasy/FFIV_DS/,False,Final Fantasy IV,Final Fantasy,female,233,1864,594,2187,-0.5214191268912298,104.39011820638433,6.562173962081473,18
../data/FinalFantasy/FFIV_DS/,False,Final Fantasy IV,Final Fantasy,neutral,24,275,68,337,0.4475695187165787,99.05676604278078,7.339597326203208,8

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/ds/939425-final-fantasy-iv/faqs/53978"

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
