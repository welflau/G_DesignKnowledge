# 上古卷轴 · Skyrim（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：上古卷轴, 开放世界RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：开放世界RPG

## 概述
上古卷轴系列《Skyrim》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：上古卷轴（ElderScrolls）
- **游戏**：Skyrim
- **品类**：开放世界RPG
- **说明**：Bethesda开放世界RPG，海量NPC对话

### 元数据 (meta.json)

```json
{
  "game": "The Elder Scrolls V: Skyrim",
  "series": "The Elder Scrolls",
  "year": 2011,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/pc/615805-the-elder-scrolls-v-skyrim/faqs/69918",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "Dialogue with Alik'r Warrior missing; some minor NPC dialogue not included.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "SkyrimParser",
    "fileType": ".html",
    "textDivId": "faqtext",
    "startText": "===",
    "endText": "THANKS TO...",
    "playerCharacter": "Dragonborn"
  },
  "mainPlayerCharacters": [
    "Dragonborn"
  ],
  "characterGroups": {
    "playerChoice": [
      "Dragonborn"
    ],
    "male": [
      "Brynjolf",
      "Ulfric",
      "Galmar",
      "Tullius",
      "Balgruuf",
      "Arngeir",
      "Ralof",
      "Hadvar",
      "Esbern",
      "Isran",
      "Harkon",
      "Paarthurnax",
      "Erandur",
      "Nazir",
      "Tolfdir",
      "Neloth",
      "Mercer",
      "Dexion",
      "Cicero",
      "Kodlak",
      "Silus",
      "Savos",
      "Urag",
      "Festus",
      "Storn",
      "Paratus",
      "Amaund",
      "Hermaeus",
      "Farkas",
      "Whiterun Guard",
      "Verulus",
      "Sheogorath",
      "Delvin",
      "Ancano",
      "Nelacar",
      "Eorlund",
      "Vilkas",
      "Farengar",
      "Proventus",
      "Garan",
      "Gallus",
      "Enthir",
      "Orthorn",
      "Arnbjorn",
      "Razelan",
      "Septimus",
      "Odahviing",
      "Etienne",
      "Alduin",
      "Aventus",
      "Logrolf",
      "Durnehviir",
      "Clavicus",
      "Skjor",
      "Erikur",
      "Malborn",
      "Sabjorn",
      "Mallus",
      "Veezara",
      "Molag Bal",
      "Yamarz",
      "Tsun",
      "Bersi",
      "Titus Mede II",
      "Gjalund",
      "Quaranir",
      "Vyrthur",
      "Hakon",
      "Sinding",
      "Ennis",
      "Sam",
      "The Caller",
      "Adril",
      "Gunmar",
      "Peryite",
      "Hircine",
      "Barbas",
      "Felldir",
      "Lokir",
      "Miraak",
      "Cipius",
      "Tyranus",
      "Vekel",
      "Rulindil",
      "Ondolemar",
      "Calcelmo",
      "Raerek",
      "Mehrunes Dagon",
      "Wizard",
      "Hadring",
      "Gaius Maro",
      "Commander Maro",
      "Gaius",
      "Veren",
      "Kesh",
      "Dervenin",
      "Orthus",
      "Alvor",
      "Corpulus",
      "Driver",
      "Vingalmo",
      "Agmaer",
      "Durak",
      "Vald",
      "Mralki",
      "Anton",
      "Nelkir",
      "Hafnar",
      "Arniel",
      "Dirge",
      "Gissur",
      "Arvel",
      "Caius",
      "Courier",
      "Jorgen",
      "Malacath",
      "Lod",
      "Augur",
      "Torturer",
      "Tolan",
      "Aringoth",
      "Fultheim",
      "Vasha",
      "Sanguine",
      "Onmund",
      "Orthjolf",
      "Madesi",
      "Balagog",
      "Hern",
      "Lurbuk",
      "Ennodius",
      "Narfi",
      "Thorek",
      "Mathies",
      "J'zargo",
      "Orgnar",
      "Whiterun Guard 2",
      "Borri",
      "Hod",
      "Rargal",
      "Vanik",
      "Ronthil",
      "Malkus",
      "Stalf",
      "Lokil",
      "Celann",
      "Garthar",
      "Aicantar",
      "Vignar",
      "Nobleman",
      "Pelagius",
      "Malyn",
      "Estormo",
      "Sahloknir",
      "Wulfgar",
      "Einarth",
      "Hrongar",
      "Frodnar",
      "Sahrotaar",
      "Feran",
      "Edhelbor",
      "Nirilor",
      "Celegriath",
      "Athring",
      "Sidanyis",
      "Vipir",
      "Thrynn",
      "Niruin",
      "Ravyn",
      "Sailor",
      "Banning",
      "J'Kier",
      "Whiterun Guard 3",
      "Whiterun Guard 4",
      "Vilod",
      "Torolf",
      "Haming",
      "Tharstan",
      "Nikulas",
      "Deor",
      "Krosulhah",
      "Doorman",
      "Watchman",
      "Adalvald",
      "Cynric",
      "Aquilius",
      "Duilis",
      "Frorkmar",
      "Nobleman 2",
      "Rexus",
      "Alain",
      "Festus",
      "Francois",
      "Samuel",
      "Hroar",
      "Thoring",
      "Sanyon",
      "Thongvor",
      "Silus",
      "Falk",
      "Rissing",
      "Runil",
      "Sulla",
      "Lob",
      "Dagur",
      "Athis",
      "Brill",
      "Girduin",
      "Sergius",
      "Gavros",
      "Nerien",
      "Ysgramor",
      "Torygg",
      "Greybeards",
      "Mirmulnir",
      "Torturer's Assistant",
      "Gunnar",
      "Asgeir Snow-Shod",
      "Brand-Shei",
      "Gelebor",
      "Gulum-Ei",
      "Headsman",
      "Hogni Red-Arm",
      "Jyrik Gaulderson",
      "Rune",
      "Talvas Fathryon",
      "Wulf Wild-Blood",
      "Phinis Gestor",
      "Conjurer",
      "Penitus Oculatus Agent",
      "Agent 2",
      "Agent"
```

### 角色列表（共383个）

- "Dragonborn" :2474,
- "ACTION" :1216,
- "CHOICE" :707,
- "Serana" :257,
- "Brynjolf" :165,
- "STATUS" :159,
- "Ulfric" :156,
- "Galmar" :140,
- "Karliah" :139,
- "Tullius" :130,
- "Delphine" :126,
- "Rikke" :119,
- "Astrid" :115,
- "Balgruuf" :112,
- "Arngeir" :108,
- "Ralof" :75,
- "Esbern" :73,
- "Valerica" :71,
- "Isran" :66,
- "Paarthurnax" :65,
- "Hadvar" :65,
- "Erandur" :64,
- "Tolfdir" :61,
- "Harkon" :60,
- "Nazir" :60,
- "Neloth" :58,
- "Gelebor" :56,
- "Mercer" :54,
- "Dexion" :48,
- "Irileth" :47,
- "Cicero" :44,
- "Frea" :43,
- "Kodlak" :39,
- "Savos" :36,
- "Whiterun Guard" :36,
- "Silus" :34,
- "Aela" :34,
- "Urag" :33,
- "Festus" :32,
- "Hermaeus" :31,
- "Nelacar" :31,
- "Mirabelle" :31,
- "Paratus" :30,
- "Maven" :30,
- "Storn" :29,
- "Farkas" :28,
- "Gallus" :27,
- "Amaund" :27,
- "Elenwen" :27,
- "Sheogorath" :26,
- ... 共383个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/ElderScrolls/Skyrim/,False,The Elder Scrolls V: Skyrim,The Elder Scrolls,TOTAL,7619,150041,29832,181540,0.6487617179019622,99.3694435321104,6.586685059280721,379
../data/ElderScrolls/Skyrim/,False,The Elder Scrolls V: Skyrim,The Elder Scrolls,playerChoice,2433,16209,4491,18963,-0.3775186352716524,104.19762885014894,6.237254540903634,1
../data/ElderScrolls/Skyrim/,False,The Elder Scrolls V: Skyrim,The Elder Scrolls,male,3587,92905,17587,112770,0.7932948073808515,98.78394580372526,6.66136306531359,265
../data/ElderScrolls/Skyrim/,False,The Elder Scrolls V: Skyrim,The Elder Scrolls,female,1576,40840,7713,49699,0.8346853627307702,98.50921359984345,6.557989542091128,104
../data/ElderScrolls/Skyrim/,False,The Elder Scrolls V: Skyrim,The Elder Scrolls,neutral,23,87,39,108,-0.0717241379310316,99.55007957559683,11.732893280282937,9

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://gamefaqs.gamespot.com/pc/615805-the-elder-scrolls-v-skyrim/faqs/69918"

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
开放世界RPG类型的对话叙事参考。Bethesda开放世界RPG，海量NPC对话
