# 龙腾世纪 · DragonAge2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：龙腾世纪, CRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：CRPG

## 概述
龙腾世纪系列《DragonAge2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：龙腾世纪（DragonAge）
- **游戏**：DragonAge2
- **品类**：CRPG
- **说明**：BioWare奇幻CRPG，对话轮+同伴系统

### 元数据 (meta.json)

```json
{
  "game": "Dragon Age 2",
  "series": "Dragon Age",
  "year": 2011,
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
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "N/A",
    "falsePositive_numErrors": "N/A",
    "falsePositive_notes": "Data extracted from game code."
  },
  "parserParameters": {
    "parser": "DragonAge2Parser",
    "fileType": ".cnv"
  },
  "mainPlayerCharacters": [
    "Hawke"
  ],
  "characterGroups": {
    "playerChoice": [
      "Hawke",
      "Aveline",
      "Varric",
      "Bethany",
      "Carver",
      "Fenris",
      "Merrill",
      "Sebastian",
      "Isabela",
      "Anders"
    ],
    "male": [
      "Carver",
      "Fenris",
      "Varric",
      "Sebastian",
      "Anders",
      "Adriano",
      "Quentin",
      "Quintus",
      "Pol",
      "Cerimon",
      "Denier",
      "Huon",
      "Jethann",
      "Leonato",
      "Osric",
      "Saemus",
      "Wilmod",
      "Brat",
      "Corff",
      "Martin",
      "Maraas",
      "Alistair",
      "Ser Roderick",
      "Talkative Man",
      "Alain",
      "Alienage Elf M1",
      "Alienage Elf M2",
      "Angry Mage M",
      "Angry Refugee",
      "Anso",
      "Arguing Male",
      "Arishok",
      "Arishok Guard",
      "Bann Teagan",
      "Aden",
      "Bartender Friend",
      "Bartrand",
      "Sketch",
      "Bodahn Feddic",
      "Bran",
      "Brekker",
      "Ser Alrik",
      "Orwald",
      "Gamlen",
      "Guardsman Wright",
      "Tobrius",
      "Hugin",
      "Hubert",
      "Hugh",
      "Keran",
      "Ketojan",
      "Castillon",
      "Master Ilen",
      "Hahren Paivel",
      "Fenarel",
      "Junar",
      "Hayder",
      "Karl",
      "Cityguard M1",
      "Closet Man",
      "Amaranthine Captain 1",
      "Amaranthine Captain 2",
      "Kirkwall Guard (Secret Rendezvous)",
      "Kirkwall Official (Secret Rendezvous)",
      "Captain Ewald",
      "Commoner M1",
      "Commoner M2",
      "Comte Guillaume de Launcet",
      "Sabin",
      "Cricket",
      "Walter",
      "Cullen",
      "Varnell",
      "Danarius",
      "Danzig",
      "Decimus",
      "Yevhen",
      "Merin",
      "Iwan",
      "Emrys",
      "Dockworker",
      "Dockworker2",
      "Dog",
      "Donnic",
      "Dougal",
      "Drunk 1",
      "Drunk M1",
      "Dwarven Scout",
      "Jansen",
      "Miner1",
      "Taarbas",
      "Hybris",
      "Mugger",
      "Nabil",
      "Nathaniel",
      "Nobleman",
      "Nobleman 1",
      "Nobleman 2",
      "Nobleman 3",
      "Harassed Human",
      "Former Werewolf",
      "Nuncio",
      "Nuncio Guard",
      "Orsino",
      "Javaris",
      "Jeven",
      "Karras",
      "Evets",
      "Fell Orden",
      "Elren",
      "Emeric",
      "Arvaarad",
      "Nexus Golem",
      "Magus Tavarin Hall",
      "Bonny Lem",
      "Tamlen",
      "Chandan",
      "Feynriel",
      "Friedrich",
      "Friedrich Thug",
      "Gascard",
      "Gen Turn In 2",
      "Gen Turn In 3",
      "Gen Turn In 4",
      "Gen Turn In 5",
      "Ghyslain",
      "Gossip Old M1",
      "Gossip Old M2",
      "Guardsman Garol",
      "Gustav",
      "Meeran",
      "Harbormaster Liam",
      "Lord Harimann",
      "Pryce",
      "Harshal",
      "Franz (Hightown Guard)",
      "Joric (Hightown Guard)",
      "Hireling 1",
      "Hireling 2",
      "Hightown Gossip 3",
      "Hightown Gossip 4",
      "Hightown Nobleman 1",
      "Hightown Nobleman 2",
      "Hunter Lieutenant",
      "Hunter 2",
      "Hunter Captain",
      "Jalen",
      "Joker1",
      "Joker2",
      "Joker3",
      "Justice",
      "Keep Noble",
      "Keep Servant Male",
      "Kelder",
      "Laborer",
      "Tal-Vashoth Leader",
      "Lowlife M1",
      "Lowlife M2",
      "Darktown Man",
      "Lucky",
      "Lyrium Smuggler",
      "Guardsman Grigor",
      "Melson",
      "Jaken",
      "Magistrate Vanard",
      "Male Elf (Darktown)",
      "Male Fereldan Urchin",
      "Male Fereldan (Darktown)",
      "Male Worshipper",
      "Guardsman (Market)",
      "Mekel",
      "Cavril",
      "Korval (Korval's Blades)",
      "Solivitus",
      "Stroud",
      "Myron",
      "Wandering Merchant",
      "Tailor (Apparel Shop)",
      "Olaf (Olaf's Armory)",
      "Terath",
      "Chandan",
      "Dalish Apprentice2",
      "Dalish Guard1",
      "Renvil Harrowmont",
      "Renvil Harrowmont's Guard",
      "Carta Lieutenant (Orzammar)",
      "Rock Demon",
      "Audacity",
      "Qunari (Lost Patrol)",
      "Qunari Ambusher",
      "Qunari Ambusher2",
      "Qunari Assassin",
      "Qunari Captain",
      "Qunari Cut A1",
      "Qunari Hunter",
      "Paxley",
      "Urn Barker",
      "Drunk 2",
      "Gossip 1",
      "Gossip 2",
      "R
```

### 角色列表（共571个）

- "GOTO" :15959,
- "ACTION" :11873,
- "CHOICE" :7826,
- "Hawke" :6219,
- "Aveline" :1604,
- "Anders" :1561,
- "Varric" :1448,
- "Merrill" :1387,
- "Isabela" :1314,
- "Fenris" :1293,
- "Carver" :629,
- "Bethany" :581,
- "Sebastian" :576,
- "Meredith" :348,
- "Arishok" :316,
- "Grand Cleric Elthina" :233,
- "Gamlen" :232,
- "Cullen" :213,
- "Leandra" :192,
- "Bodahn Feddic" :183,
- "Petrice" :169,
- "Keeper Marethari" :158,
- "Orsino" :158,
- "Thrask" :146,
- "Bran" :139,
- "Viscount Dumar" :136,
- "Hubert" :115,
- "Arianni" :113,
- "Feynriel" :107,
- "Cassandra" :105,
- "Flemeth" :103,
- "Bartrand" :98,
- "Alistair" :96,
- "Saemus" :91,
- "Emeric" :87,
- "Keran" :86,
- "Donnic" :85,
- "Gascard" :84,
- "Samson" :84,
- "Javaris" :82,
- "Grace" :82,
- "Dog" :73,
- "Dougal" :70,
- "Zevran" :67,
- "Nathaniel" :67,
- "Meeran" :66,
- "Athenril" :64,
- "Martin" :63,
- "Varric (Removed Line)" :63,
- "Corff" :56,
- ... 共571个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,TOTAL,26633,281116,67859,334367,0.06087326041950902,102.00467546394543,6.183660304103078,568
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,playerChoice,16550,167286,41251,198353,-0.017024894020883252,102.40762404776922,6.127338281155068,10
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,male,11740,131606,31130,156955,0.13160519876471,101.6489167453698,6.23305908954186,317
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,female,8118,88216,22098,104469,-0.0590629059947414,102.59629927924468,6.115585035901519,143
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,neutral,120,989,237,1196,0.3072357962908452,100.2924325385144,6.892914362203649,42
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,trans,14,170,39,200,-0.007647058823529562,102.88122926093516,6.732058069381599,1
../data/DragonAge/DragonAge2/,False,Dragon Age 2,Dragon Age,cut,453,4506,1133,5362,0.002683686632984461,102.12692064008803,6.13252787253555,65

```


### 数据来源脚本 (scraper.py)

```python
import time
print("""The source for Dragon Age 2 is game data. Copy all the '.cnv' files from the game source into 'data/DragonAge/DragonAge2/raw'""")

print("  (sleeping for 30 seconds ...)")
time.sleep(30)
```


## 策划参考价值
CRPG类型的对话叙事参考。BioWare奇幻CRPG，对话轮+同伴系统
