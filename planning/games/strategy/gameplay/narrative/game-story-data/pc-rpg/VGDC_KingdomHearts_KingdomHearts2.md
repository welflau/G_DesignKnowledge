# 王国之心 · KingdomHearts2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：王国之心, ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：ARPG

## 概述
王国之心系列《KingdomHearts2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：王国之心（KingdomHearts）
- **游戏**：KingdomHearts2
- **品类**：ARPG
- **说明**：Square Enix+Disney的ARPG

### 元数据 (meta.json)

```json
{
  "game": "Kingdom Hearts II",
  "series": "Kingdom Hearts",
  "year": 2005,
  "status": "ready",
  "source": "https://transcripts.fandom.com/wiki/Kingdom_Hearts_II",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "errorChecks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "No errors. Examples included voiced and unvoiced dialogue.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "No errors."
  },
  "parserParameters": {
    "parser": "fandomParser2",
    "fileType": ".html",
    "scriptHasOptionalDialogueSection": false,
    "scriptStartCue": "<span class=\"mw-headline\" id=\"Opening\">Opening</span>",
    "scriptEndCue": "<div class=\"printfooter\">",
    "actionCue": "("
  },
  "mainPlayerCharacters": [
    "Sora",
    "Roxas",
    "Donald",
    "Goofy"
  ],
  "characterGroups": {
    "male": [
      "Sora",
      "Donald",
      "Goofy",
      "Roxas",
      "Hayner",
      "Mickey",
      "Jack Sparrow",
      "Pete",
      "Pence",
      "Tron",
      "Jack Skellington",
      "Sebastian",
      "Hades",
      "Riku",
      "Hercules",
      "Aladdin",
      "Simba",
      "Will",
      "Leon",
      "Pooh",
      "Axel",
      "Santa",
      "Shang",
      "Barbossa",
      "Beast",
      "Merlin",
      "Mushu",
      "Genie",
      "Iago",
      "DiZ",
      "Seifer",
      "Auron",
      "Cogsworth",
      "Xemnas",
      "Phil",
      "Cloud",
      "Ping",
      "Ansem the Wise",
      "Ansem (Riku-Ansem)",
      "Ansem (Ansem, Seeker of Darkness)",
      "Sephiroth",
      "Timon",
      "Lumiere",
      "Piglet",
      "Eric",
      "Emperor",
      "Cid",
      "Yen Sid",
      "Oogie Boogie",
      "Peddler",
      "Chip",
      "Scar",
      "Flounder",
      "Dale",
      "Rabbit",
      "MCP",
      "Banzai",
      "Lock",
      "Tigger",
      "Triton",
      "Demyx",
      "Rafiki",
      "Xaldin",
      "Ansem",
      "Producer",
      "Barrel",
      "Announcer",
      "Sark",
      "Finkelstein",
      "Yao",
      "Jafar",
      "Xigbar",
      "Pumbaa",
      "Rai",
      "Luxord",
      "Ling",
      "Scrooge",
      "Eeyore",
      "Setzer",
      "Jiminy",
      "Mufasa",
      "Pirate",
      "Mayor",
      "Roo",
      "Pain",
      "Panic",
      "Vivi",
      "Owl",
      "Gopher",
      "Bo'sun",
      "Voice",
      "Storekeeper",
      "Stitch",
      "Shan-Yu",
      "Saïx",
      "Chien Po",
      "Pirate Crew",
      "King Triton",
      "Xehanort"
    ],
    "female": [
      "Ariel",
      "Kairi",
      "Olette",
      "Maleficent",
      "Mulan",
      "Elizabeth",
      "Nala",
      "Ursula",
      "Belle",
      "Naminé",
      "Yuffie",
      "Aerith",
      "Minnie",
      "Meg",
      "Sally",
      "Tifa",
      "Mrs. Potts",
      "Shock",
      "Yuna",
      "Wardrobe",
      "Shenzi",
      "Rikku",
      "Jasmine",
      "Selphie",
      "Paine",
      "Flora",
      "Fauna",
      "Merryweather",
      "Woman",
      "Lioness",
      "Vanessa",
      "Ursula",
      "Atina",
      "Andrina",
      "Fuu",
      "Kanga",
      "Daisy",
      "Owner"
    ],
    "neutral": [
      "Computer",
      "Everyone",
      "Snails",
      "Crowd",
      "Plaque",
      "Fans",
      "Elf",
      "Announcement",
      "Shopkeeper",
      "Dusk",
      "??????"
    ]
  },
  "aliases": {
    "Jack": "Jack Skellington",
    "Captain Pete": "Pete",
    "Sora, Donald & Goofy": [
      "Sora",
      "Donald",
      "Goofy"
    ],
    "Sora, Donald, & Goofy": [
      "Sora",
      "Donald",
      "Goofy"
    ],
    "Sora, Donald, and Goofy": [
      "Sora",
      "Donald",
      "Goofy"
    ],
    "Ursula ": "Ursula",
    "Chip 'n' Dale": [
      "Chip",
      "Dale"
    ],
    "Donald & Goofy": [
      "Donald",
      "Goofy"
    ],
    "Sora & Donald": [
      "Sora",
      "Donald"
    ],
    "Sora, Donald, Goofy, & Pumbaa": [
      "Sora",
      "Donald",
      "Goofy",
      "Pumbaa"
    ],
    "Timon & Pumbaa": [
      "Timon",
      "Pumbaa"
    ],
    "Sora & Goofy": [
      "Sora",
      "Goofy"
    ],
    "Sora, Donald, Goofy, & Ping": [
      "Sora",
      "Donald",
      "Goofy",
      "Ping"
    ],
    "Mickey, Sora, & Riku": [
      "Mickey",
      "Sora",
      "Riku"
    ],
    "Sora & Jack Sparrow": [
      "Sora",
      "Jack Sparrow"
    ],
    "Sora, Mickey, & Donald": [
      "Sora",
      "Mickey",
      "Donald"
    ],
    "Sora, Goofy, & Leon": [
      "Sora",
      "Goofy",
      "Leon"
    ],
    "Sebastian & Flounder": [
      "Sebastian",
      "Flounder"
    ],
    "Ariel & Sebastian": [
      "Ariel",
      "Sebastian"
    ],
    "Lock, Shock, & Barrel": [
      "Lock",
      "Shock",
      "Barrel"
    ],
    "Sora, Ariel, & Sebastian": [
      "Sora",
      "Ariel",
      "Sebastian"
   
```

### 角色列表（共149个）

- "ACTION" :2384,
- "Sora" :1357,
- "Donald" :496,
- "Goofy" :382,
- "Roxas" :196,
- "Hayner" :116,
- "Pete" :111,
- "Mickey" :109,
- "Pence" :95,
- "Jack Sparrow" :90,
- "Sebastian" :89,
- "Ariel" :86,
- "Tron" :83,
- "Jack Skellington" :80,
- "Riku" :71,
- "Hades" :69,
- "Kairi" :66,
- "Olette" :63,
- "Hercules" :62,
- "Maleficent" :59,
- "Aladdin" :57,
- "Simba" :56,
- "Will" :56,
- "Leon" :56,
- "Pooh" :52,
- "Axel" :51,
- "Mulan" :49,
- "Saïx" :44,
- "Santa" :43,
- "Shang" :43,
- "Barbossa" :41,
- "Beast" :40,
- "Xemnas" :40,
- "Elizabeth" :38,
- "Ursula" :38,
- "Merlin" :38,
- "Mushu" :38,
- "Genie" :38,
- "Nala" :37,
- "DiZ" :35,
- "Iago" :34,
- "Belle" :33,
- "Naminé" :33,
- "Seifer" :33,
- "Auron" :32,
- "Cogsworth" :31,
- "Yuffie" :31,
- "Aerith" :31,
- "Ping" :30,
- "Phil" :30,
- ... 共149个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingdomHearts/KingdomHearts2/,False,Kingdom Hearts II,Kingdom Hearts,TOTAL,5990,47843,14959,55556,-0.6403379187326355,105.34997793271552,6.510355698661921,147
../data/KingdomHearts/KingdomHearts2/,False,Kingdom Hearts II,Kingdom Hearts,male,5103,40249,12650,46705,-0.6563840313612985,105.43556782690796,6.56322330208798,99
../data/KingdomHearts/KingdomHearts2/,False,Kingdom Hearts II,Kingdom Hearts,female,852,7359,2225,8553,-0.5855542573413874,105.15159716742171,6.162932655120764,37
../data/KingdomHearts/KingdomHearts2/,False,Kingdom Hearts II,Kingdom Hearts,neutral,35,235,82,298,0.4910871821484193,96.64615853658538,8.347667618059157,11

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://transcripts.fandom.com/wiki/Kingdom_Hearts_II"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
ARPG类型的对话叙事参考。Square Enix+Disney的ARPG
