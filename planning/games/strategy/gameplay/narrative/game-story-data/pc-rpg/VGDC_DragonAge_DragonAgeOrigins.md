# 龙腾世纪 · DragonAgeOrigins（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：龙腾世纪, CRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：CRPG

## 概述
龙腾世纪系列《DragonAgeOrigins》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：龙腾世纪（DragonAge）
- **游戏**：DragonAgeOrigins
- **品类**：CRPG
- **说明**：BioWare奇幻CRPG，对话轮+同伴系统

### 元数据 (meta.json)

```json
{
  "game": "Dragon Age: Origins",
  "series": "Dragon Age",
  "year": 2009,
  "status": "superseded",
  "source": "https://github.com/pod7/dragonage_compendium",
  "alternativeMeasure": true,
  "characterInfoSource": "https://dragonage.fandom.com/wiki/",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "complete",
    "dialogueOrder": false,
    "choices": "NA"
  },
  "parserParameters": {
    "parser": "DragonAgeOriginsParser",
    "fileType": ".csv"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [
      "Alistair",
      "Zevran",
      "Sten",
      "Oghren",
      "Duncan",
      "Loghain",
      "Jowan",
      "Gorim",
      "Soris",
      "Leske",
      "Teagan",
      "Bhelen",
      "Irving",
      "Zathrian",
      "Greagoir",
      "Eamon",
      "Genitivi",
      "Vartag",
      "Harrowmont",
      "Murdock",
      "Tamlen",
      "Riordan",
      "Niall",
      "Dulin",
      "Sarel",
      "Cammen",
      "Ignacio",
      "Cullen",
      "Owen",
      "Jory",
      "Daveth",
      "Kolgrim",
      "Perth",
      "Connor",
      "Hermit",
      "Fenarel",
      "Alarith",
      "Cailan",
      "Godwin",
      "Valendrian",
      "Ruck",
      "Athras",
      "Trian",
      "Lloyd",
      "Dwyn",
      "Varathorn",
      "Paivel",
      "Weylon",
      "Vaughan",
      "Swiftrunner",
      "Rogek",
      "Kylon",
      "Dairren",
      "Gilmore",
      "Otto",
      "Kardol",
      "Baizyl",
      "Frandlin",
      "Soldier",
      "Bryant",
      "Burkel",
      "Mainar",
      "Caladrius",
      "Owain",
      "Gwiddon",
      "Oskias",
      "Berwick",
      "Carroll",
      "Deygan",
      "Uldred",
      "Tomas",
      "Fergus",
      "Doomsayer",
      "Innkeeper",
      "Varick",
      "Bevin",
      "Janar",
      "Seweryn",
      "Roggar",
      "Figor",
      "Piotin",
      "Paedan",
      "Barlin",
      "Sighard",
      "Loilinar",
      "Goilinar",
      "Aneirin",
      "Nevin",
      "Eirik",
      "Landry",
      "Imrek",
      "Sweeney",
      "Lucjan",
      "Ademaro",
      "Messenger",
      "Nelaros",
      "Pol",
      "Garin",
      "Oswyn",
      "Legnar",
      "Alimar",
      "Oren",
      "Wulff",
      "Kinnon",
      "Scout",
      "Irminric",
      "Blacksmith",
      "Kasch",
      "Ordel",
      "Ceorlic",
      "Ahren",
      "Gatekeeper",
      "Cassian",
      "Roshen",
      "Ilen",
      "Cristof",
      "Bryland",
      "Taeodor",
      "Faryn",
      "Gethon",
      "Taliesen",
      "Cesar",
      "Havard",
      "Maferath",
      "Jonaley",
      "Hessarian",
      "Braden",
      "Wojech",
      "Everd",
      "Cathaire",
      "Bandelor",
      "Kester",
      "Eadric",
      "Herren",
      "Wade",
      "Rexel",
      "Bryce",
      "Shartan",
      "Adwen",
      "Blackstone"
    ],
    "female": [
      "Morrigan",
      "Leliana",
      "Wynne",
      "Anora",
      "Rica",
      "Shianni",
      "Lanaya",
      "Mother",
      "Isolde",
      "Flemeth",
      "Lily",
      "Isabela",
      "Mithra",
      "Merrill",
      "Gheyna",
      "Bella",
      "Nadezda",
      "Nancine",
      "Zerlinda",
      "Mardy",
      "Kaitlyn",
      "Branka",
      "Corra",
      "Dagna",
      "Iona",
      "Erlina",
      "Hannah",
      "Elora",
      "Filda",
      "Jarvia",
      "Cauthrien",
      "Nerav",
      "Orta",
      "Leorah",
      "Danyla",
      "Panowen",
      "Hespith",
      "Ashalle",
      "Miner",
      "Nesiara",
      "Keili",
      "Alfstanna",
      "Myaja",
      "Theohild",
      "Marjolaine",
      "Petra",
      "Perpetua",
      "Mallol",
      "Augustine",
      "Miriam",
      "Olinda",
      "Sanga",
      "Valena",
      "Teli",
      "Valora",
      "Allison",
      "Farinden",
      "Shaevra",
      "Unna",
      "Devera",
      "Maren",
      "Elva",
      "Agatha",
      "Oriana",
      "Vasilia",
      "Ealisay",
      "Nessa",
      "Habren",
      "Landra",
      "Justine",
      "Boann",
      "Marethari",
      "Nigella",
      "Liselle",
      "Brona",
      "Goldanna",
      "Dilwyn",
      "Elemena",
      "Hanashan",
      "Lenka"
    ],
    "neutral": []
  },
  "aliases": {}
}
```

### 角色列表（共1261个）

- "Player" :22199,
- "Alistair" :3053,
- "Morrigan" :2108,
- "Leliana" :1886,
- "Zevran" :1770,
- "Wynne" :1477,
- "SYSTEM" :1444,
- "Sten" :1430,
- "Oghren" :1339,
- "Loghain" :759,
- "Duncan" :732,
- "Shale" :698,
- "Jowan" :543,
- "Anora" :460,
- "Gorim" :452,
- "Soris" :409,
- "Leske" :392,
- "Teagan" :362,
- "Bhelen" :343,
- "Rica" :302,
- "Irving" :301,
- "Eamon" :290,
- "Zathrian" :271,
- "Greagoir" :270,
- "Shianni" :256,
- "Genitivi" :237,
- "Vartag" :233,
- "Harrowmont" :216,
- "Lanaya" :214,
- "Mother" :214,
- "Couldry" :209,
- "Father" :205,
- "Guard" :204,
- "Main Gossip" :202,
- "Murdock" :202,
- "Tamlen" :197,
- "Riordan" :193,
- "Isolde" :189,
- "Flemeth" :178,
- "Drunk" :174,
- "Niall" :173,
- "Dulin" :167,
- "Lily" :165,
- "Provmaster" :164,
- "STATUS" :161,
- "Sarel" :157,
- "Ash Warrior" :157,
- "Isabela" :154,
- "Cammen" :153,
- "Child" :152,
- ... 共1261个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/DragonAge/DragonAgeOrigins/,True,Dragon Age: Origins,Dragon Age,TOTAL,79824,768317,197858,912524,-0.06079592050227234,102.41483037680908,6.052028458325891,1258
../data/DragonAge/DragonAgeOrigins/,True,Dragon Age: Origins,Dragon Age,male,21513,283778,65796,336888,0.10047851318202916,102.02413487369891,6.04778632322994,140
../data/DragonAge/DragonAgeOrigins/,True,Dragon Age: Origins,Dragon Age,female,11147,150946,34539,179697,0.16199000644304107,101.685200619117,5.86883380560653,80
../data/DragonAge/DragonAgeOrigins/,True,Dragon Age: Origins,Dragon Age,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

page = "https://raw.githubusercontent.com/pod7/dragonage_compendium/master/data/origins/csv/cleaned/t_dialogue_clean.csv"

fileName = "raw/t_dialogue.csv"
req = Request(
	page, 
	data=None, 
	headers={
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
	}
)


csv = urlopen(req).read().decode('utf-8')
o = open(fileName,'w')
o.write(csv)
o.close()
time.sleep(3)

```


## 策划参考价值
CRPG类型的对话叙事参考。BioWare奇幻CRPG，对话轮+同伴系统
