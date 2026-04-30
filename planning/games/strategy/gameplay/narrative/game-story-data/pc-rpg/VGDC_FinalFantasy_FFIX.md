# 最终幻想 · FFIX（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFIX》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFIX
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy IX",
  "series": "Final Fantasy",
  "year": 2000,
  "status": "superseded",
  "source": "http://www.finalfantasyquotes.com/ff9/script",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "FF9Parser",
    "fileType": ".html",
    "characterClassIdentifier": "ff7"
  },
  "mainPlayerCharacters": [
    "Squall"
  ],
  "characterGroups": {
    "male": [
      "Zidane",
      "Blank",
      "Marcus",
      "Puck",
      "Baku",
      "Amarant",
      "Benero",
      "Blutzen, Pluto Knight Ii",
      "Bunce",
      "Cinna",
      "Dante The Signmaker",
      "Engineer Zebolt",
      "Fratley",
      "Garland",
      "Haagen, Pluto Knight Viii",
      "Kohel, Pluto Knight Iii",
      "Weimar, Pluto Knight Vii",
      "Harold Pathknower",
      "Innkeeper Hal",
      "King Leo",
      "King Of Burmecia",
      "Kuja",
      "Marcus",
      "Mene",
      "Minister Artania",
      "Morrid",
      "Phillipo",
      "Pointy-hat Boy",
      "Ramuh",
      "Steiner",
      "Stiltzkin",
      "Thorn",
      "Tot",
      "Vivi",
      "Zenero",
      "Zorn"
    ],
    "female": [
      "Beatrix",
      "Brahne",
      "Cornelia",
      "Garnet",
      "Eiko",
      "Erin",
      "Flower Maiden Sharon",
      "Water Maiden Shannon",
      "Freya",
      "Hilda",
      "Lani",
      "Lilian",
      "Lucella",
      "Maliris",
      "Mikoto",
      "Mog",
      "Mogmi",
      "Moon Maiden Claire",
      "Part-time Worker Mary",
      "Ruby",
      "Shopkeeper Eve",
      "Wendy Grocer"
    ],
    "genderless": [
      "Qu",
      "Quale",
      "Quina"
    ],
    "neutral": [
      "Antlion",
      "Chimomo",
      "Choco",
      "Forest Oracle Kildea",
      "Night Oracle Donnegan",
      "Sand Oracle Safrea",
      "Tree Oracle Wylan",
      "Kraken",
      "Kupo",
      "Lich",
      "Moco",
      "Moguta",
      "Monster",
      "Necron",
      "Poncho",
      "Taharka",
      "Tiamat",
      "Moogle",
      "Atla",
      "Grimo",
      "Gumo",
      "Kumool",
      "Kumop",
      "Kupo",
      "Kuppo",
      "Mimoza",
      "Mocchi",
      "Mochos",
      "Mogki",
      "Mogmat",
      "Mogmi",
      "Mogrich",
      "Mogrika",
      "Mogryo",
      "Mogsam",
      "Mogtaka",
      "Mois",
      "Mojito",
      "Momatose",
      "Monev",
      "Monty",
      "Moodon",
      "Mooel",
      "Moolan",
      "Moonte",
      "Moorock",
      "Morrison",
      "Mopli",
      "Mosco",
      "Mosh",
      "Mozme",
      "Nazna",
      "Noggy",
      "Serino",
      "Suzuna"
    ]
  },
  "aliases": {
    "Rat Kid": "Puck",
    "Red-haired Man": "Amarant",
    "Red-headed Man": "Amarant",
    "Dagger": "Garnet",
    "Hooded Girl": "Garnet",
    "Little Girl": "Eiko",
    "Frea": "Freya",
    "Mysterious Girl": "Mikoto",
    "Queen Garnet": "Garnet",
    "Queen Brahne": "Brahne",
    "Regent Cid": "Cid",
    "Sir Fratley": "Fratley",
    "Stranger": "Fratley",
    "Vivi?": "Vivi",
    "Qu": {
      "Quina": [
        "You got frog!",
        "Me?"
      ]
    }
  }
}
```

### 角色列表（共152个）

- "Zidane" :1877,
- "ACTION" :1390,
- "Garnet" :850,
- "Steiner" :520,
- "Vivi" :375,
- "Eiko" :243,
- "Freya" :191,
- "Cid" :136,
- "Kuja" :111,
- "Marcus" :103,
- "Thorn" :100,
- "Zorn" :100,
- "Blank" :94,
- "Quina" :89,
- "Amarant" :85,
- "Voice" :81,
- "Beatrix" :77,
- "Tot" :71,
- "CHOICE" :59,
- "Cinna" :59,
- "Brahne" :52,
- "Puck" :48,
- "Baku" :48,
- "Black Mage" :44,
- "Minister Artania" :44,
- "Elite Guard" :44,
- "Garland" :42,
- "Lani" :31,
- "King Leo" :29,
- "Girl" :29,
- "Soldier" :28,
- "Bunce" :28,
- "Woman At The Counter" :28,
- "Lucella" :24,
- "Mog" :20,
- "Quale" :20,
- "Officer" :20,
- "Ramuh" :17,
- "Fratley" :17,
- "Haagen, Pluto Knight Viii" :17,
- "Tall Guard" :16,
- "Sleepy Soldier" :16,
- "Pluto Knight" :16,
- "Black Mage No. 288" :15,
- "Morrison" :14,
- "Short Guard" :14,
- "Benero" :14,
- "Zenero" :14,
- "Moogle" :14,
- "Burmecian Soldier" :13,
- ... 共152个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFIX/,True,Final Fantasy IX,Final Fantasy,TOTAL,6353,63794,22764,75522,-0.5277286100726588,103.83754532558888,6.499406823326027,149
../data/FinalFantasy/FFIX/,True,Final Fantasy IX,Final Fantasy,male,3839,38062,13533,44668,-0.6451170159653064,104.69719419459996,6.472523068465964,35
../data/FinalFantasy/FFIX/,True,Final Fantasy IX,Final Fantasy,female,1551,14736,5710,17538,-0.5397834931573264,103.5291527635955,6.445461323753401,22
../data/FinalFantasy/FFIX/,True,Final Fantasy IX,Final Fantasy,genderless,109,999,353,1168,-0.6900927556451624,105.0508095347472,5.657760295990041,2
../data/FinalFantasy/FFIX/,True,Final Fantasy IX,Final Fantasy,neutral,96,978,309,1138,-0.6251607203129002,105.18198493060932,7.716768616355948,22

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path
import re

base = "http://www.finalfantasyquotes.com"
indexPage = "http://www.finalfantasyquotes.com/ff9/script/Alexandria"
index = urlopen(indexPage).read().decode('utf-8')
pages = re.findall("href=['\"](/ff[0-9]+/script/.*?)['\"]>",index)

pages = [x.replace("&amp;","&") for x in pages]

pageNum = 0
for page in pages:
	print(page)
	pageNum += 1
	fileName = "raw/page_"+str(pageNum).zfill(3)+".html"
	if not path.exists(fileName):
		html = urlopen(base+page).read().decode('utf-8')
		o = open(fileName,'w')
		o.write(html)
		o.close()
		time.sleep(2)


```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
