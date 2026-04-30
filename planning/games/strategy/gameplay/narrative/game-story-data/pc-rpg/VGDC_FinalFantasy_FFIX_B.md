# 最终幻想 · FFIX_B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFIX_B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFIX_B
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy IX",
  "series": "Final Fantasy",
  "year": 2000,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/ps/197338-final-fantasy-ix/faqs/42207",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "FF9BParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Zidane",
    "Vivi",
    "Steiner",
    "Garnet",
    "Amarant",
    "Freya",
    "Quina",
    "Eiko"
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
      "Blutzen, Pluto Knight II",
      "Bunce",
      "Cinna",
      "Engineer Zebolt",
      "Fratley",
      "Garland",
      "Haagen, Pluto Knight VIII",
      "Kohel, Pluto Knight III",
      "Weimar, Pluto Knight VII",
      "Harold Pathknower",
      "Innkeeper Hal",
      "King of Burmecia",
      "Kuja",
      "Marcus",
      "Mene",
      "Minister Artania",
      "Morrid",
      "Phillipo",
      "Ramuh",
      "Steiner",
      "Stiltzkin",
      "Thorn",
      "Tot",
      "Vivi",
      "Zenero",
      "Zorn",
      "Moguta",
      "Choco",
      "Kupo",
      "Kuppo",
      "Lich",
      "Moco",
      "Atla",
      "Grimo",
      "Gumo",
      "Kumool",
      "Kumop",
      "Mochos",
      "Mogki",
      "Mogmatt",
      "Mogrich",
      "Mogryo",
      "Mois",
      "Mojito",
      "Chimomo",
      "Momatose",
      "Mocha",
      "Monev",
      "Monty",
      "Moodon",
      "Moonte",
      "Moorock",
      "Morrison",
      "Mopli",
      "Mosco",
      "Mosh",
      "Noggy",
      "Artemecion",
      "Ashley",
      "Aspiring Artist Michael",
      "Bishop",
      "Black Mage 1",
      "Black Mage 2",
      "Black Mage 3",
      "Black Mage Crewmember",
      "Black Mage No. 234",
      "Black Mage No. 163",
      "Black Mage No. 111",
      "Black Mage No. 12",
      "Black Mage No. 123",
      "Black Mage No. 144",
      "Black Mage No. 189",
      "Black Mage No. 192",
      "Black Mage No. 199",
      "Black Mage No. 239",
      "Black Mage No. 24",
      "Black Mage No. 288",
      "Black Mage No. 32",
      "Black Mage No. 33",
      "Black Mage No. 44",
      "Black Mage No. 55",
      "Black Mage No. 56",
      "Black Mage No. 69",
      "Black Mage No. 78",
      "Black Mage No. 87",
      "Black Waltz No. 1",
      "Black Waltz No. 2",
      "Black Waltz No. 3",
      "Blutzen, Pluto Knight II",
      "Boatman",
      "Bobo",
      "Breireicht, Pluto Knight VI",
      "Bryan Rootrunner",
      "Burmecian Kid Adam",
      "Burmecian Kid Jack",
      "Burmecian Soldier Dan",
      "Burmecian Soldier Din",
      "Burmecian Soldier Doyle",
      "Burmecian Soldier Gary",
      "Burmecian Soldier Gidd",
      "Burmecian Soldier Gray",
      "Card Boy",
      "Chief Engineer",
      "Cid",
      "Craftsman",
      "Cymbalist",
      "Violinist",
      "Trumpeter",
      "Drummer",
      "Dante the Signmaker",
      "David Heavenguard",
      "Dead Man",
      "Derek Stonehammer",
      "Devon",
      "Dishmeister",
      "Dojebon, Pluto Knight V",
      "Dolf",
      "Doug",
      "Dragoos",
      "Earth Guard",
      "Eggmeister",
      "Engineer Gabin",
      "Fat Chocobo",
      "Father",
      "Gilgamesh",
      "Gatz",
      "Genero",
      "Geoffrey Treefeller",
      "Grandpa",
      "Granin Miller",
      "Gus",
      "Guy Doing Research",
      "Haagen, Pluto Knight VIII",
      "Hades",
      "Herald",
      "Hippaul",
      "Honorable Lord",
      "Hunk",
      "Jacob",
      "Jinkus Emptybottle",
      "Olivier",
      "Jobless Jeff",
      "John Fruitbringer",
      "Justin",
      "Kal",
      "Laudo, Pluto Knight IV",
      "Locke",
      "Lowell",
      "Ludruff",
      "Male Red Mage",
      "Marco",
      "Mario",
      "Marolo",
      "Matthew Watchman",
      "Mayor Kapu",
      "Mayor's Son",
      "Meltigemini",
      "Nikolai",
      "Mick",
      "Moggy",
      "Mogreg",
      "Mogriffin",
      "Mogster",
      "Moss",
      "Naked Soldier",
      "Nimitz",
      "Noble Lord",
      "Old Man with a Cane",
      "Old Pops",
      "Onionmeister",
      "Ovenmeister",
      "Pasty Yacha",
      "Pigeon Lover",
      "Policeman",
      "Priest Theodore",
      "Quan",
      "Retired Boatman",
      "Richard Watchman",
      "Rio",
      "Robert Dogherder",
      "Rosco",
      "Rupta",
      "Ryan",
      "Shamis Gatekeeper",
      "Shig",
      "Silly Old Man",
      "Slai's Father",
      "Sleepy Soldier",
      "Snot-nosed Gudo",
      "Son",
      "Staff",
      "Stubborn Geezer",
      "Synthesist",
      "T
```

### 角色列表（共530个）

- "ACTION" :2914,
- "Zidane" :2043,
- "Garnet" :811,
- "LOCATION" :563,
- "Steiner" :509,
- "Vivi" :466,
- "Eiko" :431,
- "CHOICE" :296,
- "Freya" :246,
- "Cid" :187,
- "Quina" :178,
- "Amarant" :172,
- "Marcus" :157,
- "SYSTEM" :156,
- "Blank" :145,
- "Kuja" :119,
- "Tot" :118,
- "Baku" :117,
- "Beatrix" :99,
- "Zorn" :99,
- "Soldier" :93,
- "Thorn" :93,
- "Alexandrian Soldier" :89,
- "Cinna" :88,
- "Garland" :76,
- "Mene" :52,
- "Mogster" :50,
- "Mikoto" :49,
- "Brahne" :49,
- "Puck" :49,
- "Black Mage No. 288" :45,
- "Lani" :42,
- "Narrative" :42,
- "Kupo" :42,
- "Stiltzkin" :40,
- "Morrison" :37,
- "Minister Artania" :37,
- "Mog" :36,
- "Gilgamesh" :35,
- "Moguta" :35,
- "Hilda" :32,
- "Attendant" :32,
- "Hippaul" :30,
- "Mogki" :29,
- "Ramuh" :27,
- "Zenero" :27,
- "Ruby" :27,
- "Black Mage" :25,
- "Mosco" :25,
- "Mosh" :24,
- ... 共530个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFIX_B/,False,Final Fantasy IX,Final Fantasy,TOTAL,9579,99245,33791,117875,-0.4294966547312349,103.37303932979337,6.563106545140411,525
../data/FinalFantasy/FFIX_B/,False,Final Fantasy IX,Final Fantasy,male,6700,70452,23526,83526,-0.43232550981006135,103.4959470994398,6.581432326569315,350
../data/FinalFantasy/FFIX_B/,False,Final Fantasy IX,Final Fantasy,female,2475,24977,8820,29662,-0.4722185421472087,103.49202355039654,6.49218022915958,127
../data/FinalFantasy/FFIX_B/,False,Final Fantasy IX,Final Fantasy,genderless,200,1858,712,2199,-0.606613278746023,104.05961080840824,5.729060726164415,2
../data/FinalFantasy/FFIX_B/,False,Final Fantasy IX,Final Fantasy,neutral,204,1958,731,2488,0.44869939034359163,96.61640173464929,7.607985975946309,46

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *


page = "https://gamefaqs.gamespot.com/ps/197338-final-fantasy-ix/faqs/42207"

req = Request(
    page, 
    headers={
        'User-Agent': 'XYZ/3.0'
    }
)

html = urlopen(req, timeout=10).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()



```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
