# 国王密使 · KingsQuest7（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest7》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest7
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest VII: The Princeless Bride",
  "series": "King's Quest",
  "year": 1994,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ7_transcript",
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
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "n/a"
  },
  "notes": "Character info from http://sierrachest.com/index.php?a=games&id=7&title=kings-quest-7&fld=walkthrough&pid=120",
  "parserParameters": {
    "parser": "KQ7Parser",
    "startText": "class=\"mw-headline\" id=\"20.msg",
    "endText": "printfooter"
  },
  "mainPlayerCharacters": [
    "Rosella",
    "Valanice"
  ],
  "characterGroups": {
    "male": [
      "Kangaroo rat",
      "King Otar",
      "Edgar as King Otar",
      "Colin Farwalker",
      "Brutus Bonecrusher",
      "Feldspar the rock spirit",
      "Arresting badger guard",
      "Badger guard",
      "Black Valiant",
      "Weaver of Dreams",
      "Cuddles",
      "Blotar",
      "Hogarth",
      "Troll Cook",
      "Rude Forging Troll",
      "Oppi Goldworth",
      "Attis",
      "Obnoxious gate guard",
      "Arch-Duke YipYap",
      "Arresting badger guard",
      "Badger guard",
      "Mockingbird",
      "Snake Oil Salesman",
      "Fernando Bullforth",
      "Ersatz de Faux",
      "Gravedigger",
      "Dr. Mort Cadaver",
      "GHOUL KID 1",
      "Mr. Bugbear",
      "Mr. Nibbler",
      "King Otar",
      "Bogeyman",
      "GHOUL KID 2",
      "Three-headed plant 1",
      "Three-headed plant 2",
      "Three-headed plant 3",
      "Badgers of the jury",
      "Count Tsepish",
      "Borasco",
      "Levanter",
      "Oberon",
      "Prince Edgar",
      "King Graham",
      "King Otar"
    ],
    "female": [
      "Rosella",
      "Valanice",
      "Mathilde",
      "Spike",
      "Spike's mother",
      "Malicia",
      "Crystal Dragon",
      "Magic Statuette",
      "Gharbi",
      "Egglentine",
      "Winnie",
      "Chicken Petite",
      "Countess Elspeth Tsepish",
      "Lady Ceres",
      "Lachesis",
      "Clotho",
      "Atropos",
      "Gharbi",
      "Lady Mab",
      "Titania"
    ],
    "neutral": [
      "Hummingbird",
      "Spider",
      "Shrunken heads",
      "Jackalope",
      "Dragon toad",
      "Treasure the China Bird",
      "Black cat"
    ],
    "not coded": [
      "56 ????",
      "57 ????",
      "99 ???"
    ]
  },
  "aliases": {
    "1": "Valanice",
    "2": "Rosella",
    "3": "Jackalope",
    "4": "Kangaroo rat",
    "5": "Colin Farwalker",
    "6": "Edgar as King Otar",
    "7": "Rosella",
    "8": "Mathilde",
    "9": "Spike",
    "10": "Spike's mother",
    "12": "Malicia",
    "13": "Cuddles",
    "14": "Blotar",
    "15": "Hogarth",
    "16": "Egglentine",
    "17": "Winnie",
    "18": "Dragon toad",
    "19": "Troll Cook",
    "20": "Rude Forging Troll",
    "21": "Oppi Goldworth",
    "22": "Brutus Bonecrusher",
    "23": "Crystal Dragon",
    "24": "Hummingbird",
    "25": "Attis",
    "26": "Spider",
    "27": "Feldspar the rock spirit",
    "28": "Obnoxious gate guard",
    "29": "Arch-Duke YipYap",
    "30": "Chicken Petite",
    "31": "Arresting badger guard",
    "32": "Badger guard",
    "33": "Mockingbird",
    "34": "Snake Oil Salesman",
    "35": "Treasure the China Bird",
    "36": "Fernando Bullforth",
    "37": "Ersatz de Faux",
    "38": "Magic Statuette",
    "39": "Gravedigger",
    "40": "Dr. Mort Cadaver",
    "41": "GHOUL KID 1",
    "42": "Mr. Bugbear",
    "43": "Mr. Nibbler",
    "44": "King Otar",
    "45": "Bogeyman",
    "46": "Countess Elspeth Tsepish",
    "47": [
      "GHOUL KID 1",
      "GHOUL KID 2"
    ],
    "48": "GHOUL KID 2",
    "49": "Black cat",
    "50": "Shrunken heads",
    "51": "Three-headed plant 1",
    "52": "Three-headed plant 2",
    "53": "Three-headed plant 3",
    "54": "Badgers of the jury",
    "55": "Lady Ceres",
    "56": "56 ????",
    "57": "57 ????",
    "58": "Black Valiant",
    "59": "Count Tsepish",
    "60": "Lachesis",
    "61": "Clotho",
    "62": "Atropos",
    "63": "Weaver of Dreams",
    "64": "Gharbi",
    "65": "Borasco",
    "66": "Levanter",
    "67": "Titania",
    "68": "Oberon",
    "69": "Lady Mab",
    "70": "Prince Edgar",
    "71": "King Graham",
    "99": {
      "Rosella": [
        "A troll?! EEEEEEEE!",
        "Did it work?",
        "Eeeow",
        "Yech.",
        "Eeow.",
        "Oh, that's odd",
        "Oh no! She can't!",
        "Hmm?",
        "BRIDE?!",
        "AAAAAAAAAA",
        "I'm a",
        "A troll?!",
        "Yech!",
        "I already have some of those",
        "I already have a brass bowl",
        "They could cook a",
        "I'm not letting HIM out",
        "Bleh",
        "I 
```

### 角色列表（共70个）

- "ACTION" :785,
- "Valanice" :457,
- "Rosella" :349,
- "Kangaroo rat" :70,
- "Dr. Mort Cadaver" :62,
- "Mockingbird" :54,
- "Attis" :46,
- "King Otar" :43,
- "Ersatz de Faux" :41,
- "Malicia" :40,
- "GHOUL KID 1" :39,
- "Mathilde" :39,
- "Obnoxious gate guard" :36,
- "Fernando Bullforth" :36,
- "GHOUL KID 2" :31,
- "Snake Oil Salesman" :29,
- "Arch-Duke YipYap" :24,
- "Three-headed plant 1" :23,
- "Gravedigger" :20,
- "Colin Farwalker" :18,
- "Chicken Petite" :17,
- "Lachesis" :14,
- "Three-headed plant 3" :14,
- "Three-headed plant 2" :14,
- "Troll Cook" :14,
- "Rude Forging Troll" :14,
- "Arresting badger guard" :12,
- "Feldspar the rock spirit" :12,
- "Edgar as King Otar" :12,
- "Lady Ceres" :10,
- "Crystal Dragon" :10,
- "Oppi Goldworth" :10,
- "Black cat" :9,
- "Titania" :9,
- "Jackalope" :9,
- "Oberon" :8,
- "Weaver of Dreams" :7,
- "Black Valiant" :7,
- "Hummingbird" :7,
- "Blotar" :7,
- "Prince Edgar" :7,
- "99 ???" :7,
- "Count Tsepish" :6,
- "Spider" :6,
- "Hogarth" :6,
- "Cuddles" :6,
- "Treasure the China Bird" :5,
- "Badgers of the jury" :5,
- "Bogeyman" :5,
- "Brutus Bonecrusher" :5,
- ... 共70个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest7/,False,King's Quest VII: The Princeless Bride,King's Quest,TOTAL,1782,21358,4723,24878,-0.08161956945147786,103.70216379928617,6.446134548285335,69
../data/KingsQuest/KingsQuest7/,False,King's Quest VII: The Princeless Bride,King's Quest,male,758,10651,2174,12432,0.09384225511648303,103.11591333253064,6.650277132138449,40
../data/KingsQuest/KingsQuest7/,False,King's Quest VII: The Princeless Bride,King's Quest,female,974,10296,2440,11960,-0.23725716178175027,104.279305514158,6.216749506158686,19
../data/KingsQuest/KingsQuest7/,False,King's Quest VII: The Princeless Bride,King's Quest,neutral,39,393,96,459,-0.2117581106870201,103.87221016221375,6.69219631043257,7
../data/KingsQuest/KingsQuest7/,False,King's Quest VII: The Princeless Bride,King's Quest,not coded,11,18,13,27,2.650000000000002,78.52961538461541,13.354621367521368,3

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ7_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
