# 国王密使 · KingsQuest4（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：国王密使, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
国王密使系列《KingsQuest4》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：国王密使（KingsQuest）
- **游戏**：KingsQuest4
- **品类**：冒险游戏
- **说明**：Sierra经典冒险游戏

### 元数据 (meta.json)

```json
{
  "game": "King's Quest IV: The Perils of Rosella",
  "series": "King's Quest",
  "year": 1988,
  "status": "ready",
  "notes": "The parser may be overly complicated. There are only 200ish lines, they could be manually assigned",
  "source": "https://kingsquest.fandom.com/wiki/KQ4SCI_transcript",
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
    "startText": "<span class=\"mw-headline\" id=\"Text.004\">Text.004</span>",
    "endText": "<span class=\"mw-headline\" id=\"Text.697\">Text.697</span>",
    "characterCues": {
      "bucket": "Dwarf near diamond bucket",
      "softens": "Dwarf near diamond bucket",
      "dwarf": "Dwarf",
      "fisherman": "Fisherman",
      "fisherman's wife": "Fisherman's wife",
      "hen": "Hen",
      "ogress": "Ogress",
      "ogre": "Ogre",
      "prince": "Frog prince",
      "fairy": "Genesta",
      "Lolotte": "Lolotte",
      "Edgar": "Edgar",
      "Rosella": "Rosella",
      "Genesta": "Genesta",
      "minstrel": "Minstrel",
      "tired": "Fisherman",
      "witches": "Witch",
      "witch": "Witch",
      "hags": "Witch",
      "crones": "Witch",
      "you": "Rosella"
    },
    "skipLines": [
      "avoid",
      "get",
      "James",
      "King's Quest II,",
      "Leisure-Suit Larry in the Land of the Lounge Lizards",
      "King's Quest I.",
      "Space Quest!",
      "Space Quest II!",
      "Police Quest!",
      "The Black Cauldron!",
      "King's Quest III!",
      "Mixed-Up Mother Goose!",
      "Leisure Suit Larry Goes Looking For Love (in Several Wrong Places.)",
      "popular ballad.",
      "leaf",
      "accidentally",
      "oldie, but goodie.",
      "Greensleeves.",
      "The Compleat Works of William Shakespeare."
    ]
  },
  "mainPlayerCharacters": [
    "Rosella"
  ],
  "characterGroups": {
    "male": [
      "Dwarf",
      "Dwarf near diamond bucket",
      "Edgar",
      "Fisherman",
      "Frog prince",
      "Graham",
      "Ogre",
      "Minstrel"
    ],
    "neutral": [
      "Raven",
      "Robin",
      "Unknown",
      "Cockatoo",
      "Swamp monster"
    ],
    "female": [
      "Fisherman's wife",
      "Genesta",
      "Hen",
      "Lolotte",
      "Ogress",
      "Rosella",
      "Witch"
    ]
  },
  "aliases": {
    "Fisherman": {
      "Fisherman's wife": [
        "What're you doin",
        "I said GIT",
        "You're a very kind girl",
        "Thank you very much",
        "You have certainly helped us"
      ]
    },
    "Unknown": {
      "Ogress": [
        "JUST A MINUTE! I'M COMIN'!"
      ],
      "Fisherman's wife": [
        "Jest come on in!"
      ],
      "Fisherman": [
        "D'ya know what TIME it is?! GO AWAY!!"
      ],
      "Frog prince": [
        "Ribbit! Ribbit!"
      ],
      "Dwarf": [
        "Go away!",
        "We're all asleep here! Come back tomorrow!",
        "...and STAY OUT!"
      ],
      "Robin": [
        "Cheep, cheep!"
      ],
      "Ogre": [
        "Got ya!"
      ],
      "Swamp monster": [
        "Oh, boy! I sure love frog legs!"
      ],
      "Cockatoo": [
        "Polly want a cracker!"
      ],
      "Rosella": [
        "Phew! I hope that's the last of it!",
        "Oh, my goodness!!",
        "A CHASM!!!",
        "Aaaaahhhhhhh!!",
        "Oh, Father!",
        "You're still young; you should have many years ahead of you! Oh, I wish I could help you, Father!",
        "Aaaaahhhhhhh!!",
        "Polly want a cracker?"
      ],
      "Graham": [
        "Help me,",
        "Never felt better in my life",
        "What is IN this fruit"
      ],
      "Raven": [
        "Caw, caw!",
        "Caw! Caw!"
      ],
      "Edgar": [
        "Rosella,",
        "I love you. Will"
      ]
    },
    "Rosella": {
      "Lolotte": [
        "I don't know how",
        "Bring me the hen",
        "If you do just ONE MORE",
        "I want to have Pandora's Box",
        "Take her away",
        "My son, Edgar,",
        "You'll be married first",
        "You will sleep in Edgar's",
        "Rosella. What a pretty name",
        "Let us relieve you of your burdensome"
      ],
      "Frog prince": [
        "Well, ta, ta,",
        "I'm off. Here, you may keep THIS!"
      ],
      "Edgar": [
        "You may now walk freely about the castle. I..."
      ],
      "Dwarf": [
        "Is Daventry far from Tamir?",
        "How did you get here?"
      ],
      "Graham": [
        "Never felt better in my life!",
        "What is IN this fruit, anyway?"
      ],
      "Minstrel": [
        "Well, well. Who do we have here?",
        "Hello, Rosella,",
        
```

### 角色列表（共21个）

- "SYSTEM" :2186,
- "Genesta" :44,
- "Lolotte" :40,
- "Rosella" :32,
- "Witch" :15,
- "Dwarf" :10,
- "Fisherman's wife" :9,
- "Fisherman" :8,
- "Dwarf near diamond bucket" :7,
- "Ogre" :6,
- "Minstrel" :5,
- "Robin" :5,
- "Frog prince" :5,
- "Graham" :3,
- "Edgar" :3,
- "Ogress" :3,
- "Raven" :2,
- "Swamp monster" :1,
- "Unknown" :1,
- "Hen" :1,
- "Cockatoo" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingsQuest/KingsQuest4/,False,King's Quest IV: The Perils of Rosella,King's Quest,TOTAL,201,1772,343,2033,-0.03715338699168669,104.53049131616531,6.218470556568322,20
../data/KingsQuest/KingsQuest4/,False,King's Quest IV: The Perils of Rosella,King's Quest,male,47,349,73,387,-0.6406656984731303,108.17100443537309,6.633485500647643,8
../data/KingsQuest/KingsQuest4/,False,King's Quest IV: The Perils of Rosella,King's Quest,neutral,10,30,12,31,-2.421666666666665,116.87750000000001,11.6555,5
../data/KingsQuest/KingsQuest4/,False,King's Quest IV: The Perils of Rosella,King's Quest,female,144,1393,258,1615,0.19624325948680266,103.27223118638598,6.0013223687652,7

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://kingsquest.fandom.com/wiki/KQ4SCI_transcript"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
冒险游戏类型的对话叙事参考。Sierra经典冒险游戏
