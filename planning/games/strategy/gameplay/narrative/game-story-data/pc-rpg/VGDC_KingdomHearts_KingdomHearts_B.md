# 王国之心 · KingdomHearts_B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：王国之心, ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：ARPG

## 概述
王国之心系列《KingdomHearts_B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：王国之心（KingdomHearts）
- **游戏**：KingdomHearts_B
- **品类**：ARPG
- **说明**：Square Enix+Disney的ARPG

### 元数据 (meta.json)

```json
{
  "game": "Kingdom Hearts",
  "series": "Kingdom Hearts",
  "year": 2002,
  "status": "ready",
  "source": "https://transcripts.fandom.com/wiki/Kingdom_Hearts",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "errorChecks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "As noted and expected, some optional text-based dialogue not captured.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "No errors."
  },
  "parserParameters": {
    "parser": "KingdomHeartsParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Sora",
    "Donald",
    "Goofy"
  ],
  "characterGroups": {
    "male": [
      "Sora",
      "Donald",
      "Riku",
      "Goofy",
      "Leon",
      "Pooh",
      "Philoctetes",
      "Ansem",
      "Cid",
      "Genie",
      "Aladdin",
      "Triton",
      "Hades",
      "Owl",
      "Peter Pan",
      "Piglet",
      "Jafar",
      "Rabbit",
      "Jiminy",
      "Captain Hook",
      "Tigger",
      "Cheshire Cat",
      "Pinocchio",
      "Tarzan",
      "Finkelstein",
      "Sebastian",
      "Beast",
      "Clayton",
      "Merlin",
      "Hercules",
      "Oogie Boogie",
      "Cloud",
      "Geppetto",
      "Eeyore",
      "Barrel",
      "Mayor",
      "Iago",
      "Lock",
      "Doorknob",
      "White Rabbit",
      "Roo",
      "Jetsam",
      "Flotsam",
      "Mickey",
      "Smee",
      "Flounder",
      "Tidus",
      "Sephiroth",
      "Chip",
      "Wakka",
      "Dale",
      "Jack Skellington",
      "Xemnas"
    ],
    "female": [
      "Kairi",
      "Maleficent",
      "Ariel",
      "Aerith",
      "Ursula",
      "Queen of Hearts",
      "Yuffie",
      "Jane",
      "Alice",
      "Fairy Godmother",
      "Jasmine",
      "Cinderella",
      "Aurora",
      "Shock",
      "Snow White",
      "Wendy",
      "Sally",
      "Belle",
      "Minnie",
      "Selphie",
      "Daisy",
      "Grandmother",
      "Sora's Mom"
    ],
    "neutral": [
      "Card Soldier",
      "Moogle",
      "Flower"
    ]
  },
  "aliases": {
    "Hook": "Captain Hook",
    "Snow Whtie": "Snow White",
    "Sebstian": "Sebastian",
    "Jack": "Jack Skellington",
    "Donald & Goofy": [
      "Donald",
      "Goofy"
    ],
    "Sora & Donald": [
      "Sora",
      "Donald"
    ],
    "Sora & Goofy": [
      "Sora",
      "Goofy"
    ],
    "Flotsam & Jetsam": [
      "Flotsam",
      "Jetsam"
    ],
    "Sora, Donald & Goofy": [
      "Sora",
      "Donald",
      "Goofy"
    ],
    "Donald & Sora": [
      "Donald",
      "Sora"
    ],
    "hades": "Hades",
    "Voice": "Mickey",
    "Ansem (in robed form)": "Ansem",
    "Queen Of Hearts": "Queen of Hearts",
    "Sora’S Mom": "Sora's Mom",
    "ACTION": {
      "Donald": [
        "\"Donald, Sorry to rush off without sayin' goodbye, but there's big trouble brewin'"
      ]
    },
    "????": {
      "Sora": [
        "I've been having these weird thoughts lately... Like, is any of this for real or not?",
        "Yes.",
        "I can't open it...",
        "Friendship.",
        "To be strong.",
        "Being indecisive.",
        "Sounds good.",
        "Whoa!",
        "Gimme a break, Kairi."
      ],
      "Leon": [
        "Sora. You did it."
      ],
      "Riku": [
        "Hey!"
      ],
      "Captain Hook": [
        "And the brat's friends are the king's lackeys. Swoggle me eyes, they're all bilge rats by the look of them.",
        "Shut up!",
        "Just remember, this is no pleasure cruise. It won't be a pleasant voyage.",
        "Not so fast. No shenanigans aboard my vessel, boy.",
        "That scurvy brat thinks he can order me around!"
      ],
      "Smee": [
        "What shall we do, Captain Hook?",
        "But, Captain, you-know-who is also down-"
      ],
      "Philoctetes": [
        "Good timing. Give me a hand, will ya? Move that pedestal over there for me.",
        "I gotta spruce this place up for the games.",
        "What? Too heavy? Since when have you been such a little-"
      ],
      "Pooh": [
        "Think, think. Think, think.",
        "Nothing. Just thinking.",
        "I was thinking of how to say goodbye to Pooh."
      ]
    },
    "???????": {
      "Selphie": [
        "What's most important to you?",
        "Is friendship such a big deal?"
      ],
      "Jasmine": [
        "Who's there? Hello?",
        "I'm Jasmine. My father is the sultan of Agrabah."
      ],
      "Clayton": [
        "Highly doubtful.",
        "A circus of clowns. Not much use for hunting gorillas."
      ]
    },
    "?????": {
      "Wakka": [
        "What do you want outta life?",
        "To be strong, huh?"
      ],
      "Mickey": [
        "Riku, can you hear me? I'll be there soon.",
        "I have the other Keyblade-the one that belongs
```

### 角色列表（共81个）

- "ACTION" :1208,
- "Sora" :458,
- "Donald" :165,
- "Goofy" :144,
- "Riku" :142,
- "Kairi" :74,
- "Leon" :57,
- "Maleficent" :50,
- "Ansem" :50,
- "Pooh" :48,
- "Philoctetes" :44,
- "Ariel" :37,
- "Cid" :37,
- "Aerith" :36,
- "Mickey" :35,
- "Peter Pan" :32,
- "Genie" :31,
- "Aladdin" :30,
- "Jack Skellington" :29,
- "Ursula" :28,
- "Triton" :27,
- "Yuffie" :27,
- "Hades" :26,
- "Captain Hook" :25,
- "Owl" :24,
- "Jane" :24,
- "Tarzan" :24,
- "Queen of Hearts" :24,
- "Jafar" :24,
- "Piglet" :23,
- "Rabbit" :21,
- "Jiminy" :20,
- "Tigger" :18,
- "Cheshire Cat" :17,
- "Pinocchio" :16,
- "Merlin" :16,
- "Sebastian" :15,
- "Clayton" :15,
- "Alice" :15,
- "Finkelstein" :14,
- "Beast" :13,
- "Geppetto" :13,
- "Fairy Godmother" :13,
- "Oogie Boogie" :12,
- "Xemnas" :11,
- "Jasmine" :11,
- "Hercules" :11,
- "Cloud" :10,
- "Cinderella" :8,
- "Eeyore" :8,
- ... 共81个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingdomHearts/KingdomHearts_B/,False,Kingdom Hearts,Kingdom Hearts,TOTAL,2176,19847,5555,22999,-0.5225850360115345,105.17284702175061,6.190923406443632,79
../data/KingdomHearts/KingdomHearts_B/,False,Kingdom Hearts,Kingdom Hearts,male,1776,15418,4439,17705,-0.6850803464299524,106.16061391995638,6.234934304301274,53
../data/KingdomHearts/KingdomHearts_B/,False,Kingdom Hearts,Kingdom Hearts,female,394,4381,1102,5233,0.0552631806791517,101.74718638498783,6.039455127052099,23
../data/KingdomHearts/KingdomHearts_B/,False,Kingdom Hearts,Kingdom Hearts,neutral,6,48,13,61,0.8458333333333332,95.5748076923077,6.1223467948717945,3

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/ps3/684080-kingdom-hearts-hd-15-remix/faqs/68066"

req = Request(
    page, 
    headers={
        'User-Agent': 'XYZ/3.0'
    }
)

html = urlopen(req, timeout=10).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()
```


## 策划参考价值
ARPG类型的对话叙事参考。Square Enix+Disney的ARPG
