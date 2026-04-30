# 最终幻想 · FFXII_B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXII_B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXII_B
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy XII",
  "series": "Final Fantasy",
  "year": 2006,
  "status": "ready",
  "source": "http://ffnerdery.blogspot.com/p/final-fantasy-xii.html",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": ""
  },
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "FF12Parser",
    "fileType": ".html",
    "PhrasesWithColonsThatAreNotNames": [
      "Ah, Vaan. I meant to tell you",
      "Note",
      "I know what you're thinking",
      "So 'ow was it? Don't tell me",
      "Then allow me to continue. I ask",
      "Voiceless words chime within your head",
      "Here's the exception"
    ],
    "PhrasesThatLookLikeNamesButAreActions": [
      "Private Residence",
      "Throne Road",
      "Nomad Village",
      "Toam Hills",
      "Starfall Field",
      "Giza's North Bank",
      "Crystal Glade",
      "Tree Stump",
      "ACTION",
      "Tree Stump",
      "Storehouse No. 5",
      "South Lift Terminal",
      "Southfall Pedestal",
      "Sparkling Light",
      "Starfall Field",
      "Shrine of the Northwest Wind",
      "Shrine of the South Wind",
      "Scrap of Paper",
      "Security Gate",
      "Security Station",
      "Scorpio Gate Stone",
      "Power Relay",
      "Pilgrim's Door",
      "Pedestal of the Dawn",
      "Gambitry Banner",
      "Ore Separation",
      "North Lift Terminal",
      "Northfall Pedestal",
      "Mysterious Magicks",
      "Gate Switchboard",
      "Gate of the Soul Ward",
      "Feywood Glyph",
      "Empyrean Way Stone",
      "Dark Crystal",
      "Crystal Glade",
      "Caution! (signs all around railing on upper and lower decks)",
      "Caution! (two signs on upper deck)",
      "Ascetic's Door",
      "Mark of Counsel",
      "Timeworn Device",
      "Way Stone",
      "Weapons of War",
      "Weather-beaten Door",
      "Ascetic's Door",
      "Pilgrim's Door",
      "Bulkhead Controls"
    ],
    "PlayerChoiceWhichIsDialogue": [
      "No,",
      "Sure,",
      "Sure.",
      "Yeah,",
      "Yes,",
      "Tell me",
      "Okay",
      "Not,",
      "It is pretty hot out here",
      "What's",
      "Of course.",
      "None at all.",
      "A Rabanastre",
      "A Nalbina",
      "A Bhujerba",
      "I don't drink",
      "I'm ready.",
      "I'm not ready.",
      "I'm really ready.",
      "Let me check",
      "Not yet.",
      "Take me to him.",
      "It's ",
      "Out west",
      "Out east",
      "Can you ",
      "How do I",
      "How do you",
      "What are",
      "Nothing, sorry.",
      "So,",
      "I've got this sunstone",
      "I would meet this Great-chief.",
      "I'll come",
      "I'm with you.",
      "I ",
      "One more time",
      "Come again?",
      "Why not?",
      "Nope.",
      "Toward the ",
      "Actually,",
      "Just passing",
      "Take me to ",
      "Let's go.",
      "No way.",
      "That fishing rod",
      "I'm a bird of prey.",
      "Show me your",
      "Just wanted to say hello",
      "Take me, please.",
      "We've been through.",
      "Huh?",
      "Here you are.",
      "Sorry",
      "You should've",
      "It'll never happen",
      "Who' this ... Rande?",
      "There's this man",
      ">Not especially.",
      "Uh ",
      "Erm ",
      "Let's hear that story",
      "No idea.",
      "It came from",
      "It likes your masks",
      "Not really",
      "Sounds fair"
    ]
  },
  "mainPlayerCharacters": [
    "Vaan",
    "Penelo",
    "Balthier",
    "Basch",
    "Fran",
    "Ashe"
  ],
  "characterGroups": {
    "male": [
      "Anastasis",
      "Ba'Gamnan",
      "Balthier",
      "Basch",
      "Havharo",
      "Kytes",
      "Larsa",
      "Migelo",
      "Nono",
      "Raz",
      "Reddas",
      "Reks",
      "Rikken",
      "Tomaj",
      "Vaan",
      "Vayne",
      "Vossler",
      "Zargabaath",
      "Bwagi",
      "Cid",
      "Bergan",
      "Gabranth",
      "Judge Ghis",
      "Jules",
      "Old Dalan",
      "Rasler",
      "War-chief Supinelu",
      "Great Chief Uball-Ka",
      "Tchigri",
      "Jinn",
      "Ondore",
      "Al-Cid",
      "Cotze",
      "Yrlon",
      "Va'Kansa",
      "Gijuk",
      "Arryl",
      "Montblanc",
      "Hurdy",
      "Horne",
      "Lulucce",
      "Tetran",
      "Gramis",
      "Dyce",
      "Nutsy",
      "Cartographers' Guild",
      "Ardent Man",
      "Homesick Man",
      "Longing Man",
      "Patient Man",
      "Poor Husband",
      "Curious Boy",
      "Gentle Gentleman",
      "Gentleman Onlooker",
      "Good Brother",
      "Haughty Boy",
      "Hesitant Man",
      "Idle Gentleman",
      "Imperious Man",
```

### 角色列表（共1093个）

- "ACTION" :1742,
- "LOCATION" :776,
- "Vaan" :448,
- "CHOICE" :259,
- "Balthier" :255,
- "Ashe" :136,
- "Basch" :124,
- "City Parijanah" :92,
- "Penelo" :89,
- "Fran" :75,
- "Bhujerban Sainikah" :74,
- "Imperial" :57,
- "Larsa" :54,
- "Ondore" :48,
- "Vossler" :43,
- "Vayne" :37,
- "Tchigri" :34,
- "Masyua" :33,
- "Judge Ghis" :32,
- "Jules" :29,
- "Mjrn" :29,
- "Huntmaster" :28,
- "Gabranth" :28,
- "Old Dalan" :27,
- "Tomaj" :27,
- "Jinn" :24,
- "Kytes" :24,
- "War-chief Supinelu" :23,
- "Cid" :23,
- "Cartographers' Guild" :23,
- "Migelo" :23,
- "Al-Cid" :21,
- "Dantro's Wife" :21,
- "Informed Shopkeep" :20,
- "Reddas" :18,
- "Drace" :17,
- "Gramis" :16,
- "STATUS" :16,
- "Jote" :15,
- "Burrogh" :15,
- "Stok" :14,
- "Blok" :14,
- "Atak" :14,
- "Dyce" :14,
- "Reks" :14,
- "Rimzat" :13,
- "Ba'Gamnan" :13,
- "Terra" :13,
- "Rabanastran (boy in brown near bridge)" :13,
- "The Moogles Eight" :12,
- ... 共1093个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXII_B/,False,Final Fantasy XII,Final Fantasy,TOTAL,5135,128742,23631,153068,0.5643533979140205,100.71996576473242,6.5441525962210765,1089
../data/FinalFantasy/FFXII_B/,False,Final Fantasy XII,Final Fantasy,male,3546,86946,16025,103277,0.5423873786706341,100.83761523004598,6.586312662091014,672
../data/FinalFantasy/FFXII_B/,False,Final Fantasy XII,Final Fantasy,female,1257,32526,5963,38735,0.589850983130729,100.54895857093659,6.357640903500834,299
../data/FinalFantasy/FFXII_B/,False,Final Fantasy XII,Final Fantasy,genderless,11,384,57,460,1.1727850877192996,98.65335526315789,7.589189035087719,2
../data/FinalFantasy/FFXII_B/,False,Final Fantasy XII,Final Fantasy,neutral,321,8886,1584,10596,0.6686039070652523,100.26078771765597,6.7703111677204175,116

```


### 数据来源脚本 (scraper.py)

```python
import time
import requests
import os

pageKeys= [
	'1yVXjEKYqboerrkavKV6FGB_3tnVoCNIP9OfikDQ5fbk',
	'1BzbP1J-Dw2oMI8FRWRSpW1Advwi3AyE7CRruQ1TW5vk',
	'1q_z56uKxi-eDPyO8JfFRbM31yJ-EqtHMmiJRi66KSk0',
	'1quvXPeaOLtvpq0yb4-RpZP4LTUBqpS3iUWfYFE7OUcs',
	'1zBy_jYXyiUVslb96hhVWcmociZ0ewX2CWNeXq750VZI',
	'1oTvIGK23B-2f8SssH9pvZeldWEsu7UePgisD_nE3kPo',
	'1dD6Rc_hIw5B19vzSj-dJZGaIohRL-u1bW4J0yjJD-dA',
	'1XsdX_O5oc4yPkPOXfH4iyn3FbGTdjQ9STiEXWGxQsjM',
	'13K_-SluOW0PiSQoM1Xp9RBXwYQ6acMJ2f-4bSifxC8I',
	'1CgLSViRqep9mMNiiRvycKhV5qgtxw9icn7SGz61OnaQ',
	'1tnoRRBg2hO1UzTAeHEfsIogKsdwzAoMYXSnAoLP2x0s'     # side quests
]

i = 0
for pageKey in pageKeys:
	i += 1
	fileName = "raw/page_"+str(i).zfill(3)+".html"
	if not os.path.isfile(fileName):
		response = requests.get('https://docs.google.com/document/d/'+ pageKey + '/export?format=html')
		o = open(fileName,'wb')
		o.write(response.content)
		o.close()
		time.sleep(3)
```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
