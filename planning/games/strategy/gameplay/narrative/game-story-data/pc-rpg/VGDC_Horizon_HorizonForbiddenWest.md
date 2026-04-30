# 地平线 · HorizonForbiddenWest（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：地平线, 开放世界ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：开放世界ARPG

## 概述
地平线系列《HorizonForbiddenWest》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：地平线（Horizon）
- **游戏**：HorizonForbiddenWest
- **品类**：开放世界ARPG
- **说明**：Guerrilla的开放世界ARPG

### 元数据 (meta.json)

```json
{
  "game": "Horizon Forbidden West",
  "series": "Horizon",
  "year": 2022,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "https://game-scripts-wiki.blogspot.com/2022/02/horizon-ii-forbidden-west-transcript.html",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {},
  "characterInfoSource": "",
  "parserParameters": {
    "parser": "HorizonForbiddenWestParser",
    "fileType": ".html",
    "scriptStartCue": "[A fox is running through the woods, followed by three Watchers",
    "scriptEndCue": "THE END"
  },
  "mainPlayerCharacters": [
    "Aloy"
  ],
  "characterGroups": {
    "male": [
      "Sylens",
      "Erend",
      "Rost",
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
      "Bashar Mati",
      "Bast",
      "Charles Ronson",
      "General Herres",
      "Patrick Brochard-Klein",
      "Ted Faro",
      "Travis Tate",
      "Three-Toed Huadiv",
      "Brad Andac",
      "HADES",
      "Connor Chasson",
      "Guliyev",
      "Jackson Frye",
      "Ron Felder",
      "Wandari",
      "Tom Paech",
      "Abadund",
      "Aldur",
      "Amadis",
      "Arnuf",
      "Arokkeh",
      "Arorro",
      "Blameless Marad",
      "Bohai",
      "Ceo",
      "Corend",
      "Erayyo",
      "Erik",
      "Fane",
      "Fendur",
      "Gerard",
      "Gilvarn",
      "Grudda",
      "Hakund",
      "Hataktto",
      "Hekarro",
      "Holo Projector",
      "Hologram of Dr. Somptow",
      "Javad the Willing",
      "Joruf",
      "Jorund",
      "Karhn",
      "Kotallo",
      "Kavvoh",
      "Kentokk",
      "Kenzo Sasaki",
      "Keruf",
      "Kue",
      "Larend",
      "Lawan",
      "Lel",
      "Lirokkeh",
      "Luf",
      "Marshal Fashav",
      "Milduf",
      "Morlund",
      "Nakko",
      "Nirik",
      "Nozar",
      "Odurg",
      "Penttoh",
      "Porguf",
      "Ragurt",
      "Rokko",
      "Savohar",
      "Stemmur",
      "Studious Vuadis",
      "Tekotteh",
      "Thurlis",
      "Ulvund",
      "Uvveh",
      "Varl",
      "Vetteh",
      "Zokkah",
      "Dr. Somptow",
      "Unknown Man",
      "AETHER",
      "HEPHAESTUS",
      "POSEIDON"
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
      "Elisabet Sobeck",
      "Samina Ebadji",
      "GAIA",
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
      "Alva",
      "Aquino",
      "Belna",
      "Beta",
      "Boomer",
      "Dekka",
      "Delah",
      "Eileen Sasaki",
      "Faraday",
      "Gerrah",
      "Isabel",
      "Isabet",
      "Ivinna",
      "Ivvira",
      "Jekkah",
      "Kel",
      "Kenalla",
      "Kitakka",
      "Kivva",
      "Litakka",
      "Littay",
      "Lokasha",
      "Lora",
      "Lunda",
      "Tilda van der Meer",
      "Mian",
      "Milu",
      "Minda",
      "Nakalla",
      "Nasadi",
      "Natikka",
      "Ritakka",
      "Rukka",
      "Salma",
      "Silga",
      "Sonkai",
      "Talanah",
      "Telga",
      "Terakka",
      "Untalla",
      "Urekka",
      "Verbena",
      "Volma",
      "Wekatta",
      "Yivekka",
      "Zikka",
      "Ziverra",
      "Zo",
      "Female Stranger",
      "Mysterious Woman Voice",
      "Woman's Voice",
      "DEMETER",
      "MINERVA"
    ],
    "neutral": [],
    "trans": [
      "Wekatta"
    ]
  },
  "aliases": {
    "ALoy": "Aloy",
    "Aloy & Morlund": [
      "Aloy",
      "Morlund"
    ],
    "Aoy": "Aloy",
    "Alog": "Aloy",
    "Aluf": "Luf",
    "lvvira": "Ivvira",
    "Tilda van der Meer. ": "Tilda van der Meer",
    "Amuf": "Arnuf",
    "Armuf": "Arnuf",
    "Hekarra": "Hekarro",
    "Hologram of Dr. Somptow": "Dr. Somptow",
    "Katallo": "Kotallo",
    "Katalo": "Kotallo",
    "Kavoh": "Kavvoh",
    "Pentton": "Penttoh",
    "Talanan": "Talanah",
    "Tekatteh": "Tekotteh",
    "Tekotten": "Tekotteh",
    "Ulvand": "Ulvund",
    "Vetten": "Vetteh",
    "Nakata": "Nakalla",
    "Rakka": "Rukka",
    "Patra": "Petra",
    "Male Suranger": "Male Stranger"
  }
}
```

### 角色列表（共180个）

- "Aloy" :3039,
- "ACTION" :972,
- "Varl" :391,
- "Zo" :301,
- "Erend" :247,
- "Alva" :244,
- "GAIA" :228,
- "Kotallo" :227,
- "Tilda van der Meer" :164,
- "Beta" :131,
- "Sylens" :118,
- "Talanah" :84,
- "Dekka" :66,
- "Morlund" :65,
- "LOCATION" :62,
- "Hekarro" :52,
- "Ceo" :46,
- "Lawan" :40,
- "Synthetic Voice" :39,
- "Bohai" :37,
- "Amadis" :36,
- "Ulvund" :36,
- "Petra" :36,
- "Javad the Willing" :34,
- "Abadund" :33,
- "Kue" :32,
- "Silga" :32,
- "Natikka" :29,
- "Ivvira" :28,
- "Marshal Fashav" :27,
- "Lokasha" :26,
- "HADES" :26,
- "Tenakth Survivor" :25,
- "Arokkeh" :23,
- "Penttoh" :23,
- "Stemmur" :22,
- "Avad" :21,
- "Kavvoh" :20,
- "Regalla" :19,
- "Studious Vuadis" :18,
- "Ritakka" :17,
- "HEPHAESTUS" :17,
- "Tenakth Soldier" :17,
- "Porguf" :16,
- "Erik" :16,
- "Larend" :16,
- "Delah" :16,
- "Wekatta" :15,
- "Tekotteh" :15,
- "Vanasha" :15,
- ... 共180个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Horizon/HorizonForbiddenWest/,True,Horizon Forbidden West,Horizon,TOTAL,6861,117947,21985,142901,0.7988265269939028,98.89085313492525,6.725458910271426,178
../data/Horizon/HorizonForbiddenWest/,True,Horizon Forbidden West,Horizon,male,1934,33554,6214,40393,0.7209839232481805,99.51102953990129,6.6944240876328855,70
../data/Horizon/HorizonForbiddenWest/,True,Horizon Forbidden West,Horizon,female,4671,81658,15107,98992,0.8229223743976117,98.79009678963457,6.708431477699316,58
../data/Horizon/HorizonForbiddenWest/,True,Horizon Forbidden West,Horizon,neutral,0,NA,NA,NA,NA,NA,NA,0
../data/Horizon/HorizonForbiddenWest/,True,Horizon Forbidden West,Horizon,trans,15,315,54,374,0.695158730158731,100.46845238095241,5.780531746031746,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

page = "https://game-scripts-wiki.blogspot.com/2022/02/horizon-ii-forbidden-west-transcript.html"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()


# TODO: import datapoints
# https://horizon.fandom.com/wiki/List_of_datapoints_in_Horizon_Forbidden_West
```


## 策划参考价值
开放世界ARPG类型的对话叙事参考。Guerrilla的开放世界ARPG
