# 逆转裁判 · JusticeForAll（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：逆转裁判, AVG, 对话语料, PC RPG, 角色对话
> 游戏类型：AVG

## 概述
逆转裁判系列《JusticeForAll》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：逆转裁判（AceAttorney）
- **游戏**：JusticeForAll
- **品类**：AVG
- **说明**：Capcom法庭推理AVG

### 元数据 (meta.json)

```json
{
  "game": "Phoenix Wright: Ace Attorney – Justice for All",
  "series": "Ace Attorney",
  "year": 2002,
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
        "AhahahahahahaaahahaahahaahahahahahaHahahaAhahahahahaHahahaHahhaahaAAAHAHAhhahahahahAHAHAHAHAHAHAHAHAHAWAHAHAHAHAHAWAHAHAHAHAWAHAAHAHAHWAHAHAHAHAAAAAA",
        "Ahahahahahahaaahahaahahaahahahahaha HahahaAhahahahahaHahahaHahhaaha AAAHAHAhhahahahah AHAHAHAHAHAHAHAHAHAWAHAHAHAHAHAWAHAHAHAHAWAHAAHAHAHWAHAHAHAHAAAAAA"
      ],
      [
        "AaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaagggggggghhhnn",
        "Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaagggggggghhhnn"
      ]
    ]
  },
  "mainPlayerCharacters": [
    "Phoenix"
  ],
  "characterGroups": {
    "male": [
      "Phoenix",
      "Payne",
      "Judge",
      "Gumshoe",
      "Wellington",
      "Grey",
      "Hotti",
      "Max",
      "Russell",
      "Ben",
      "Moe",
      "Acro",
      "Bat",
      "Will",
      "Engarde",
      "Edgeworth",
      "Doe",
      "de Killer",
      "Bellboy",
      "Chief",
      "Detective",
      "Bailiff",
      "Jailer"
    ],
    "female": [
      "Maya",
      "Byrde",
      "Pearl",
      "Morgan",
      "Lotta",
      "Ini",
      "Mimi",
      "Mia",
      "Franziska",
      "Regina",
      "Oldbag",
      "Andrews",
      "Nurse"
    ],
    "neutral": [
      "TV",
      "Phone",
      "Shoe",
      "Money",
      "???",
      "Trilo",
      "Ray Gun",
      "PA Notice"
    ],
    "lawyer": [
      "Payne",
      "Phoenix",
      "Edgeworth",
      "Franziska",
      "Mia"
    ],
    "prosecutor": [
      "Payne",
      "Edgeworth",
      "Franziska"
    ],
    "defence attorney": [
      "Phoenix",
      "Mia"
    ],
    "assistant": [
      "Maya",
      "Mia",
      "Byrde",
      "Gumshoe",
      "Pearl"
    ],
    "culprit": [
      "Wellington",
      "Ini",
      "Mimi",
      "Acro",
      "Engarde",
      "de Killer"
    ],
    "defendant": [
      "Byrde",
      "Maya",
      "Max",
      "Engarde"
    ],
    "victim": [
      "Grey",
      "Russell"
    ]
  },
  "aliases": {
    "von Karma": "Franziska",
    "Ini": "Mimi",
    "Doe": "de Killer",
    "Powers": "Will"
  }
}
```

### 角色列表（共44个）

- "Phoenix" :7490,
- "ACTION" :2749,
- "Judge" :1647,
- "Maya" :1377,
- "Pearl" :891,
- "Franziska" :813,
- "Edgeworth" :790,
- "Gumshoe" :760,
- "CHOICE" :553,
- "Mia" :476,
- "Andrews" :452,
- "Moe" :360,
- "Mimi" :355,
- "Lotta" :294,
- "Will" :290,
- "Engarde" :282,
- "Oldbag" :268,
- "Acro" :248,
- "Max" :246,
- "de Killer" :202,
- "???" :187,
- "Morgan" :168,
- "Trilo" :164,
- "Regina" :160,
- "Payne" :121,
- "Wellington" :113,
- "Byrde" :96,
- "Hotti" :91,
- "Ben" :65,
- "Grey" :37,
- "Phone" :31,
- "LOCATION" :25,
- "Chief" :14,
- "Ray Gun" :14,
- "Detective" :8,
- "Money" :7,
- "Bailiff" :7,
- "Shoe" :6,
- "Jailer" :4,
- "Bellboy" :4,
- "Nurse" :4,
- "PA Notice" :2,
- "Russell" :2,
- "TV" :2

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,TOTAL,16686,196089,65822,236468,-0.19828157266201707,101.79024950903704,6.579031730097891,41
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,male,10929,125516,42489,152106,-0.13813100824041769,101.3144770838238,6.565859646929003,21
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,female,5354,65271,21449,78079,-0.2877084168508812,102.54538321756034,6.597273395913322,12
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,neutral,403,5302,1883,6283,-0.5085800326252894,103.7239702980849,6.667915633135163,8
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,lawyer,7838,82422,27318,100531,-0.020731760299133484,100.58508143657768,6.541382308989266,5
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,prosecutor,1723,22955,6507,29013,0.6999285651090972,96.32775775175953,6.818145007402346,3
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,defence attorney,6115,59467,20811,71518,-0.28431063464286055,102.19045088217263,6.436405923375247,2
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,assistant,1853,20121,6908,23787,-0.5041102324710831,103.86467370069592,6.6217735521145125,2
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,culprit,1200,17010,5406,20350,-0.24587347913775304,102.42965834551853,6.314696516249175,5
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,defendant,2001,22860,7988,26885,-0.596254307094938,104.43461112929239,6.707814558670902,4
../data/AceAttorney/JusticeForAll/,True,Phoenix Wright: Ace Attorney – Justice for All,Ace Attorney,victim,39,808,167,995,0.8278867018438394,97.74464635086264,6.260614501689689,2

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
	"https://aceattorney.fandom.com/wiki/The_Lost_Turnabout_-_Transcript",
	
	"https://aceattorney.fandom.com/wiki/Reunion,_and_Turnabout_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Reunion,_and_Turnabout_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Reunion,_and_Turnabout_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Reunion,_and_Turnabout_-_Transcript_-_Part_4",
	
	"https://aceattorney.fandom.com/wiki/Turnabout_Big_Top_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Turnabout_Big_Top_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Turnabout_Big_Top_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Turnabout_Big_Top_-_Transcript_-_Part_4",
	
	"https://aceattorney.fandom.com/wiki/Farewell,_My_Turnabout_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Farewell,_My_Turnabout_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Farewell,_My_Turnabout_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Farewell,_My_Turnabout_-_Transcript_-_Part_4"
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
