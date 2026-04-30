# 最终幻想 · FFVI（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFVI》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFVI
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy VI",
  "series": "Final Fantasy",
  "year": 1994,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/snes/554041-final-fantasy-iii/faqs/70118",
  "notes": "The original script is explicit about various parts that are left out. This includes that 'random townsfolk talking will likely not be included'. Note that link suggests FFIII, but the script is really for the (Japanese number) FFVI.",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
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
    "parser": "FF3Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Terra",
    "Locke",
    "Celes",
    "Edgar",
    "Sabin",
    "Cyan",
    "Shadow",
    "Gau",
    "Setzer",
    "Strago",
    "Relm",
    "Mog",
    "Gogo",
    "Umaro"
  ],
  "characterGroups": {
    "male": [
      "Henchman",
      "Edgar",
      "Man 1",
      "Man 2",
      "Rachel's Dad",
      "Arvis",
      "Banon",
      "Chancellor",
      "Cid",
      "Commander",
      "Gogo",
      "Curley",
      "Larry",
      "Moe",
      "Cyan",
      "Doma Sentry",
      "Draco",
      "Duane",
      "Duncan",
      "Elder",
      "Esper Elder",
      "Maduin",
      "Gau",
      "Gestahl",
      "Guard",
      "Guard 1",
      "Gungho",
      "Henchmen",
      "Ifrit",
      "Impresario",
      "Innkeeper",
      "Kefka",
      "King Doma",
      "Leo",
      "Locke",
      "Master",
      "Mayor",
      "Merchant",
      "Mog",
      "Odin",
      "Other Sentry",
      "Owain",
      "Owzer",
      "Patriarch",
      "Ralse",
      "Ramuh",
      "Sabin",
      "Sentry",
      "Setzer",
      "Shadow",
      "Soldier",
      "Soldier A",
      "Soldier B",
      "Soldiers",
      "Strago",
      "Thief",
      "Trooper",
      "Ultros",
      "Umaro",
      "Vargas",
      "Vicks",
      "Wedge",
      "Wolf",
      "Youth",
      "Yura"
    ],
    "female": [
      "Little Girl",
      "Rachel",
      "Celes",
      "Daryl",
      "Katarin",
      "Elayne",
      "Fairy",
      "Madonna",
      "Shiva",
      "Maria",
      "Matron",
      "Relm",
      "Terra"
    ],
    "neutral": [
      "Chadarnook",
      "Kid",
      "Loud Cheers",
      "Unknown",
      "Wrexsoul"
    ]
  },
  "aliases": {
    "Littlegirl": "Little Girl",
    "Old Man": "Arvis",
    "Creature": "Gogo",
    "Esper": "Maduin",
    "Gerad": "Edgar",
    "Gestashl": "Gestahl",
    "Mgo": "Mog",
    "Warrior": "Cyan",
    "Yelling": "Guard",
    "Girl": {
      "Terra": [
        "....",
        "... ... ...",
        "Where am I...?",
        "...head...hurts...",
        "I can't remember a thing...",
        "My name... is... Terra..."
      ],
      "Madonna": [
        "You're... an Esper? What's that pendant for?",
        "Esper World... Boy, did I take the low road or what?",
        "You the one who... saved me?"
      ]
    },
    "Man": {
      "Edgar": [
        "You mean, THIS young woman...?!",
        "Oh... sorry!"
      ],
      "Man 1": [
        "Of course. He left"
      ],
      "Man 2": [
        "Shhh I'm a Returner",
        "I... I'm gonna be sick!",
        "Urghh... gonna toss it all"
      ]
    },
    "Voice": {
      "Sabin": [
        "Give it up, Vargas!"
      ],
      "Cyan": [
        "A moment Sir! Allow me the honor!"
      ],
      "Guard 1": [
        "Got her"
      ]
    },
    "Elder": {
      "Esper Elder": [
        "We've no choice... We must do what we've been avoiding...",
        "Here's the plan. We'll cause a tempest that'll sweep all the nasty creatures out of our realm. Then we'll seal the gate... I am the last of our kind able to cast this magical seal.",
        "Pass away... but at least we will finally be safe.",
        "Let's do it. We have no other choice."
      ]
    }
  }
}
```

### 角色列表（共86个）

- "ACTION" :350,
- "Locke" :169,
- "LOCATION" :153,
- "Edgar" :137,
- "Terra" :122,
- "Celes" :116,
- "Sabin" :101,
- "Kefka" :77,
- "Cyan" :74,
- "Strago" :72,
- "COMMENT" :57,
- "Setzer" :55,
- "Banon" :49,
- "Relm" :43,
- "Gestahl" :43,
- "Leo" :34,
- "Cid" :30,
- "Soldier" :29,
- "Maduin" :23,
- "Gau" :21,
- "Shadow" :20,
- "Arvis" :20,
- "Ramuh" :19,
- "Guard" :19,
- "Impresario" :17,
- "Madonna" :13,
- "Wedge" :11,
- "Gungho" :10,
- "Elayne" :10,
- "Vargas" :10,
- "Owzer" :9,
- "Rachel" :9,
- "Yura" :8,
- "Doma Sentry" :8,
- "Vicks" :8,
- "Elder" :7,
- "Soldier B" :6,
- "Soldier A" :6,
- "Ultros" :6,
- "Mog" :5,
- "Daryl" :5,
- "Henchman" :5,
- "King Doma" :5,
- "Youth" :5,
- "Matron" :5,
- "Owain" :4,
- "Esper Elder" :4,
- "Draco" :4,
- "Sentry" :4,
- "Umaro" :3,
- ... 共86个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFVI/,False,Final Fantasy VI,Final Fantasy,TOTAL,1520,14750,5902,17625,-0.5153303964757718,103.2085293695329,6.621927132888018,83
../data/FinalFantasy/FFVI/,False,Final Fantasy VI,Final Fantasy,male,1181,12003,4501,14379,-0.4141550715409341,102.78164481818895,6.679981703750172,65
../data/FinalFantasy/FFVI/,False,Final Fantasy VI,Final Fantasy,female,332,2672,1372,3154,-0.9018736579319491,104.99733716240989,6.345065647422356,13
../data/FinalFantasy/FFVI/,False,Final Fantasy VI,Final Fantasy,neutral,7,75,29,92,-0.10671264367816136,100.43400000000003,7.554375862068966,5

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/snes/554041-final-fantasy-iii/faqs/70118"

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
