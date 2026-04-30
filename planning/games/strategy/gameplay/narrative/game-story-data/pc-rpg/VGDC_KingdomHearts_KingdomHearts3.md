# 王国之心 · KingdomHearts3（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：王国之心, ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：ARPG

## 概述
王国之心系列《KingdomHearts3》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：王国之心（KingdomHearts）
- **游戏**：KingdomHearts3
- **品类**：ARPG
- **说明**：Square Enix+Disney的ARPG

### 元数据 (meta.json)

```json
{
  "game": "Kingdom Hearts III",
  "series": "Kingdom Hearts",
  "year": 2019,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/ps4/718920-kingdom-hearts-iii/faqs/78466",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "2",
    "truePositive_notes": "Optional NPC dialogue not included. Some party dialogue not included. Meta needs source details.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "SimpleMovieScriptParser",
    "actionCue": "(",
    "textDivId": "faqtext",
    "startText": "----",
    "endText": "Please check out my other Kingdom Hearts scripts:"
  },
  "mainPlayerCharacters": [
    "Sora",
    "Aqua",
    "Riku",
    "Donald",
    "Goofy",
    "Mickey",
    "Kairi",
    "Lea"
  ],
  "characterGroups": {
    "male": [
      "Sora",
      "Goofy",
      "Donald",
      "Riku",
      "Mickey",
      "Woody",
      "Hiro",
      "Mike",
      "Sulley",
      "Flynn",
      "Buzz",
      "Master Xehanort",
      "Axel",
      "Jack Sparrow",
      "Luxord",
      "Hercules",
      "Young Xehanort",
      "Ventus",
      "Hayner",
      "Pence",
      "Rex",
      "Ienzo",
      "Xemnas",
      "Fred",
      "Kristoff",
      "Randall",
      "Yen Sid",
      "Dark Riku",
      "Ansem",
      "Vanitas",
      "Saïx",
      "Jiminy",
      "Demyx",
      "Marluxia",
      "Xigbar",
      "Wasabi",
      "Hades",
      "Olaf",
      "Baymax",
      "Ansem the Wise",
      "Scrooge",
      "Pete",
      "Sarge",
      "Pooh",
      "Hamm",
      "Terra-Xehanort",
      "Vexen",
      "Lea",
      "Davy Jones",
      "Rabbit",
      "Young Eraqus",
      "Will",
      "Dale",
      "Chip",
      "Barbossa",
      "Terra",
      "Gibbs",
      "Beckett",
      "Merlin",
      "Master Eraqus",
      "Roxas",
      "Riku Replica",
      "CDA Agent",
      "Tigger",
      "Piglet",
      "Gopher",
      "Lumpy",
      "Roo",
      "Little Green Man 1",
      "Little Green Man 2",
      "Little Green Man 3",
      "Corporal",
      "Zeus",
      "Marshmallow",
      "Gula",
      "Aced",
      "Ira",
      "Isa",
      "Trailer Son",
      "Citizen",
      "Narrator",
      "Ephemer"
    ],
    "female": [
      "Rapunzel",
      "Aqua",
      "Elsa",
      "Kairi",
      "Larxene",
      "Anna",
      "Mother Gothel",
      "Go Go",
      "Honey Lemon",
      "Elizabeth",
      "Maleficent",
      "Olette",
      "Boo",
      "Naminé",
      "Tia Dalma",
      "Meg",
      "Xion",
      "Woman",
      "Girl",
      "Invi",
      "Trailer Mom",
      "Star",
      "Action 7 News"
    ],
    "neutral": [
      "Chirithy",
      "Lingering Will",
      "Star 12",
      "Star 11",
      "Star 10",
      "Star 9",
      "Star 8",
      "Star 7",
      "Star 6",
      "Star 5",
      "Star 4",
      "Star 3",
      "Star 2",
      "Dusk"
    ]
  },
  "aliases": {
    "Emeralda": "Esmeralda",
    "Young Xenahort": "Young Xehanort",
    "Jack": "Jack Sparrow",
    "Donald & Goofy": [
      "Donald",
      "Goofy"
    ],
    "Sora, Donald & Goofy": [
      "Sora",
      "Donald",
      "Goofy"
    ],
    "Boy in Black": "Young Xehanort",
    "Boy in White": "Young Eraqus",
    "Anti-Aqua": "Aqua",
    "Eugene": "Flynn",
    "Little Green Men": [
      "Little Green Man 1",
      "Little Green Man 2",
      "Little Green Man 3"
    ],
    "Sora & Donald": [
      "Sora",
      "Donald"
    ],
    "Ventus & Aqua": [
      "Ventus",
      "Aqua"
    ],
    "Terra & Eraqus": [
      "Terra",
      "Master Eraqus"
    ],
    "Sora, Donald, Goofy & Mickey": [
      "Sora",
      "Donald",
      "Goofy",
      "Mickey"
    ],
    "Jiminy, Donald & Goofy": [
      "Jiminy",
      "Donald",
      "Goofy"
    ],
    "Sora, Donald, Goofy & Jiminy": [
      "Sora",
      "Donald",
      "Goofy",
      "Jiminy"
    ],
    "Donald & Goofy & Roxas & Riku & Aqua & Kairi": [
      "Donald",
      "Goofy",
      "Roxas",
      "Riku",
      "Aqua",
      "Kairi"
    ],
    "Go Go, Wasabi, Honey Lemon & Fred": [
      "Go Go",
      "Wasabi",
      "Honey Lemon",
      "Fred"
    ],
    "Sora & Hiro": [
      "Sora",
      "Hiro"
    ],
    "Sora & Company": [
      "Sora",
      "Fred",
      "Go Go",
      "Wasabi",
      "Honey Lemon"
    ],
    "Sora, Donald and Goofy": [
      "Sora",
      "Donald",
      "Goofy"
    ],
    "Sora, Donald, Goofy, Riku & Mickey": [
      "Sora",
      "Donald",
      "Goofy",
      "Riku",
      "Mickey"
    ],
    "Rapunzel & Flynn": [
      "Rapunzel",
      "Flynn"
    ],
    "Sora & Rapunzel": [
      "Sora",
      "Rapunzel"
    ],
    "Sora & Woody": [
      "Sora",
      "Woody"
    ],
    "Ansem & Xemnas": [
      "Ansem",
      "Xemnas"
    ],
 
```

### 角色列表（共120个）

- "ACTION" :2649,
- "Sora" :1247,
- "Donald" :423,
- "Goofy" :421,
- "Rapunzel" :130,
- "Riku" :127,
- "Mickey" :122,
- "Hiro" :110,
- "Woody" :110,
- "Jack Sparrow" :104,
- "Mike" :104,
- "Aqua" :93,
- "Flynn" :85,
- "Sulley" :81,
- "Buzz" :73,
- "Young Xehanort" :65,
- "Master Xehanort" :55,
- "Axel" :55,
- "Luxord" :55,
- "Elsa" :52,
- "Hercules" :49,
- "Kairi" :46,
- "Ventus" :45,
- "Anna" :44,
- "Hayner" :43,
- "Larxene" :42,
- "Fred" :40,
- "Pence" :40,
- "Ienzo" :40,
- "Rex" :38,
- "Xemnas" :38,
- "Randall" :37,
- "Kristoff" :36,
- "Jiminy" :35,
- "Vanitas" :34,
- "Ansem" :34,
- "Wasabi" :33,
- "Marluxia" :33,
- "Xigbar" :33,
- "Yen Sid" :33,
- "Dark Riku" :32,
- "Demyx" :32,
- "Saïx" :32,
- "Go Go" :31,
- "Olaf" :31,
- "Honey Lemon" :30,
- "Mother Gothel" :28,
- "Hades" :28,
- "Young Eraqus" :26,
- "Chirithy" :25,
- ... 共120个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingdomHearts/KingdomHearts3/,False,Kingdom Hearts III,Kingdom Hearts,TOTAL,5219,40808,12995,47417,-0.6542372027333361,105.34634164528319,6.563092027471395,119
../data/KingdomHearts/KingdomHearts3/,False,Kingdom Hearts III,Kingdom Hearts,male,4529,33972,11000,39529,-0.6553427267375262,105.26179095147876,6.67140896376267,82
../data/KingdomHearts/KingdomHearts3/,False,Kingdom Hearts III,Kingdom Hearts,female,651,5546,1724,6365,-0.7928412400651617,106.47658824570375,6.113597056384778,23
../data/KingdomHearts/KingdomHearts3/,False,Kingdom Hearts III,Kingdom Hearts,neutral,39,1290,270,1523,0.2046511627906984,102.1050904392765,5.672803359173127,14

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/ps4/718920-kingdom-hearts-iii/faqs/78466"

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
ARPG类型的对话叙事参考。Square Enix+Disney的ARPG
