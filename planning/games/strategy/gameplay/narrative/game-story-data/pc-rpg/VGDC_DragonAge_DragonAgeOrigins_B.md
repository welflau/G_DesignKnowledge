# 龙腾世纪 · DragonAgeOrigins_B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：龙腾世纪, CRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：CRPG

## 概述
龙腾世纪系列《DragonAgeOrigins_B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：龙腾世纪（DragonAge）
- **游戏**：DragonAgeOrigins_B
- **品类**：CRPG
- **说明**：BioWare奇幻CRPG，对话轮+同伴系统

### 元数据 (meta.json)

```json
{
  "game": "Dragon Age: Origins",
  "series": "Dragon Age",
  "year": 2009,
  "status": "ready",
  "source": "Game Data",
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
    "truePositive_notes": "Previous issue fixed.",
    "falsePositive_numTestsDone": "N/A",
    "falsePositive_numErrors": "N/A",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "DragonAgeOriginsGameDataParser",
    "fileType": ".dlg"
  },
  "mainPlayerCharacters": [
    "Warden",
    "Morrigan",
    "Wynne",
    "Alistair",
    "Zevran",
    "Leliana",
    "Sten",
    "Oghren",
    "Shale",
    "Dog"
  ],
  "characterGroups": {
    "male": [
      "Alistair",
      "Arl Eamon",
      "Arl Howe",
      "Bann Teagan",
      "Bodahn Feddic",
      "Connor",
      "Duncan",
      "Ser Jory",
      "Jowan",
      "King Cailan",
      "King Endrin Aeducan",
      "Knight-Commander Greagoir",
      "Kolgrim",
      "Leske",
      "Loghain",
      "Lucjan",
      "Master Wade",
      "Mouse",
      "Niall",
      "Oghren",
      "Riordan",
      "Sandal",
      "Seweryn",
      "Sten",
      "Tamlen",
      "Swiftrunner",
      "Uldred",
      "Valendrian",
      "Zathrian",
      "Zevran",
      "Adalbo",
      "Adwen",
      "Aller Bemot",
      "Arl Wulff",
      "Baizyl",
      "Bruntin Vollney",
      "Arl Bryland",
      "Cammen",
      "First Enchanter Irving",
      "Captain Chase",
      "Bann Ceorlic",
      "Cristof",
      "Cullen",
      "Cyrion",
      "Dairren",
      "Daveth",
      "Eirik",
      "Everd",
      "Fenarel",
      "Fergus",
      "Figor",
      "Frandlin Ivo",
      "Gethon",
      "Gorim",
      "Gwiddon",
      "Lord Harrowmont",
      "Hermit",
      "Herren",
      "Imrek",
      "Junar",
      "Loilinar",
      "Lord Bemot",
      "Lord Braden",
      "Lord Jonaley",
      "Lord Meino",
      "Lord Ronus Dace",
      "Mandar Dace",
      "Mainar",
      "Murdock",
      "Nelaros",
      "Nessa's Father",
      "Oren",
      "Orphan Ollie",
      "Paedan",
      "Starved Veteran",
      "Piotin",
      "Pol",
      "Prince Bhelen Aeducan",
      "Prince Trian Aeducan",
      "Roshen",
      "Scholar Gertek",
      "Ser Blackstone",
      "Ser Gilmore",
      "Ser Perth",
      "Ser Varal",
      "Bann Sighard",
      "Soris",
      "Teyrn Bryce Cousland",
      "Tomas",
      "Vaughan",
      "Redcliffe Doomsayer",
      "Chasind Doomsayer",
      "\"Beggar\"",
      "Owen",
      "Dwyn",
      "Bevin",
      "Berwick",
      "Lloyd",
      "Cassian",
      "Kasch",
      "Oskias",
      "Goilinar",
      "Beraht",
      "Taeodor",
      "Alarith",
      "Master Ilen",
      "Hahren Paivel",
      "Sweeney",
      "Owain",
      "Senior Enchanter Torrin",
      "Dog",
      "Ruck",
      "Sarel",
      "Varathorn",
      "Deygan",
      "Grand Oak",
      "Ahren",
      "Brother Burkel",
      "Garin",
      "Legnar",
      "Roggar",
      "Lord Denek Helmi",
      "Nevin",
      "Ordel",
      "Janar",
      "Lord Darvianak Vollney",
      "Varick",
      "Wojech Ivo",
      "Dulin Forender",
      "Vartag Gavorn",
      "Rogek",
      "Alimar",
      "Caridin",
      "Kardol",
      "Faryn",
      "Scavenger (Sword of the Beresaad)",
      "Brother Genitivi",
      "Cathaire",
      "The Guardian",
      "Havard",
      "Archon Hessarian",
      "Maferath",
      "Shartan",
      "Aneirin",
      "Liselle's Brother",
      "Master Tilver",
      "Slim Couldry",
      "Imposter Weylon",
      "Alert Guard",
      "Restless Guard",
      "Concerned Farmer 2",
      "Concerned Farmer 1",
      "Lothering Brother",
      "Godwin",
      "Kinnon",
      "Spirit of Valor",
      "Eadric",
      "Sloth Demon (Bereskarn)",
      "The Spirit of Rage",
      "Kester",
      "Mages' Collective Liaison",
      "Knight-Commander Harrith",
      "Knight-Commander Tavish",
      "Starrick the Apprentice",
      "Fayed the Apprentice",
      "Sheth the Apprentice",
      "Maleficarum (Thy Brother's Keeper)",
      "Adventurer Leader (Careless Accusations)",
      "Raelnor",
      "Taoran",
      "Hooded Courier in the Pearl",
      "Hooded Courier (Dark Alley)",
      "Hooded Courier in the Marketplace",
      "Layson",
      "Sammael",
      "Tornas the Deserter",
      "Varel Baern",
      "Patter Gritch",
      "Dernal Garrison",
      "Quartermaster (Ostagar)",
      "Quartermaster (Circle Tower)",
      "Templar Bran",
      "Male Elf Mage Apprentice",
      "Male Human Mage Apprentice 3",
      "Templar Guarding Door with Bran",
      "Male Apprentice discussing blood magic",
      "Other Male Apprentice discussing blood magic",
      "Male Human Mage Apprentice 1",
      "Male Human Enchanter (Mentor 1)",
      "Male Human Mage Apprentice (Classroom)",
      "Young 
```

### 角色列表（共1256个）

- "GOTO" :36713,
- "Warden" :19790,
- "CHOICE" :16733,
- "ACTION" :8695,
- "Alistair" :2940,
- "Morrigan" :1959,
- "Leliana" :1742,
- "Zevran" :1616,
- "Wynne" :1335,
- "Oghren" :1197,
- "Sten" :1188,
- "Duncan" :705,
- "Loghain" :640,
- "Shale" :543,
- "Anora" :497,
- "Jowan" :464,
- "Gorim" :455,
- "Bann Teagan" :364,
- "Leske" :330,
- "Soris" :329,
- "Prince Bhelen Aeducan" :316,
- "Arl Eamon" :298,
- "Rica" :288,
- "First Enchanter Irving" :276,
- "Bodahn Feddic" :256,
- "Shianni" :256,
- "Proving Master" :255,
- "Zathrian" :250,
- "Knight-Commander Greagoir" :244,
- "Brother Genitivi" :237,
- "Czibor" :230,
- "Dog" :228,
- "Vartag Gavorn" :219,
- "Slim Couldry" :195,
- "Lanaya" :192,
- "Lord Harrowmont" :192,
- "Isolde" :189,
- "Murdock" :183,
- "Dulin Forender" :167,
- "Riordan" :164,
- "Niall" :159,
- "Flemeth" :156,
- "Isabela" :140,
- "Teyrna Eleanor" :140,
- "Sarel" :134,
- "Tamlen" :134,
- "Mouse" :133,
- "Owen" :133,
- "Cammen" :130,
- "Ser Perth" :127,
- ... 共1256个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,TOTAL,61108,701258,166056,833206,0.07725438062397849,102.03038261848133,6.053969729138796,1252
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,male,26957,377660,83807,450448,0.24172302413097846,101.35578547755813,6.141464170171704,783
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,female,12311,179001,39108,213536,0.27166295839612076,101.26721207926067,5.923622195826535,288
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,neutral,215,2073,546,2466,-0.07223795741161787,102.34285121896919,6.064208668755267,61
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,trans,5,40,10,51,1.0150000000000006,94.91000000000003,6.203399999999999,1
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,cut,1874,10335,3978,12216,-0.6291304533424391,104.20054462278382,6.12431388201144,120
../data/DragonAge/DragonAgeOrigins_B/,False,Dragon Age: Origins,Dragon Age,playerChoice,19776,132255,38671,154613,-0.4613821096795814,104.46187833099052,5.9922929809368375,1

```


### 数据来源脚本 (scraper.py)

```python
import time
print("""This source for Dragon Age Origins is game data. Copy all the '.cnv' files from the game source into 'data/DragonAge/DragonAgeOrigins_B/raw'""")

print("  (sleeping for 30 seconds ...)")
time.sleep(30)
```


## 策划参考价值
CRPG类型的对话叙事参考。BioWare奇幻CRPG，对话轮+同伴系统
