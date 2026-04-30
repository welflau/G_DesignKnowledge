# 超级马里奥RPG · SuperMarioRPG（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：超级马里奥RPG, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
超级马里奥RPG系列《SuperMarioRPG》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：超级马里奥RPG（SuperMarioRPG）
- **游戏**：SuperMarioRPG
- **品类**：JRPG
- **说明**：任天堂+Square的JRPG

### 元数据 (meta.json)

```json
{
  "game": "Super Mario RPG: Legend of the Seven Stars",
  "series": "Super Mario RPG",
  "year": 1996,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/snes/588739-super-mario-rpg-legend-of-the-seven-stars/faqs/30431",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "notes": "See README",
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "As noted and expected, skippable NPC dialogue isn't all included.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "SuperMarioParser",
    "fileType": ".html",
    "textDivId": "faqtext",
    "startText": "-¯-_-",
    "endText": "CJayC, for creating GameFAQs",
    "playerCharacter": "Mario"
  },
  "mainPlayerCharacters": [
    "Mario",
    "Mallow",
    "Geno",
    "Bowser",
    "Toadstool"
  ],
  "characterGroups": {
    "male": [
      "Apprentice",
      "Axem Black",
      "Axem Green",
      "Axem Red",
      "Axem Yellow",
      "Belome",
      "Boomer",
      "Booster",
      "Bowser",
      "Bowyer",
      "Chancellor",
      "Chef Torte",
      "Cloaker",
      "Croco",
      "Culex",
      "Dodo",
      "Domino",
      "Exor",
      "Frogfucius",
      "Garro",
      "Gaz",
      "Geno",
      "Hammer Brother",
      "Hinopio",
      "Jagger",
      "Jinx",
      "Johnny",
      "King Calamari",
      "King Nimbus",
      "Mack",
      "Mallow",
      "Mario",
      "Mite",
      "Pa'Mole",
      "Punchinello",
      "Raz",
      "Real Elder",
      "Sergeant Flutter",
      "Smithy",
      "Toad",
      "Torte",
      "Yaridovich",
      "Grate Guy",
      "Knife Guy",
      "Gardener",
      "Bus Driver",
      "Repair Man",
      "Manager"
    ],
    "female": [
      "Toadstool",
      "Valentina",
      "Queen Nimbus",
      "Ma'Mole",
      "Mom",
      "Axem Pink",
      "Monstermama",
      "Dyna",
      "Birdo",
      "Raini",
      "Jump Girl"
    ],
    "neutral": [
      "Rat",
      "Miners",
      "Miner 1",
      "Miner 2",
      "Snifits",
      "Snifit 1",
      "Snifit 2",
      "Snifit 3",
      "Vault Guard",
      "Pirates",
      "Shy Away",
      "Retired Guard",
      "Magikoopa",
      "Clerk",
      "Spring Guard",
      "Party",
      "Aero",
      "Retainer",
      "Director",
      "Guard",
      "Guard 1",
      "Guard 2",
      "Townspeople",
      "Troops",
      "Tadpole",
      "Piranha",
      "Pounder 1",
      "Pounder 2",
      "Pounder 3",
      "Shyster",
      "Shyster 1",
      "Shyster 2",
      "Shyster 3",
      "Shyster 4",
      "Shyster 5",
      "Shyster 6",
      "Drill Bit",
      "Factory Chief",
      "Pounder",
      "Countdown",
      "Pirate",
      "Goomba",
      "Flunkies",
      "Everybody",
      "Tadpole y",
      "Tadpole x"
    ]
  },
  "aliases": {
    "Elder": "Real Elder",
    "Toadn": "Toad",
    "Bowser & Booster": [
      "Bowser",
      "Booster"
    ],
    "Snifit 1 & 2": [
      "Snifit 1",
      "Snifit 2"
    ],
    "Knife Guy & Grate Guy": [
      "Knife Guy",
      "Grate Guy"
    ],
    "Raz & Raini": [
      "Raz",
      "Raini"
    ],
    "S. Flutter": "Sergeant Flutter",
    "Shy Away (singing)": "Shy Away",
    "Altogether": [
      "Axem Black",
      "Axem Red",
      "Axem Yellow",
      "Axem Green",
      "Axem Pink"
    ],
    "Axem Rangers": [
      "Axem Black",
      "Axem Red",
      "Axem Yellow",
      "Axem Green",
      "Axem Pink"
    ],
    "Chefs": [
      "Chef Torte",
      "Apprentice"
    ],
    "Both": [
      "Chef Torte",
      "Apprentice"
    ],
    "???": {
      "Birdo": [
        "Ha ha ha ha. I'm so ... lonely. Will you play with me?",
        "Oh ... If you had played with me, I was going to give you the key to",
        "this room.",
        "Thanks!"
      ],
      "Jinx": [
        "You did well for your inexperience, Jagger."
      ],
      "Geno": [
        "Stop! Hold it right there! You don't know what you're doing. RETURN that star to me!",
        "I serve ... a higher authority ... That Star Piece belongs to everyone. You can't keep it.",
        "Hey! Chill out!",
        "Stop it! That's enough.",
        "Thanks for the help! But ... who are you?",
        "So! You're THE Mario! WE know about you!",
        "Thanks for the help. You really got me out of a jam. Why are you staring at me?",
        "Higher than that, I'm afraid! Do you two know anything about the \"Star Road\"?",
        "Completely in the dark, eh? Well, it's a big mess up there right now",
        "That's \"STAR ROAD\", my fluffy little friend"
      ]
    }
  }
}
```

### 角色列表（共108个）

- "ACTION" :416,
- "Mallow" :96,
- "Booster" :67,
- "Mario" :55,
- "CHOICE" :55,
- "Toadstool" :47,
- "Bowser" :43,
- "Geno" :41,
- "Toad" :32,
- "Valentina" :31,
- "Frogfucius" :28,
- "LOCATION" :27,
- "Axem Red" :23,
- "Gardener" :22,
- "Gaz" :21,
- "Snifit 1" :19,
- "Real Elder" :17,
- "Croco" :17,
- "Chancellor" :17,
- "Jinx" :15,
- "Snifit 2" :15,
- "Apprentice" :14,
- "King Nimbus" :13,
- "Garro" :13,
- "Belome" :12,
- "Snifit 3" :11,
- "Smithy" :10,
- "Axem Pink" :10,
- "Axem Yellow" :10,
- "Queen Nimbus" :10,
- "Shy Away" :10,
- "Bowyer" :10,
- "Vault Guard" :10,
- "Axem Black" :9,
- "Axem Green" :9,
- "Rat" :9,
- "Snifits" :9,
- "Punchinello" :9,
- "Pa'Mole" :9,
- "Miners" :8,
- "Culex" :7,
- "Pirates" :7,
- "Chef Torte" :7,
- "Mom" :7,
- "Birdo" :6,
- "Retired Guard" :6,
- "Johnny" :6,
- "Torte" :6,
- "Ma'Mole" :6,
- "Boomer" :5,
- ... 共108个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/SuperMarioRPG/SuperMarioRPG/,False,Super Mario RPG: Legend of the Seven Stars,Super Mario RPG,TOTAL,977,13755,4806,15911,-0.8242340681018927,106.06956383242323,6.504829781339302,105
../data/SuperMarioRPG/SuperMarioRPG/,False,Super Mario RPG: Legend of the Seven Stars,Super Mario RPG,male,671,9728,3347,11253,-0.8066564998800949,106.02268660048081,6.4426270380584345,48
../data/SuperMarioRPG/SuperMarioRPG/,False,Super Mario RPG: Legend of the Seven Stars,Super Mario RPG,female,129,1939,742,2239,-0.9451657146749444,106.49337309155665,6.559291989646481,11
../data/SuperMarioRPG/SuperMarioRPG/,False,Super Mario RPG: Legend of the Seven Stars,Super Mario RPG,neutral,177,2088,717,2419,-0.7836739126949759,105.86797720386672,6.745347971272383,46

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/snes/588739-super-mario-rpg-legend-of-the-seven-stars/faqs/30431"

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
JRPG类型的对话叙事参考。任天堂+Square的JRPG
