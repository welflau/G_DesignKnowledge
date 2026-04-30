# 地平线 · HorizonZeroDawn（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：地平线, 开放世界ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：开放世界ARPG

## 概述
地平线系列《HorizonZeroDawn》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：地平线（Horizon）
- **游戏**：HorizonZeroDawn
- **品类**：开放世界ARPG
- **说明**：Guerrilla的开放世界ARPG

### 元数据 (meta.json)

```json
{
  "game": "Horizon Zero Dawn",
  "series": "Horizon",
  "year": 2017,
  "status": "ready",
  "source": "https://game-scripts.fandom.com/wiki/Horizon_Zero_Dawn",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "2",
    "truePositive_notes": "Some sidequest and choice dialogue missing (this is to be expected as it's just a sample)",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "characterInfoSource": "https://horizon.fandom.com/wiki/",
  "parserParameters": {
    "parser": "HorizonZeroDawnParser",
    "fileType": ".html",
    "scriptStartCue": "<p><i>[We see stunning views",
    "scriptEndCue": "<center>THE END</center>"
  },
  "mainPlayerCharacters": [
    "Aloy"
  ],
  "characterGroups": {
    "male": [
      "Sylens",
      "Erend",
      "Rost",
      "Varl",
      "Olin",
      "Avad",
      "Teb",
      "Uthid",
      "Karst",
      "Resh",
      "Helis",
      "Balahn",
      "Dervahl",
      "Ligan",
      "Cren",
      "Bahavas",
      "Dran",
      "Walid",
      "Nil",
      "Odund",
      "Kikuk",
      "Elkend",
      "Itamen",
      "Lut",
      "Adolescent Male",
      "Adolescent Male #1",
      "Adolescent Male #2",
      "Child Male #1",
      "Child Male #2",
      "Bashar Mati",
      "Bast",
      "Blameless Marad",
      "Boy",
      "Charles Ronson",
      "FAS Spokesman 1",
      "FAS Spokesman 2",
      "FAS Spokesman 3",
      "General Herres",
      "Patrick Brochard-Klein",
      "Male Proctor",
      "Ted Faro",
      "Travis Tate",
      "Cultist Leader",
      "Nora Youth",
      "Attacker",
      "Three-Toed Huadiv",
      "Carja Archer",
      "Carja Spearman",
      "Carja Guard",
      "Male Carja Artisan 1",
      "Male Carja Artisan 2",
      "Brad Andac",
      "Male Contestant",
      "Sun Priest",
      "Unknown Man",
      "Unknown Man 2",
      "Carja Artisan",
      "Eclipse Officer",
      "Nora Brave Veteran",
      "Nora Gate Guard",
      "Seasoned Nora Brave",
      "Nora Keeper",
      "Nora Brave",
      "HADES",
      "Military Commander",
      "Military Commander 2",
      "Oseram Heavy",
      "Mercenary Warrior",
      "Oseram Outlander",
      "Cultist Dredger",
      "Cultist Thug",
      "Shadow Carja Crier",
      "Synthetic Voice (Zero Dawn)",
      "Shadow Heavy",
      "Shadow Soldier",
      "Cultist Punisher",
      "Multiservitor (Father)",
      "Multiservitor, Male",
      "Oseram Guard 1",
      "Oseram Guard 2",
      "Oseram Guard 3",
      "Vanguard Regular",
      "Vanguard Regular 2",
      "Geo-Thermal Maintenance Tech",
      "Greeting Nora Brave",
      "Heavy Oseram Vanguard",
      "Kikuk's Killers Outlander",
      "Connor Chasson",
      "Guliyev",
      "Jackson Frye",
      "Ron Felder",
      "Wandari",
      "Tom Paech",
      "Male interviewer",
      "Male Counselor",
      "Code Expert",
      "Corporate Spokesman",
      "Father",
      "Male Voice",
      "Male Voice (Full Stop)",
      "Usrc Tech",
      "Janeva",
      "Sunstone Guard"
    ],
    "female": [
      "Aloy",
      "Teersa",
      "Vanasha",
      "Sona",
      "Marea",
      "Lansra",
      "Vala",
      "Jezza",
      "Aidaba",
      "Petra",
      "Ersa",
      "Kam",
      "Girl",
      "Elisabet Sobeck",
      "Adolescent Female",
      "Adolescent Female #1",
      "Adolescent Female #2",
      "Child Female #1",
      "Child Female #2",
      "FAS Spokeswoman",
      "Margo Shěn",
      "Nora Mother",
      "Nora Woman",
      "Proctor",
      "Samina Ebadji",
      "Female Carja Villager 1",
      "Female Carja Villager 2",
      "Female Contestant",
      "Synthetic Voice",
      "GAIA",
      "Maintenance Tech",
      "Multiservitor",
      "Multiservitor (System)",
      "Multiservitor (Healer)",
      "Multiservitor, Female",
      "Ayomide Okilo",
      "Christina Hsu-Vhey",
      "Susanne Alpert",
      "Ella Pontes",
      "Mia Sayied",
      "Mills",
      "Mrs. Guliyev",
      "Skylar Rivera",
      "Acosta",
      "Murell",
      "Selection Counselor",
      "Female Counselor",
      "Female Voice",
      "Female Voice (FAS)",
      "Girl's Voice",
      "Woman's Voice"
    ],
    "neutral": [
      "Greeting Nora Child",
      "Greeting Young Nora Hunter"
    ],
    "trans": [
      "Janeva"
    ]
  },
  "aliases": {
    "Graphic": "SYSTEM",
    "Hades": "HADES",
    "Gaia": "GAIA",
    "Alby": "Aloy",
    "Aldy": "Aloy",
    "Aluki": "Aloy",
    "Nll": "Nil",
    "Leader": "Cultist Leader",
    "Margo Shën": "Margo Shěn",
    "Margo Shĕn": "Margo Shěn",
    "CHARLES RONSON": "Charles Ronson",
    "TED FARO": "Ted Faro",
    "TOM PAECH": "Tom Paech",
    "TRAVIS TATE": "Travis Tate",
    "Herres": "General Herres",
    "GENERAL HERRES": "Ge
```

### 角色列表（共159个）

- "Aloy" :1006,
- "ACTION" :535,
- "Sylens" :229,
- "Erend" :145,
- "Rost" :114,
- "Elisabet Sobeck" :87,
- "Teersa" :74,
- "Varl" :71,
- "Ted Faro" :65,
- "Olin" :44,
- "Avad" :43,
- "Teb" :42,
- "Vanasha" :40,
- "Sona" :32,
- "GAIA" :30,
- "Helis" :30,
- "Uthid" :29,
- "LOCATION" :26,
- "Karst" :24,
- "General Herres" :23,
- "HADES" :22,
- "Synthetic Voice" :22,
- "Resh" :21,
- "Nora Keeper" :18,
- "Marea" :18,
- "Nora Brave" :17,
- "Corporate Spokesman" :16,
- "Travis Tate" :16,
- "Janeva" :16,
- "Lansra" :16,
- "Blameless Marad" :15,
- "Balahn" :15,
- "Vala" :15,
- "Bast" :15,
- "Charles Ronson" :14,
- "Dervahl" :14,
- "Multiservitor, Female" :13,
- "Margo Shěn" :13,
- "Female Counselor" :13,
- "Carja Guard" :13,
- "Jezza" :13,
- "Male Counselor" :12,
- "Synthetic Voice (Zero Dawn)" :12,
- "Bahavas" :12,
- "Adolescent Female" :11,
- "Heavy Oseram Vanguard" :10,
- "Selection Counselor" :9,
- "Adolescent Male" :9,
- "Multiservitor" :9,
- "Cultist Leader" :9,
- ... 共159个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Horizon/HorizonZeroDawn/,False,Horizon Zero Dawn,Horizon,TOTAL,2864,50996,10946,62311,0.6451453600105381,98.73518564197174,6.678420450766537,156
../data/Horizon/HorizonZeroDawn/,False,Horizon Zero Dawn,Horizon,male,1334,28504,5689,34982,0.8457875608408099,97.92274045534596,6.760052987278136,103
../data/Horizon/HorizonZeroDawn/,False,Horizon Zero Dawn,Horizon,female,1528,22480,5254,27316,0.4171412392794789,99.69263811879648,6.578957883808574,51
../data/Horizon/HorizonZeroDawn/,False,Horizon Zero Dawn,Horizon,neutral,2,12,2,13,-0.4666666666666668,109.09500000000001,5.249933333333333,2
../data/Horizon/HorizonZeroDawn/,False,Horizon Zero Dawn,Horizon,trans,16,495,85,580,0.5074390968508631,101.79684491978611,6.82815513963161,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

page = "https://game-scripts.fandom.com/wiki/Horizon_Zero_Dawn"
#html = urlopen(page).read().decode('utf-8')
#time.sleep(2)
#o = open("raw/page01.html",'w')
#o.write(html)
#o.close()


# Datapoints

#indexpage = "https://horizon.fandom.com/wiki/Datapoints"
# Updated index page since Horizon Forbidden West
#  This is untested, and includes links to the Frozen Wilds DLC
indexpage = "https://horizon.fandom.com/wiki/List_of_datapoints_in_Horizon_Zero_Dawn"

html = urlopen(indexpage).read().decode('utf-8')
time.sleep(2)

soup = BeautifulSoup(html,'html5lib')
content = soup.find("div",{"class":"mw-parser-output"})

ols = content.findAll("ol", recursive=True)

startPos = '<span class="mw-headline" id="Content">Content</span>'
endPos = '<i>Horizon Zero Dawn</i> Datapoints'


# (only audio and hologram)
pcount = 2
for ol in ols[:2]:
	links = ol.find_all("a")
	for link in links:
		url = "https://horizon.fandom.com" + link["href"]
		t = link["title"]
		print("Extracting datapoint "+t)
		datapointContent = urlopen(url).read().decode("utf-8")
		time.sleep(2)
		
		toSave = "DATAPOINT\t"+t.strip()+"\n"+datapointContent[datapointContent.index(startPos):datapointContent.index(endPos)]
		o = open("raw/page"+"{:02d}".format(pcount)+".html",'w')
		o.write(toSave)
		o.close()
		pcount += 1

```


## 策划参考价值
开放世界ARPG类型的对话叙事参考。Guerrilla的开放世界ARPG
