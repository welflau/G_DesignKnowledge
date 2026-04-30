# 国王密使 · KingsQuest3（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest3》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest3
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest III: To Heir Is Human",
  "series": "King's Quest",
  "year": 1986,
  "status": "ready",
  "source": "https://kingsquest.fandom.com/wiki/KQ3_transcript",
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
    "truePositive_notes": "Previous errors fixed.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "Previous errors fixed."
  },
  "parserParameters": {
    "parser": "KQ3Parser",
    "startText": "<span class=\"mw-headline\" id=\"Logic.000\">Logic.000</span>",
    "endText": "class=\"mw-headline\" id=\"Words.tok\">Words.tok",
    "splitString": "(\\\\\".+?\\\\\")",
    "quoteRecogniser": "\\\"",
    "characterCues": {
      "shopkeeper": "Storekeeper",
      "storekeeper": "Storekeeper",
      "store": "Storekeeper",
      "wizard": "Manannan",
      "Manannan": "Manannan",
      "Papa": "Papa Bear",
      "Mama": "Mama Bear",
      "fish": "Fish",
      "hens": "Hen",
      "hen": "Hen",
      "chickens": "Hen",
      "Oracle": "Oracle",
      "seamen": "Sailor",
      "sailors": "Sailor",
      "sailor": "Sailor",
      "ship": "Sailor",
      "salt": "Sailor",
      "surly-looking": "Sailor",
      "growls": "Mama Bear",
      "captain": "Captain",
      "Captain": "Captain",
      "pirate": "Pirate",
      "pirates": "Pirate",
      "mate": "First Mate",
      "rogues": "Sailor",
      "bandits": "Bandit",
      "barmaid": "Barmaid",
      "tosses": "Barmaid",
      "gnome": "Gnome",
      "Rosella": "Rosella",
      "Valanice": "Valanice",
      "mother": "Valanice",
      "Graham": "Graham",
      "flings": "Graham",
      "mouse": "Mouse",
      "mice": "Mouse",
      "bird": "Bird",
      "friend": "Bird",
      "squirrel": "Squirrel",
      "lizards": "Lizard",
      "lizard": "Lizard",
      "sister": "Rosella",
      "You": "Gwydion",
      "you": "Gwydion"
    },
    "skipLines": [
      "Ancient Arabic Mythology,",
      "A Study of the Heavens,",
      "The Philosophies of Socrates.",
      "King's Quest IV,",
      "King's Quest III.",
      "your own.",
      "No pain, no magic.",
      "wizard's",
      "Powdered Fish Bone,",
      "Nightshade Juice,",
      "Nightshade Juice",
      "Mandrake Root Powder,",
      "Saffron,",
      "Toad Spittle,",
      "Toad Spittle",
      "Toadstool Powder",
      "Toadstool Powder.",
      "Saffron",
      "missing.",
      "Ration",
      "King's Quest III!!",
      "King's Quest IV!",
      "do chore.",
      "Powdered Fish Bone",
      "Mandrake Root Powder",
      "Hi.",
      "You're welcome."
    ]
  },
  "mainPlayerCharacters": [
    "Gwydion"
  ],
  "characterGroups": {
    "male": [
      "Bandit",
      "Captain",
      "First Mate",
      "Gnome",
      "Graham",
      "Gwydion",
      "Manannan",
      "Papa Bear",
      "Pirate",
      "Sailor",
      "Storekeeper"
    ],
    "neutral": [
      "Oracle",
      "Fish 1",
      "Fish 2",
      "Cat",
      "Bird 1",
      "Bird 2",
      "Squirrel 1",
      "Squirrel 2",
      "Mouse 1",
      "Mouse 2",
      "Unknown",
      "Lizard 1",
      "Lizard 2"
    ],
    "female": [
      "Valanice",
      "Rosella",
      "Barmaid",
      "Hen",
      "Mama Bear"
    ]
  },
  "aliases": {
    "Unknown": {
      "Mama Bear": [
        "AND STAY OUT!!!"
      ],
      "Fish 1": [
        "My, that was a tasty little bug."
      ],
      "Oracle": [
        "Years ago, a terrible",
        "Sadly, your own sister",
        "Behold the",
        "You, Gwydion",
        "are the only one"
      ],
      "Captain": [
        "Ya little cheat!"
      ],
      "Barmaid": [
        "I'll be happy to take yer order"
      ],
      "Pirate": [
        "Arrr!",
        "What d'ya think yer",
        "I gotcha, boy"
      ],
      "Sailor": [
        "You'd bet'er get aboard boy, or we'll sail without ya.",
        "Ya better skedaddle, sonny!",
        "Climb aboard, laddie! We won't be awaiting all day for ye."
      ],
      "Mouse": [
        "What happened to the last",
        "Didn't you hear?"
      ],
      "Cat": [
        "Screeeeeeeeee",
        "Get lost, Gwydion",
        "Ha, ha! Missed me",
        "HEY! That hu",
        "Ow! I'll get you for t",
        "Wait till I catch yo",
        "The next scratch is gonna be"
      ],
      "Manannan": [
        "Out of my way, Gwydion",
        "I mean it, boy.",
        "Gwydion, let this be a lesson to",
        "Attempt to use magic around me, ",
        "Shoo, boy! I don't want to",
        "our kitchen is filthy! ",
        "Gwydion, my chamber pot needs servicing.",
        "My office is dusty.",
        "You've been neglecting my chickens again",
        "When I assign a chore",
        "Go find something to do.",
        "Instead of fooling ar
```

### 角色列表（共30个）

- "SYSTEM" :1433,
- "Manannan" :66,
- "Gwydion" :39,
- "Storekeeper" :29,
- "Barmaid" :17,
- "Captain" :15,
- "Rosella" :14,
- "Hen" :14,
- "Mouse 1" :12,
- "Sailor" :10,
- "Squirrel 1" :9,
- "Mouse 2" :9,
- "Lizard 1" :8,
- "Squirrel 2" :8,
- "Bird 1" :8,
- "Unknown" :8,
- "Bird 2" :7,
- "Gnome" :7,
- "Fish 2" :7,
- "Fish 1" :7,
- "Lizard 2" :6,
- "Oracle" :6,
- "Mama Bear" :6,
- "Cat" :3,
- "Graham" :3,
- "Valanice" :3,
- "Pirate" :3,
- "Papa Bear" :3,
- "Bandit" :2,
- "First Mate" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest3/,False,King's Quest III: To Heir Is Human,King's Quest,TOTAL,330,3151,528,3631,0.33496777718473325,103.29034257102123,6.568345619957109,29
../data/KingsQuest/KingsQuest3/,False,King's Quest III: To Heir Is Human,King's Quest,male,178,1645,296,1880,0.06311293436293575,104.50849179536682,6.887771748952599,11
../data/KingsQuest/KingsQuest3/,False,King's Quest III: To Heir Is Human,King's Quest,neutral,98,988,147,1160,0.8854755019416682,100.6851600154232,6.031515783965408,13
../data/KingsQuest/KingsQuest3/,False,King's Quest III: To Heir Is Human,King's Quest,female,54,518,85,591,0.24964024528730455,104.1270767658415,6.590756652282534,5

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ3_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
