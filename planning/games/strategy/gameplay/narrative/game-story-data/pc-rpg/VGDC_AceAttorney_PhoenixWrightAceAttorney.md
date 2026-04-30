# 逆转裁判 · PhoenixWrightAceAttorney（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：逆转裁判, AVG, 对话语料, PC RPG, 角色对话
> 游戏类型：AVG

## 概述
逆转裁判系列《PhoenixWrightAceAttorney》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：逆转裁判（AceAttorney）
- **游戏**：PhoenixWrightAceAttorney
- **品类**：AVG
- **说明**：Capcom法庭推理AVG

### 元数据 (meta.json)

```json
{
  "game": "Phoenix Wright: Ace Attoreny",
  "series": "Ace Attorney",
  "year": 2001,
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
        "Unrelated evidence:",
        "Unrelated evidence - "
      ],
      [
        "Alarm Clock:",
        "Alarm Clock - "
      ]
    ]
  },
  "mainPlayerCharacters": [
    "Phoenix"
  ],
  "characterGroups": {
    "male": [
      "Phoenix",
      "Edgeworth",
      "Judge",
      "Gumshoe",
      "Butz",
      "Payne",
      "Sawhit",
      "Grossberg",
      "Bellboy",
      "White",
      "Will",
      "Cody",
      "Manella",
      "Manfred",
      "Uncle",
      "Yogi",
      "Goodman",
      "Gant",
      "Chief",
      "Meekins",
      "Marshall",
      "Officer",
      "Patrolman",
      "Guard",
      "Sahwit"
    ],
    "female": [
      "Maya",
      "Ema",
      "Mia",
      "April",
      "Penny",
      "Oldbag",
      "Vasquez",
      "Lotta",
      "Lana",
      "Angel"
    ],
    "neutral": [
      "TV",
      "Parrot",
      "Missile",
      "Cellular",
      "Interphone",
      "Teacher"
    ],
    "lawyer": [
      "Payne",
      "Phoenix",
      "Edgeworth",
      "Mia",
      "Manfred",
      "Grossberg"
    ],
    "prosecutor": [
      "Payne",
      "Edgeworth",
      "Manfred"
    ],
    "defence attorney": [
      "Phoenix",
      "Mia",
      "Grossberg"
    ],
    "assistant": [
      "Maya",
      "Ema",
      "Mia",
      "Grossberg",
      "Gumshoe"
    ],
    "culprit": [
      "Sawhit",
      "White",
      "Vasquez",
      "Manfred",
      "Gant",
      "Yogi"
    ],
    "defendant": [
      "Butz",
      "Maya",
      "Will",
      "Edgeworth",
      "Yogi",
      "Lana"
    ],
    "victim": [
      "Mia",
      "Goodman"
    ]
  },
  "aliases": {
    "von Karma": "Manfred",
    "Karma": "Manfred",
    "Uncle": "Yogi",
    "Meg": "Mia"
  }
}
```

### 角色列表（共45个）

- "Phoenix" :7668,
- "ACTION" :3133,
- "Judge" :1757,
- "Edgeworth" :1539,
- "Maya" :1508,
- "Ema" :1399,
- "Gumshoe" :767,
- "CHOICE" :694,
- "Manfred" :402,
- "Gant" :345,
- "Angel" :329,
- "Marshall" :320,
- "Lana" :293,
- "Oldbag" :246,
- "Lotta" :215,
- "Mia" :200,
- "Grossberg" :197,
- "Butz" :194,
- "White" :186,
- "Vasquez" :179,
- "April" :167,
- "Cody" :159,
- "Meekins" :158,
- "???" :131,
- "Yogi" :118,
- "Penny" :95,
- "Will" :88,
- "Bellboy" :68,
- "Sahwit" :62,
- "Manella" :59,
- "Payne" :52,
- "Police" :38,
- "Parrot" :31,
- "LOCATION" :31,
- "Chief" :28,
- "Cellular" :15,
- "Officer" :8,
- "Interphone" :8,
- "Missile" :7,
- "Teacher" :5,
- "Guard" :5,
- "Patrolman" :4,
- "TV" :4,
- "Goodman" :2,
- "Meg" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,TOTAL,17218,199993,63003,244652,0.08296617677937945,100.12162578239564,6.621798433647675,42
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,male,12371,143723,44291,177092,0.21521283147107262,99.29928347060455,6.634691283684853,23
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,female,4626,53804,17831,64642,-0.2362667183906737,102.13090958512457,6.56006815564146,11
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,neutral,56,414,225,514,-0.2221584541062782,99.93261739130436,9.219937913043479,6
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,lawyer,8244,87120,27332,107724,0.24383055170197743,98.9916988230428,6.633971228489679,6
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,prosecutor,1992,24839,7107,32009,0.9792276926131187,94.2670216701538,6.915216791953321,3
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,defence attorney,6252,62281,20224,75715,-0.04371423017678033,100.8610435688369,6.5225354090746634,3
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,assistant,3301,34806,12306,41539,-0.40429802547255456,102.99886438903968,6.604434139641407,4
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,culprit,1110,14715,4307,18382,0.48302482087296106,97.68477432016297,6.684965725338983,4
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,defendant,3737,42954,13981,52845,0.12538301591611223,99.63579551430419,6.788523517015625,6
../data/AceAttorney/PhoenixWrightAceAttorney/,True,Phoenix Wright: Ace Attoreny,Ace Attorney,victim,201,2979,803,3523,-0.18834608552938015,103.02057172310784,6.364717436375926,2

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
pages = ["https://aceattorney.fandom.com/wiki/The_First_Turnabout_-_Transcript",

	"https://aceattorney.fandom.com/wiki/Turnabout_Sisters_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Turnabout_Sisters_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Turnabout_Sisters_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Turnabout_Sisters_-_Transcript_-_Part_4",
	
	"https://aceattorney.fandom.com/wiki/Turnabout_Samurai_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Turnabout_Samurai_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Turnabout_Samurai_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Turnabout_Samurai_-_Transcript_-_Part_4",
	"https://aceattorney.fandom.com/wiki/Turnabout_Samurai_-_Transcript_-_Part_5",
	"https://aceattorney.fandom.com/wiki/Turnabout_Samurai_-_Transcript_-_Part_6",
	
	"https://aceattorney.fandom.com/wiki/Turnabout_Goodbyes_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Turnabout_Goodbyes_-_Transcript_-_Part_2",
	"https://aceattorney.fandom.com/wiki/Turnabout_Goodbyes_-_Transcript_-_Part_3",
	"https://aceattorney.fandom.com/wiki/Turnabout_Goodbyes_-_Transcript_-_Part_4",
	"https://aceattorney.fandom.com/wiki/Turnabout_Goodbyes_-_Transcript_-_Part_5",
	"https://aceattorney.fandom.com/wiki/Turnabout_Goodbyes_-_Transcript_-_Part_6",
	
	"https://aceattorney.fandom.com/wiki/Rise_from_the_Ashes_-_Transcript_-_Part_1",
	"https://aceattorney.fandom.com/wiki/Rise_from_the
```


## 策划参考价值
AVG类型的对话叙事参考。Capcom法庭推理AVG
