# 最终幻想 · FFXIII-2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXIII-2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXIII-2
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy XIII-2",
  "series": "Final Fantasy",
  "year": 2011,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/pc/846193-final-fantasy-xiii-2/faqs/64861",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "notes": "PlayStation 3 version",
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "FFXIII2Parser",
    "actionCue": "(",
    "textDivId": "faqtext",
    "startText": "let us begin...",
    "endText": "Acknowledgements",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Serah",
    "Noel",
    "Mog"
  ],
  "characterGroups": {
    "male": [
      "Caius",
      "Maqui",
      "Gadot",
      "Yuj",
      "Sazh",
      "Jed",
      "Duncan",
      "Dajh",
      "Thorne",
      "Snow",
      "Arbiter of Time",
      "Assistant",
      "Baxter",
      "Boy",
      "Brant",
      "Captain",
      "Captain Cryptic",
      "Chester",
      "Cole",
      "Commander",
      "Corporal Thunder",
      "Dr. M",
      "Falcon",
      "Government Agent",
      "Sentry",
      "Guard 1",
      "Guard 2",
      "Guard 3",
      "Guard 4",
      "Guard at Exit to Main Ruins Area",
      "Hope",
      "Jonah",
      "Laborer",
      "Lester",
      "Lex",
      "Male Academia Citizen 1",
      "Male Academia Citizen 2",
      "Male Bounty Hunter 1",
      "Male Bounty Hunter 2",
      "Male Bounty Hunter 3",
      "Male Bounty Hunter 4",
      "Male Bounty Hunter 5",
      "Male Citizen 1",
      "Male Citizen 2",
      "Male Guard (Bresha)",
      "Male Guard 1",
      "Male Guard 2",
      "Male Hunter 1",
      "Male Hunter 2",
      "Male Hunter 3",
      "Male Hunter 4",
      "Male Hunter 5",
      "Male Hunter 6",
      "Male Hunter on Chocobo-back",
      "Male Laborer",
      "Male NORA Member Guarding Exit",
      "Male Operator 1",
      "Male Operator 2",
      "Male Researcher",
      "Male Researcher 1",
      "Male Researcher 2",
      "Male Researcher 3",
      "Male Researcher 4",
      "Male Researcher near Entrance Time Gate",
      "Male Resident",
      "Male Soldier",
      "Male Soldier 1",
      "Male Soldier 2",
      "Male Tourist 1",
      "Male Tourist 2",
      "Male Voice",
      "Man",
      "Man at Terminal",
      "Man in Corner",
      "Man on Stairway",
      "Marlow",
      "Mog",
      "Morris",
      "Noel",
      "Porter",
      "Professor",
      "Ray",
      "Raymond",
      "Male Resident of Academia",
      "Rhett",
      "Roaming Male NORA Member",
      "Roaming Male NORA Member 1",
      "Roaming Male NORA Member 2",
      "Roaming Male NORA Member 3",
      "Roaming Male NORA Member 4",
      "Roaming Male NORA Member 5",
      "Ronan",
      "Sergeant Blitz",
      "Sitting Man",
      "Technical Engineer",
      "Thunder",
      "Thurston",
      "Tipur",
      "Torreno",
      "Walter",
      "Wandering Man 1",
      "Wandering Man 2",
      "Soldier",
      "Soldier 1",
      "Soldier 2",
      "Soldier 3",
      "Soldiers",
      "Roaming Soldier",
      "Roaming Soldier 1",
      "Roaming Soldier 2",
      "Roaming Soldier 3",
      "Roaming Soldier 4",
      "Roaming Mercenaries",
      "Roaming Mercenary 4",
      "Roving Mercenary 1",
      "Roving Mercenary 2",
      "Roving Mercenary 3",
      "Operator",
      "Pilot",
      "Patrolling Man 1",
      "Patrolling Man 2",
      "Patrolling Man 3",
      "Patrolling Man 4",
      "Patrolling Man 5",
      "Patrolling Man 6",
      "Guard",
      "Resident Holed Up in Shack",
      "Wandering Kid 2",
      "Male NORA Member near lower barrier",
      "Male Guard",
      "Male Hunter",
      "Man guarding Barrier"
    ],
    "female": [
      "Serah",
      "Alyssa",
      "Yeul",
      "Chocolina",
      "Lebreau",
      "Vanille",
      "Alyssa's Duplicate",
      "Brenda",
      "Bridget",
      "Casino Staff",
      "Casino Vender",
      "Catlin",
      "Cordelia",
      "Fake Lightning",
      "Fang",
      "Female Academia Citizen 1",
      "Female Academia Citizen 2",
      "Female Citizen 1",
      "Female Citizen 2",
      "Female Citizen 3",
      "Female Guard",
      "Female Guard 1",
      "Female Guard 2",
      "Female NORA Member",
      "Female Operator",
      "Female Researcher",
      "Female Researcher 1",
      "Female Researcher 2",
      "Female Researcher 3",
      "Female Researcher 4",
      "Female Researcher 5",
      "Female Resident",
      "Female Tourist 1",
      "Female Voice",
      "Girl",
      "Female Hunter (Chocobo Stables)",
      "Female Hunter (Weather Device)",
      "Female Hunter 1",
      "Female Hunter 2
```

### 角色列表（共210个）

- "ACTION" :2925,
- "Serah" :1035,
- "Noel" :961,
- "CHOICE" :547,
- "Mog" :373,
- "Hope" :128,
- "Snow" :119,
- "Caius" :102,
- "Alyssa" :94,
- "SYSTEM" :92,
- "Lightning" :76,
- "Yeul" :70,
- "Maqui" :56,
- "Gadot" :53,
- "Chocolina" :50,
- "Yuj" :42,
- "Lebreau" :41,
- "Female Voice" :40,
- "Tipur" :35,
- "Guard" :27,
- "Myta" :25,
- "Miss Horizon" :22,
- "Vanille" :21,
- "Male Researcher 1" :21,
- "Captain Cryptic" :20,
- "Male Researcher 2" :20,
- "Roaming Male NORA Member 3" :19,
- "Female Guard" :18,
- "Male Researcher" :18,
- "Female Researcher 1" :17,
- "Rhett" :17,
- "Sazh" :15,
- "Technical Engineer" :14,
- "Female Researcher 2" :14,
- "Torreno" :13,
- "Female Resident" :13,
- "Male NORA Member Guarding Exit" :13,
- "Baxter" :12,
- "Falcon" :12,
- "Captain" :12,
- "Female NORA Member" :12,
- "Man guarding Barrier" :12,
- "Porter" :11,
- "Guard 2" :11,
- "Alyssa's Duplicate" :10,
- "Sentry" :10,
- "Raymond" :9,
- "Male Voice" :9,
- "Lex" :9,
- "Corporal Thunder" :9,
- ... 共210个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXIII-2/,False,Final Fantasy XIII-2,Final Fantasy,TOTAL,4292,68922,13977,83323,0.5986962996123193,99.55307158976042,6.4880065282846395,207
../data/FinalFantasy/FFXIII-2/,False,Final Fantasy XIII-2,Final Fantasy,male,2538,40352,8203,48707,0.5717032287031039,99.72535821851699,6.545288409099763,132
../data/FinalFantasy/FFXIII-2/,False,Final Fantasy XIII-2,Final Fantasy,female,1747,28325,5733,34232,0.5976862822799021,99.57739924369052,6.374510949075581,71
../data/FinalFantasy/FFXIII-2/,False,Final Fantasy XIII-2,Final Fantasy,neutral,4,89,20,107,0.3320168539325863,100.60813764044944,7.405534606741573,3
../data/FinalFantasy/FFXIII-2/,False,Final Fantasy XIII-2,Final Fantasy,genderless,3,156,20,277,8.404564102564104,48.698769230769244,11.81716205128205,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/pc/846193-final-fantasy-xiii-2/faqs/64861"

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
