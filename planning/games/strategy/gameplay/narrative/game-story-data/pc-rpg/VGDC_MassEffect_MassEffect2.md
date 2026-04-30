# 质量效应 · MassEffect2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffect2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffect2
- **品类**：科幻RPG
- **说明**：BioWare科幻RPG，跨三部曲选择延续

### 元数据 (meta.json)

```json
{
  "game": "Mass Effect 2",
  "series": "Mass Effect",
  "year": 2010,
  "status": "ready",
  "source": "Dump from custom branch of Legendary Explorer: https://github.com/ME3Tweaks/LegendaryExplorer",
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "N/A",
    "falsePositive_numErrors": "N/A",
    "falsePositive_notes": "Data extracted from game code."
  },
  "sourceFeatures": {
    "type": "game data",
    "completeness": "complete",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "parserParameters": {
    "parser": "MassEffect3ExplorerParser",
    "fileType": "ME2DialogueDump_Extended_withDLC_B.csv",
    "MainCharacterOverride": {
      "norcr3_jokershit_a_dlg": "Jeff \"Joker\" Moreau",
      "norcr3_ai_core_d_dlg": "Jeff \"Joker\" Moreau",
      "norcr3_ai_cockpit_d_dlg": "Jeff \"Joker\" Moreau",
      "norcr3_ai_engines_d_dlg": "Jeff \"Joker\" Moreau"
    }
  },
  "mainPlayerCharacters": [
    "Shepard",
    "Garrus Vakarian",
    "Tali'Zorah",
    "Jacob Taylor",
    "Miranda Lawson",
    "Kasumi Goto",
    "Zaeed Massani",
    "Grunt",
    "Legion",
    "Jack",
    "Mordin Solus",
    "Samara",
    "Thane Krios"
  ],
  "characterGroups": {
    "playerChoice": [
      "Shepard"
    ],
    "male": [
      "Other Batarian Merc hassling Daniel",
      "Garrus Vakarian",
      "Illusive Man",
      "Jeff \"Joker\" Moreau",
      "Sick Urdnot Scout",
      "Maelon",
      "Turian Checkpoint Guard (Omega)",
      "Vorcha with Rocket Launcher (Omega)",
      "Batarian Shuttle Driver (Omega)",
      "Batarian Plague Victim (Omega)",
      "Turian Worker",
      "Warden Kuril",
      "Starved Batarian",
      "Quarantined Turian",
      "Kal'Reegar",
      "Turian talking to Quarian (Eternity Bar)",
      "Human (Bachelor Party)",
      "Salarian (Bachelor Party)",
      "Turian (Bachelor Party)",
      "Stockmarket Volus",
      "Weyrloc ClanSpeaker",
      "Beacon VI (Aeia)",
      "Ronald Taylor",
      "Feral Hunter (Aeia)",
      "Officer (Aeia)",
      "Joram Talid",
      "Talid's Bodyguard",
      "Mouse",
      "Elias Kelham",
      "Kolyat Krios",
      "Jim Reynolds",
      "Joram Talid",
      "Thane Krios",
      "Volus (Fade's Lackey)",
      "Harkin (Fade)",
      "Lantar Sidonis",
      "Elcor Hamlet Advertisement",
      "C-Sec Auction Advertisement",
      "Ion Liquidators Advertisement (Keth Mak)",
      "Burgat Advertisement",
      "Dark Star Advertisement (Male)",
      "Holo Advertisement",
      "Feros Colony Investment Advertisement",
      "Pawn and Payday Loan Advertisement",
      "Safety Advertisement",
      "Dark Star Bartender",
      "Turian Customer (Citadel Souvenirs)",
      "Hamlet (elcor)",
      "Game Shop Salesman",
      "Stand Chef",
      "Shuttle Salesman",
      "Gunnery Chief",
      "Citadel Film Human Man",
      "Citadel Film Narrator",
      "Citadel Film Lance Actor",
      "Citadel Film Saren Actor",
      "Citadel Film Shepard Actor",
      "Serviceman Burnside",
      "Serviceman Chung",
      "Human Customer (Rodam Expeditions)",
      "Turian Customer (Rodam Expeditions)",
      "Investigating C-Sec Officer",
      "Kor Tun",
      "Rukar",
      "Presidium Groundskeeper",
      "Elcor (Saronis Applications)",
      "Kargesh",
      "Sergeant Haron",
      "Michael Petrovsky",
      "Tupari Vending Machine",
      "Turian at Customs",
      "Marab",
      "Etarn Tiron",
      "Salarian (Warehouse)",
      "Refund Guy",
      "Aspiring Chef (Zakera Cafe)",
      "Zakera Cafe Shopkeeper",
      "David Anderson",
      "Councillor Valern",
      "Councillor Sparatus",
      "Donnel Udina",
      "Dr. Wilson",
      "Crewman Thomas Hawthorne",
      "Wounded Merc (Korlus)",
      "Vorcha Redshirt",
      "Collector General",
      "Legion",
      "Grunt",
      "Jacob Taylor",
      "Mordin Solus",
      "Zaeed Massani",
      "Kaidan Alenko",
      "Delan",
      "Tank Grown Krogan",
      "Merc on Radio (Korlus)",
      "Okeer",
      "Kureck",
      "Teltin Scientist",
      "Security Officer Zemkl",
      "Aresh",
      "Nakmor Ambassador",
      "Nakmor Guards",
      "Urdnot Chief Scout",
      "Urdnot Wreav",
      "Natorth",
      "Krogan discussing Citadel 1",
      "Krogan discussing Citadel 2",
      "Urdnot Krogans",
      "Injured Krogan",
      "Potential Krogan Father",
      "Krogan talking to Potential Father",
      "Krogan Mechanic",
      "Blood Pack Recruiter",
      "Ratch",
      "Urdnot Overcaptain",
      "Krogan Pit Boss",
      "Krogan Xenophobe",
      "Krogan talking to Xenophobe",
      "Fortack",
      "Urdnot Wrestling 1",
      "Urdnot Wrestling 2",
      "Urdnot Wrex",
      "Gatatog Uvenk",
      "Urdnot Shaman",
      "Mess Sergeant Rupert Gardner",
      "Crewman Richard Hadley",
      "Crewman Zach Matthews",
      "Crewman Vadim Rolston",
      "Kenneth
```

### 角色列表（共384个）

- "ACTION" :28372,
- "GOTO" :15936,
- "STATUS" :10997,
- "CHOICE" :5637,
- "Shepard" :4859,
- "Jacob Taylor" :1242,
- "Miranda Lawson" :1189,
- "LOCATION" :1036,
- "Tali'Zorah" :969,
- "Mordin Solus" :929,
- "Thane Krios" :928,
- "Garrus Vakarian" :923,
- "Jack" :822,
- "Samara" :717,
- "Legion" :643,
- "Grunt" :526,
- "EDI" :521,
- "Jeff "Joker" Moreau" :414,
- "Galactic News" :390,
- "Kasumi Goto" :367,
- "Zaeed Massani" :364,
- "Illusive Man" :306,
- "Kelly Chambers" :180,
- "Morinth" :175,
- "Liara T'Soni" :152,
- "Armando-Owen Bailey" :137,
- "Kal'Reegar" :134,
- "Jedore" :127,
- "David Anderson" :111,
- "Aria T'Loak" :110,
- "Urdnot Krogans" :102,
- "Admiral Raan" :102,
- "Harbinger" :98,
- "Emily Wong" :95,
- "Background Male Quarian Chatter" :88,
- "Background Female Quarian Chatter" :88,
- "Admiral Han'Gerrel" :87,
- "Admiral Zaal'Koris" :75,
- "Warden Kuril" :73,
- "Dr. Wilson" :72,
- "Ish" :71,
- "Urdnot Chief Scout" :69,
- "Dr. Chakwas" :69,
- "Shiala" :69,
- "Urdnot Wrex" :68,
- "Kenneth Donnolly" :67,
- "Elias Kelham" :67,
- "Mouse" :66,
- "Batarian Plague Victim (Omega)" :66,
- "Urdnot Shaman" :65,
- ... 共384个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffect2/,False,Mass Effect 2,Mass Effect,TOTAL,23384,270209,62711,343067,1.072132596606389,95.05038808280163,7.1161013561117334,379
../data/MassEffect/MassEffect2/,False,Mass Effect 2,Mass Effect,playerChoice,4859,50579,10542,61068,0.5282308803160145,99.82095009832621,6.556766318336077,1
../data/MassEffect/MassEffect2/,False,Mass Effect 2,Mass Effect,male,10829,123945,31011,157451,0.9586440216157666,95.30835769260656,7.152367861358163,260
../data/MassEffect/MassEffect2/,False,Mass Effect 2,Mass Effect,female,7685,95609,21126,124424,1.531334059331975,92.14439340009966,7.366154665401419,115
../data/MassEffect/MassEffect2/,False,Mass Effect 2,Mass Effect,neutral,11,76,29,124,4.6847005444646115,66.1434210526316,9.999380943738656,3

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
