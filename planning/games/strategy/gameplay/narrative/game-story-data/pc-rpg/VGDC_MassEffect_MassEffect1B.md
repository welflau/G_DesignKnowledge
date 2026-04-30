# 质量效应 · MassEffect1B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffect1B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffect1B
- **品类**：科幻RPG
- **说明**：BioWare科幻RPG，跨三部曲选择延续

### 元数据 (meta.json)

```json
{
  "game": "Mass Effect",
  "series": "Mass Effect",
  "year": 2007,
  "status": "ready",
  "source": "See Readme",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "complete",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "N/A",
    "falsePositive_numErrors": "N/A",
    "falsePositive_notes": "N/A - source is the game code"
  },
  "parserParameters": {
    "parser": "MassEffect3ExplorerParser",
    "fileType": "ME1DialogueDump_ExtendedX_withDLC.csv"
  },
  "mainPlayerCharacters": [
    "Shepard",
    "Garrus Vakarian",
    "Kaidan Alenko",
    "Liara T'Soni",
    "Ashley Williams",
    "Tali'Zorah",
    "Urdnot Wrex"
  ],
  "characterGroups": {
    "playerChoice": [
      "Shepard"
    ],
    "male": [
      "Sovereign",
      "Biotic Leader",
      "Rogue AI",
      "Darius",
      "Elanos Haliat",
      "Major Kyle",
      "Dr. Saleon",
      "Human Commander",
      "Turian Commander",
      "Turian Navigator",
      "David Anderson",
      "Donnel Udina",
      "Valern",
      "Sparatus",
      "Kaidan Alenko",
      "Richard L. Jenkins",
      "Urdnot Wrex",
      "Jeff \"Joker\" Moreau",
      "Garrus Vakarian",
      "ERCS Corporal",
      "Salarian Businessman (Rulamin)",
      "Elanus Interviewee",
      "Bel Anoleis",
      "Inamorda",
      "Lilihierax",
      "Lorik Qui'in",
      "Merchant Opold",
      "Rafael Vargas",
      "Turian ECRS Guard (Barricade)",
      "Scientist (Rift Station)",
      "Scientist 4 (Rift Station)",
      "Sick Scientist (Med Bay)",
      "Sick Scientist 1 (Med Bay)",
      "Han Olar",
      "Captain Ventralis",
      "Dr. Palon",
      "Petozi",
      "ERCS Quarantine Guard",
      "Dr. Zev Cohen",
      "Yaroslev Tartakovsky",
      "ERCS Guard 2 (Rift Station)",
      "Noveria Businessman",
      "Hotel Doorman",
      "Scientist talking to Sick Scientist",
      "Kirrahe",
      "Commander Rentola",
      "Lieutenant Ganto Imness",
      "Saren Arterius",
      "Krogan Battlemaster (Therum)",
      "Damaged Hologram",
      "Vigil",
      "Nihlus Kryik",
      "Engineer Adams",
      "Charles Pressly",
      "Indoctrinated Salarians",
      "Private Menos Avot",
      "Indoctrinated Salarian 1",
      "Indoctrinated Salarian 2",
      "Indoctrinated Salarian 3",
      "Indoctrinated Salarian 4",
      "Admiral Hackett",
      "Businessman (Port Hanshan)",
      "Turian ECRS Guard (Port Hanshan)",
      "Turian ECRS Guard 2 (Port Hanshan)",
      "Salarian Soldier (Virmire)",
      "Salarian Soldier 2 (Virmire)",
      "Dr. Droyas",
      "Normandy Requisitions Officer",
      "Balak",
      "Charn",
      "Hostage Scientist",
      "Simon Atwell",
      "Batarians",
      "Admiral Tadius Ahern",
      "Lieutenant Bryant",
      "Pinnacle Station Guard",
      "Guard Captain Vidinos",
      "Khel Burrum",
      "Tech Officer Alud Ochren",
      "Sergeant Dahga",
      "Male Soldier on Nepmos",
      "Sacred Angel Distress Call",
      "Male Biotic 2 (Presrop)",
      "Male Biotic (Presrop)",
      "Admiral Kahoku",
      "Shadow Broker Agent",
      "Biotic Terrorist Leader",
      "Insane Male Scientist",
      "Elias Keeler",
      "Salarian Consort Client",
      "Volus Consort Client",
      "Calyn",
      "Executor Venari Pallin",
      "Lieutenant Girard",
      "Conrad Verner",
      "Jahleed",
      "C-Sec Requisitions Officer",
      "Rear Admiral Mikhailovich",
      "Detective Chellick",
      "Chora's Den Patron 1",
      "Chora's Den Patron 2",
      "Volus Shopper",
      "Assassin outside Chora's Den",
      "Chorban",
      "Fist",
      "Fist's Guard",
      "Schells",
      "Colonist (Feros)",
      "Colonist 4 (Feros)",
      "Manuel",
      "Cole",
      "Blake",
      "Powell",
      "Terra Firma Protestor (Male)",
      "Charles Saracino",
      "Clerk Bosker",
      "Samesh Bhatia",
      "Finch",
      "Turian Guard (Chora's)",
      "Michael Petrovsky",
      "MSV Worthington Captain",
      "Dr. Smith",
      "Biotic Terrorist",
      "Chairman Martin Burns",
      "Dr. Wayne",
      "Corporal Toombs",
      "Barla Von",
      "Embassies Bartender",
      "Din Korlack",
      "Xeltan",
      "Ernesto Zabaleta",
      "C-Sec Officer",
      "Refund Guy",
      "Successful Refund Guy",
      "Human near door (Flux)",
      "Turian Merchant",
      "Assassin 2 outside Chora's Den",
      "Morlan",
      "Doran",
      "Expat",
      "Fist's Thug",
      "Fist's Guard 2",
      "Fist's Guard 3",
      "Fist's Guard 1",
      "Eddie Lang",
      "Harkin",
      "Jax",
      "Jax's Thug",
      "Private Fredricks",
      "Private Jaz",
      "Private Nick",
      "Septimus Oraka",
      "Blackmailer",
      "Garoth",
      "Turian C-Sec Officer",
      "David Al Talaqani",
      "Davin Reynolds",
      "Fai D
```

### 角色列表（共286个）

- "ACTION" :24634,
- "GOTO" :22249,
- "Shepard" :21284,
- "STATUS" :14189,
- "CHOICE" :9730,
- "Kaidan Alenko" :3395,
- "Ashley Williams" :3114,
- "Liara T'Soni" :2036,
- "Garrus Vakarian" :1362,
- "Tali'Zorah" :1334,
- "ANCHOR" :1275,
- "Urdnot Wrex" :1226,
- "Admiral Tadius Ahern" :1092,
- "LOCATION" :776,
- "Citadel News" :714,
- "David Anderson" :526,
- "Jeff "Joker" Moreau" :465,
- "SYSTEM" :438,
- "Gianna Parasini" :357,
- "Lizbeth Baynham" :344,
- "Mira" :286,
- "Donnel Udina" :281,
- "Kirrahe" :243,
- "Saren Arterius" :242,
- "Admiral Hackett" :216,
- "Shiala" :207,
- "Juliana Baynham" :202,
- "Ethan Jeong" :154,
- "Emily Wong" :142,
- "Bel Anoleis" :133,
- "Tech Officer Alud Ochren" :131,
- "Simon Atwell" :130,
- "Dr. Chakwas" :123,
- "Nassana Dantius" :114,
- "Davin Reynolds" :112,
- "Charles Pressly" :104,
- "Avina" :104,
- "Lorik Qui'in" :100,
- "Richard L. Jenkins" :96,
- "Macha Doyle" :96,
- "Maeko Matsuo" :89,
- "Batarians" :88,
- "Chorban" :85,
- "Vigil" :85,
- "Tevos" :81,
- "Hana Murakami" :70,
- "Colonist 5 (Feros)" :69,
- "Captain Ventralis" :68,
- "Dr. Zev Cohen" :67,
- "Gavin Hossle" :66,
- ... 共286个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffect1B/,False,Mass Effect,Mass Effect,TOTAL,31361,385744,82847,486722,1.1148202440964834,95.36292221875907,6.990820731112239,280
../data/MassEffect/MassEffect1B/,False,Mass Effect,Mass Effect,playerChoice,8119,82580,18112,99899,0.4629112379087186,99.86455846461554,6.50629571068038,1
../data/MassEffect/MassEffect1B/,False,Mass Effect,Mass Effect,male,13636,175938,37813,224718,1.29623904003717,94.05644110367771,7.2033760632987045,197
../data/MassEffect/MassEffect1B/,False,Mass Effect,Mass Effect,female,9551,126420,26792,161053,1.2828758510841478,94.26931742440811,7.010430543460449,79
../data/MassEffect/MassEffect1B/,False,Mass Effect,Mass Effect,neutral,22665,24754,23105,26208,-2.6790575804501007,116.17832636389859,0.7828708963084438,3
../data/MassEffect/MassEffect1B/,False,Mass Effect,Mass Effect,genderless,53,796,123,1034,2.2620431425419785,90.3714072394493,7.171031331454017,2

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time, os.path

pages = [
 ("https://pastebin.com/raw/eVZPgnb2", "bools.txt"),
 ("https://mod.gib.me/masseffect3/conditionals.txt", "conditionals.txt"),
 ("https://pastebin.com/raw/eqiNW7rE","plotDatabase.txt")]

for page,fn in pages:
	fileName = "raw/"+fn
	if not os.path.isfile(fileName):
		req = Request(
			page, 
			data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			}
		)

		html = urlopen(req).read()#.decode('cp1252').encode('utf-8')#.decode('ISO-8859-1')
		o = open(fileName,'wb')
		o.write(html)
		o.close()
		time.sleep(3)
	#with codecs.open(fileName, "w", "utf-8") as targetFile:
	#	targetFile.write(html)

input("The raw data is an extended dump of the game files for Mass Effect. This can be acquired using a custom branch of the ME3 Legendary Explorer (https://github.com/ME3Tweaks/LegendaryExplorer). This requires having Mass Effect installed on your computer. Press any key to continue.")
```


## 策划参考价值
科幻RPG类型的对话叙事参考。BioWare科幻RPG，跨三部曲选择延续
