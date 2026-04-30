# 逆转裁判 · TrialsAndTribulations（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：逆转裁判, AVG, 对话语料, PC RPG, 角色对话
> 游戏类型：AVG

## 概述
逆转裁判系列《TrialsAndTribulations》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：逆转裁判（AceAttorney）
- **游戏**：TrialsAndTribulations
- **品类**：AVG
- **说明**：Capcom法庭推理AVG

### 元数据 (meta.json)

```json
{
  "game": "Phoenix Wright: Ace Attorney – Trials and Tribulations",
  "series": "Ace Attorney",
  "year": 2004,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "https://aceattorney.fandom.com",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "characterInfoSource": "https://aceattorney.fandom.com/wiki/",
  "parserParameters": {
    "parser": "AceAttorneyParser",
    "fileType": ".html",
    "replaces": [
      [
        "The time is 1:",
        "The time is 1-"
      ],
      [
        "M-M-M-M-M-M-M-M-M-M-M-M-M-M-M-Miles",
        "M-M-M-M-M-M-M-M -M-M-M-M-M-M-M-Miles"
      ],
      [
        "Name:",
        "Name - "
      ],
      [
        "Sogoon!Desecrateme!Commemorateme!ThereisnothingthegreatAceDetectivecannothandle!Blackmail!Murder!Threats!I'llgetawaywithallofit!",
        "Sogoon!Desecrateme!Commemorateme! ThereisnothingthegreatAceDetectivecannothandle!Blackmail!Murder!Threats!I'llgetawaywithallofit!"
      ],
      [
        "Gwoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar!",
        "Gwoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar!"
      ],
      [
        "Gwoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar!",
        "Gwoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar!"
      ],
      [
        "Noooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo!",
        "Noooooooooooooooooooooooooooooooooooooooooooooooooooo oooooooooooooooooooooooooooooooooooooooooooooooooo!"
      ],
      [
        "Gwoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "Gwoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      ],
      [
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
      ]
    ]
  },
  "mainPlayerCharacters": [
    "Phoenix"
  ],
  "characterGroups": {
    "male": [
      "Phoenix",
      "Grossberg",
      "Swallow",
      "Judge",
      "Payne",
      "Gumshoe",
      "DeMasque",
      "Ron",
      "Butz",
      "Godot",
      "Atmey",
      "Armstrong",
      "Kudo",
      "Tigre",
      "The Tiger",
      "Fawles",
      "Armando",
      "Edgeworth",
      "Old Man",
      "Chief",
      "Detective",
      "Bailiff",
      "Officer",
      "Programmer"
    ],
    "female": [
      "Mia",
      "Dahlia",
      "Maya",
      "Pearl",
      "Andrews",
      "Desirée",
      "Byrde",
      "Basil",
      "Violetta",
      "Viola",
      "Valerie",
      "Melissa",
      "Bikini",
      "Elise",
      "Iris",
      "Franziska",
      "Morgan",
      "Oldbag"
    ],
    "neutral": [
      "Buzzer",
      "Phone",
      "Charge",
      "Announcer",
      "Ray Gun",
      "???"
    ],
    "lawyer": [
      "Payne",
      "Phoenix"
```

### 角色列表（共45个）

- "Phoenix" :6906,
- "ACTION" :2751,
- "Maya" :2251,
- "Judge" :2144,
- "Godot" :1415,
- "Edgeworth" :1391,
- "Mia" :1240,
- "Gumshoe" :1110,
- "Butz" :589,
- "Iris" :587,
- "CHOICE" :559,
- "Dahlia" :498,
- "Franziska" :400,
- "Bikini" :389,
- "Pearl" :369,
- "Atmey" :345,
- "Armstrong" :315,
- "Kudo" :310,
- "Ron" :301,
- "Payne" :216,
- "Andrews" :208,
- "Tigre" :204,
- "Byrde" :178,
- "???" :151,
- "Desirée" :149,
- "Basil" :109,
- "Viola" :89,
- "Grossberg" :87,
- "Fawles" :85,
- "Misty" :32,
- "LOCATION" :27,
- "Chief" :24,
- "Phone" :14,
- "Detective" :11,
- "Programmer" :9,
- "Bailiff" :5,
- "Morgan" :3,
- "Officer" :3,
- "Buzzer" :2,
- "Announcer" :2,
- "Swallow" :2,
- "Ray Gun" :1,
- "Oldbag" :1,
- "Valerie" :1,
- "Charge" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,TOTAL,19935,251941,86553,304787,-0.17966219915520654,101.53519655984907,6.667990143019635,42
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,male,13521,173457,57873,211017,-0.06594546858570993,100.87374196326554,6.74677043297414,20
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,female,6216,76539,27581,91481,-0.4041209099501426,102.90263715670926,6.474817137594575,15
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,neutral,166,1483,937,1750,-1.0482653855038695,105.39712576759302,7.792932326523798,6
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,lawyer,9449,111663,38093,136466,-0.0257230775005155,100.46803815011573,6.589259412725933,7
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,prosecutor,3217,43871,14806,54357,0.18601516642743476,99.0064961646393,6.569599394773977,4
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,defence attorney,6232,67792,23286,82109,-0.16255859778006077,101.41337029585281,6.602006262517511,3
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,assistant,3323,36700,12359,43576,-0.4210846044747143,103.37056382721902,6.634161656730426,3
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,culprit,2460,38396,13010,47047,0.01965177131008744,100.17824280224235,6.603171998071154,4
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,defendant,6311,70265,25731,84378,-0.3549302721726324,102.47104511703219,6.550392075659333,5
../data/AceAttorney/TrialsAndTribulations/,True,Phoenix Wright: Ace Attorney – Trials and Tribulations,Ace Attorney,victim,35,527,176,611,-0.7413809944799024,105.7111370644299,5.732551388649301,3

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re,time
import os


def openPage(url):
	req = Request(
		url, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)
	html = urlopen(req).read().decode('utf-8')
	html = BeautifulSoup(html, 'lxml')
	html = html.find("div",{"id":"mw-content-text"})
	return(html)
	
# In order
pages = [
	"https://aceattorney.fandom.com/wiki/Turnabout_Memories_-_Transcript",
	
	"https://aceattorney.fandom.com/wiki/The_Stolen_Turnabout_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/The_Stolen_Turnabout_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/The_Stolen_Turnabout_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/The_Stolen_Turnabout_-_Transcript_-_Part_4",
	
	"https://aceattorney.fandom.com/wiki/Recipe_for_Turnabout_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Recipe_for_Turnabout_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Recipe_for_Turnabout_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Recipe_for_Turnabout_-_Transcript_-_Part_4",
	
	"https://aceattorney.fandom.com/wiki/Turnabout_Beginnings_-_Transcript",
	
	"https://aceattorney.fandom.com/wiki/Bridge_to_the_Turnabout_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Bridge_to_the_Turnabout_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Bridge_to_the_Turnabout_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Bridge_to_the_Turnabout_-_Transcript_-_Part_4"
]

pageNum = 0
for page in pages:
	print(page)
	pageNum += 1
	fname = "raw/p" + f"{pageNum:02d}" + "_" + page[page.rindex("/")+1:] + ".html"
	fname = fname.replace(",","")
	if not os.path.isfile(fname):
		html = openPage(page)
		o = open(fname, "w")
		o.write(str(html))
		o.close()
		time.sleep(2)
```


## 策划参考价值
AVG类型的对话叙事参考。Capcom法庭推理AVG
