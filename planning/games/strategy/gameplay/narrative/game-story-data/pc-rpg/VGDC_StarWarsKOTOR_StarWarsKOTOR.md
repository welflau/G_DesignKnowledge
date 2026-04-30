# 星球大战旧共和国 · StarWarsKOTOR（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：星球大战旧共和国, CRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：CRPG

## 概述
星球大战旧共和国系列《StarWarsKOTOR》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：星球大战旧共和国（StarWarsKOTOR）
- **游戏**：StarWarsKOTOR
- **品类**：CRPG
- **说明**：BioWare星战CRPG，光明/黑暗面

### 元数据 (meta.json)

```json
{
  "game": "Star Wars: Knights of the Old Republic",
  "series": "Star Wars: Knights of the Old Republic",
  "year": 2003,
  "status": "ready",
  "source": "https://github.com/hmi-utwente/video-game-text-corpora/blob/master/Star%20Wars:%20Knights%20of%20the%20Old%20Republic/data/dataset_20200716.csv",
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
    "falsePositive_notes": "Data extracted from game code"
  },
  "characterInfoSource": "https://starwars.fandom.com/wiki/",
  "parserParameters": {
    "parser": "KOTORParser",
    "fileType": ".csv",
    "IDToCharName": {
      "Hidden Bek (Orange Twi'lek male)": [
        "8013"
      ],
      "Hidden Bek (Aqualish)": [
        "12908"
      ],
      "Female Jedi": [
        "8715",
        "8720",
        "8722"
      ],
      "Male Jedi": [
        "11704",
        "11708",
        "11710"
      ],
      "Upper City Man 2": [
        "14446",
        "14447",
        "14448",
        "14449"
      ],
      "North Apartments Man": [
        "18909",
        "18910",
        "18911",
        "18912",
        "18913"
      ],
      "Southwest Apartment Man": [
        "22565",
        "22566",
        "22567",
        "22568",
        "22569"
      ],
      "Prospective Sith (Human Male)": [
        "12655",
        "12656",
        "12657",
        "12659",
        "12660",
        "12661"
      ],
      "Prospective Sith (Twi'lek southeast corner)": [
        "9646",
        "9647",
        "9648",
        "9650",
        "9651",
        "9652"
      ],
      "Female Sith Soldier (Swoop Registration)": [
        "13958"
      ],
      "Male Sith Soldier (Swoop Registration)": [
        "23627"
      ],
      "Male Sith Teacher": [
        "16206"
      ],
      "Female Sith Teacher": [
        "5317"
      ],
      "Female Human Swoop Fan": [
        "23378",
        "23379",
        "23380",
        "23381",
        "23382",
        "23383",
        "23384",
        "23385",
        "23386",
        "23387",
        "23388",
        "23389",
        "23390",
        "23391",
        "23392",
        "23393",
        "23394",
        "23395",
        "23396",
        "23397",
        "23398",
        "23399",
        "23400",
        "23401",
        "23402",
        "23403",
        "23404"
      ],
      "Male Human Swoop Fan": [
        "19747",
        "19748",
        "19749",
        "19750",
        "19751",
        "19752",
        "19753",
        "19754",
        "19755",
        "19756",
        "19757",
        "19758",
        "19759",
        "19760",
        "19761",
        "19762",
        "19763",
        "19764",
        "19765",
        "19766",
        "19767",
        "19768",
        "19769",
        "19770",
        "19771",
        "19772",
        "19773"
      ],
      "Alien Swoop Fan": [
        "4802",
        "4803",
        "4804",
        "4805",
        "4806",
        "4807",
        "4808",
        "4809",
        "4810",
        "4811",
        "4812",
        "4813",
        "4814",
        "4815",
        "4816",
        "4817",
        "4818",
        "4819",
        "4820",
        "4821",
        "4822",
        "4823",
        "4824",
        "4825"
      ],
      "Southwest Apartment Woman": [
        "12649",
        "12650",
        "12651",
        "12652",
        "12653"
      ],
      "North Apartments Woman": [
        "12662",
        "12663",
        "12664",
        "12665"
      ],
      "Upper City Woman 2": [
        "13486",
        "13487",
        "13488",
        "13489",
        "13490"
      ],
      "Male Citizen (Korriban)": [
        "12553",
        "12549",
        "12548",
        "12547"
      ],
      "Twi'lek Female Citizen": [
        "16211",
        "16212",
        "16213",
        "16217"
      ],
      "Female Generic Duel Spectator": [
        "18547"
      ],
      "Male Generic Duel Spectator": [
        "1253"
      ],
      "Unknown Hidden Bek": [
        "20246"
      ],
      "Helmeted Republic Soldier 1": [
        "13586"
      ],
      "Helmeted Republic Soldier 2": [
        "13876"
      ],
      "Female Slaves": [
        "7617",
        "7619",
        "7621",
        "7622",
        "7623",
        "7624",
        "7626",
        "7627",
        "7631",
        "7637",
        "7640",
        "7648",
        "7651",
        "7653"
      ],
      "Male Slave 1": [
        "19335",
        "19337",
        "19339",
        "19340",
        "19341",
        "19342",
        "19344",
        "19345",
        "19349",
        "19356",
        "19358",
        "19365",
        "19368",
        "19370"
      ],
      "Child (Southwest)":
```

### 角色列表（共646个）

- "GOTO" :17856,
- "Revan" :9332,
- "CHOICE" :7932,
- "ACTION" :5375,
- "SYSTEM" :1183,
- "Bastila" :1045,
- "Carth" :922,
- "Juhani" :754,
- "Jolee" :663,
- "HK-47" :418,
- "Canderous" :415,
- "Mission" :384,
- "Yuthura Ban" :339,
- "Zaalbar" :261,
- "Suvam Tan" :189,
- "Judge Shelkar" :184,
- "Hulas" :180,
- "Uthar Wynn" :170,
- "Komad Fortuna" :152,
- "Darth Malak" :150,
- "Tanis Venn" :145,
- "Motta the Hutt" :141,
- "Vandar Tokare" :137,
- "Roland Wann" :128,
- "Dorak Quinn" :125,
- "Freyyr" :113,
- "Computer" :111,
- "Elder Councillor" :111,
- "Janos Wertka" :101,
- "Trask" :96,
- "Loremaster Gjarshi" :96,
- "Chuundar" :94,
- "Lashowe" :93,
- "Zhar Lestin" :91,
- "The Imprisoned One" :87,
- "Zax" :87,
- "Protocol Officer" :86,
- "Rahasia Sandral" :86,
- "Vrook Lamar" :83,
- "Zelka Forn" :82,
- "Ahlan Matale" :80,
- "Sunry" :80,
- "Queedle" :79,
- "Yuka Laka" :76,
- "Jorak Uln" :75,
- "Shaardan" :73,
- "The One" :71,
- "Gadon Thek" :71,
- "Sasha" :70,
- "Sslamoth" :70,
- ... 共646个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/StarWarsKOTOR/StarWarsKOTOR/,False,Star Wars: Knights of the Old Republic,Star Wars: Knights of the Old Republic,TOTAL,27829,439667,86465,533550,0.712794360508429,99.00900110198099,6.540819141939428,642
../data/StarWarsKOTOR/StarWarsKOTOR/,False,Star Wars: Knights of the Old Republic,Star Wars: Knights of the Old Republic,playerChoice,9330,65510,18058,78087,-0.10974126062260225,102.31081675661723,6.52129666994759,1
../data/StarWarsKOTOR/StarWarsKOTOR/,False,Star Wars: Knights of the Old Republic,Star Wars: Knights of the Old Republic,male,12787,258877,46745,317269,1.0314411170196678,97.53158150463635,6.597068545003648,461
../data/StarWarsKOTOR/StarWarsKOTOR/,False,Star Wars: Knights of the Old Republic,Star Wars: Knights of the Old Republic,female,5050,103678,19371,123211,0.5204961222384412,100.86379615397333,6.2854414256785995,98
../data/StarWarsKOTOR/StarWarsKOTOR/,False,Star Wars: Knights of the Old Republic,Star Wars: Knights of the Old Republic,undefined,0,NA,NA,NA,NA,NA,NA,0
../data/StarWarsKOTOR/StarWarsKOTOR/,False,Star Wars: Knights of the Old Republic,Star Wars: Knights of the Old Republic,neutral,662,11602,2288,14983,1.6263138604629308,92.43440162610621,7.889270291835384,82

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

page = "https://github.com/hmi-utwente/video-game-text-corpora/raw/master/Star%20Wars:%20Knights%20of%20the%20Old%20Republic/data/dataset_20200716.csv"

fileName = "raw/dataset_20200716.csv"
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
CRPG类型的对话叙事参考。BioWare星战CRPG，光明/黑暗面
