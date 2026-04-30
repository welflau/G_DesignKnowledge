# 质量效应 · MassEffect3C（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffect3C》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffect3C
- **品类**：科幻RPG
- **说明**：BioWare科幻RPG，跨三部曲选择延续

### 元数据 (meta.json)

```json
{
  "game": "Mass Effect 3",
  "series": "Mass Effect",
  "year": 2012,
  "status": "ready",
  "source": "Dump from custom branch of Legendary Explorer: https://github.com/ME3Tweaks/LegendaryExplorer",
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
    "falsePositive_notes": "Data extracted from game code."
  },
  "parserParameters": {
    "parser": "MassEffect3ExplorerParser",
    "fileType": "ME3DialogueDump_Extended.csv",
    "avoidConvIDs": [
      "ss_mp_horde_narr_v1_dlg"
    ]
  },
  "mainPlayerCharacters": [
    "Shepard",
    "Garrus Vakarian",
    "James Vega",
    "Javik",
    "Kaidan Alenko",
    "Liara T'Soni",
    "EDI",
    "Ashley Williams",
    "Tali'Zorah"
  ],
  "characterGroups": {
    "playerChoice": [
      "Shepard"
    ],
    "male": [
      "Garrus Vakarian",
      "James Vega",
      "Javik",
      "David Anderson",
      "Urdnot Wreav",
      "Kaidan Alenko",
      "Admiral Hackett",
      "Admiral Han'Gerrel",
      "Admiral Zaal'Koris",
      "Armando-Owen Bailey",
      "Engineer Adams",
      "Grunt",
      "Geth Prime",
      "Illusive Man",
      "Jacob Taylor",
      "Jason Prangley",
      "Kenneth Donnelly",
      "Legion",
      "Mordin Solus",
      "Jeff \"Joker\" Moreau",
      "Quentius (new turian councilor)",
      "Cerberus Radio (Mars)",
      "Donnel Udina",
      "Urdnot Wrex",
      "Valern",
      "Sparatus",
      "Zaeed Massani",
      "Vendetta (Prothean VI)",
      "Cerberus Pilot",
      "Cerberus Assault Trooper (C-Sec Perimeter)",
      "Kolyat Krios",
      "Dr. Charleson",
      "Dr. Fredricks",
      "Cerberus Assault Trooper 2 (Gellix)",
      "Dr. Webber",
      "Dr. Baynar",
      "Henry Lawson",
      "Rupe Elkoss",
      "Citadel Announcer",
      "Male Hospital Nurse (Presidium Commons)",
      "Human C-Sec Officer (looking for turrets)",
      "Zymandis",
      "Citadel News Announcer",
      "Departing Soldier (D24)",
      "Jondum Bau",
      "Guy with Mel",
      "Lead Scientist (Hospital)",
      "Dr. Fraelik",
      "Michael Petrovsky",
      "Alliance Marine (talking to asari doctor)",
      "Balak",
      "Barla Von",
      "Dehkarr (Batarian Refugee)",
      "Batarian in Custody",
      "Siress (Salarian Businessman)",
      "Turian Businessman",
      "Elcor Ambassador",
      "Christophe Vasser (Human Refugee)",
      "Dominic Osoba",
      "Blasto",
      "Gruff Partner Bubin",
      "Vorcha Villain",
      "Stressed-Out Chief",
      "Din Korlack",
      "Ghorek",
      "Turian Guard 1 (outside Purgatory)",
      "Turian Guard 2 (outside Purgatory)",
      "Thane Krios",
      "Kai Leng",
      "David Archer",
      "Robert (Steve's Husband)",
      "Conrad Verner",
      "Turian Soldier (talking to Garrus at docks)",
      "Cerberus Commander",
      "Male Student (Grissom)",
      "C-Sec Assistant",
      "Kannik",
      "Gryll",
      "Gung-ho Civilian (Presidium Commons)",
      "Kreete",
      "Narl",
      "General Oraka",
      "Refugee (Citadel Docks)",
      "Human Customer (Refund Guy)",
      "Salarian Sales Clerk",
      "Sayn",
      "Drunk Soldier 1",
      "Drunk Soldier 2",
      "Drunk Soldier 3",
      "Darner Vosque",
      "Colonel Vaykom",
      "The Child",
      "Kirrahe",
      "Padok Wiks",
      "Primarch Victus",
      "Base Announcer (SurKesh)",
      "Cerberus Trooper 1 (SurKesh)",
      "Cerberus Assault Trooper 2 (SurKesh)",
      "Cerberus Trooper 3 (SurKesh)",
      "Cerberus Trooper 4 (SurKesh)",
      "Cerberus Trooper 5 (SurKesh)",
      "Cerberus Trooper 6 (SurKesh)",
      "Cerberus Atlas Pilot (SurKesh)",
      "Salarian Soldier 1 (SurKesh)",
      "Salarian Soldier 10 (SurKesh)",
      "Salarian Soldier 11 (SurKesh)",
      "Salarian Soldier 18 (SurKesh)",
      "Salarian Soldier 2 (SurKesh)",
      "Salarian Scientist 3 (SurKesh)",
      "Salarian Soldier 4 (SurKesh)",
      "Salarian Soldier 5 (SurKesh)",
      "Salarian Soldier 6 (SurKesh)",
      "Salarian Soldier 7 (SurKesh)",
      "Salarian Soldier 8 (SurKesh)",
      "Salarian Soldier 9 (SurKesh)",
      "Lieutenant Tolan",
      "Salarian Scientist (SurKesh lab)",
      "Salarian Scientist 2 (SurKesh lab)",
      "Salarian Solder 3 (SurKesh lab)",
      "Salarian Soldier 4 (SurKesh lab)",
      "Salarian Soldier 5 (SurKesh lab)",
      "Salarian Soldier 6 (SurKesh lab)",
      "Salarian Soldier 7 (SurKesh lab)",
      "Salarian Soldier (SurKesh lab)",
      "Jorgal Thurak",
      "Krogan Shaman",
      "Krogran Soldier 1",
      "Krogan Soldier 2",
      "Krogan Soldier 3",
      "Krogan Soldier 4",
      "Krogan Soldier 5",
      "Krogan Scout",
      "Turian Pilot (Artimec)",
      "Turian Pilo
```

### 角色列表（共482个）

- "ACTION" :46215,
- "STATUS" :23079,
- "GOTO" :15213,
- "CHOICE" :9511,
- "Shepard" :8964,
- "Liara T'Soni" :2669,
- "Garrus Vakarian" :2246,
- "EDI" :2047,
- "James Vega" :1915,
- "Javik" :1664,
- "LOCATION" :1627,
- "Ashley Williams" :1517,
- "Kaidan Alenko" :1498,
- "Tali'Zorah" :1392,
- "Urdnot Wrex" :746,
- "David Anderson" :736,
- "Admiral Hackett" :721,
- "Urdnot Wreav" :638,
- "The Catalyst" :597,
- "Padok Wiks" :560,
- "Mordin Solus" :510,
- "Citadel Female Announcer" :474,
- "Legion" :471,
- "Jeff "Joker" Moreau" :466,
- "Steve Cortez" :453,
- "Citadel Announcer" :426,
- "Samantha Traynor" :369,
- "SYSTEM" :282,
- "Miranda Lawson" :275,
- "Eve" :265,
- "Jack" :264,
- "Armando-Owen Bailey" :264,
- "Dr. Chakwas" :225,
- "Illusive Man" :222,
- "Jacob Taylor" :198,
- "Primarch Victus" :183,
- "Engineer Adams" :178,
- "Diana Allers" :176,
- "Dr. Michel" :167,
- "Aria T'Loak" :141,
- "Major Coats" :139,
- "Admiral Raan" :136,
- "Grunt" :127,
- "Lieutenant Tarquin Victus" :122,
- "Samara" :115,
- "Brynn Cole" :114,
- "Kahlee Sanders" :114,
- "Avina" :111,
- "Zaeed Massani" :109,
- "Jason Prangley" :109,
- ... 共482个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffect3C/,False,Mass Effect 3,Mass Effect,TOTAL,40540,361358,95688,458575,0.8573854798107252,95.6417958173261,7.185015568138102,476
../data/MassEffect/MassEffect3C/,False,Mass Effect 3,Mass Effect,playerChoice,8684,66068,18542,79231,-0.049407326328886114,101.76319201368426,6.533726016842767,1
../data/MassEffect/MassEffect3C/,False,Mass Effect 3,Mass Effect,male,19050,176144,45672,224711,0.967654418872975,94.99424297431865,7.26101378979429,310
../data/MassEffect/MassEffect3C/,False,Mass Effect 3,Mass Effect,female,12761,118845,31386,154229,1.2000003631702096,93.20348469816047,7.43284890739573,149
../data/MassEffect/MassEffect3C/,False,Mass Effect 3,Mass Effect,neutral,91,1052,176,1464,3.1624291393017643,83.03574879018323,7.985539267196681,15
../data/MassEffect/MassEffect3C/,False,Mass Effect 3,Mass Effect,genderless,5,64,18,79,0.36229166666666757,98.79798611111113,5.786605555555555,2

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
