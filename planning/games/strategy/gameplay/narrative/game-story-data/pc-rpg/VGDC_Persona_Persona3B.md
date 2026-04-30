# 女神异闻录 · Persona3B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：女神异闻录, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
女神异闻录系列《Persona3B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：女神异闻录（Persona）
- **游戏**：Persona3B
- **品类**：JRPG
- **说明**：Atlus的社交模拟+JRPG，Confidant系统

### 元数据 (meta.json)

```json
{
  "game": "Persona 3",
  "series": "Persona",
  "year": 2006,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "https://gamefaqs.gamespot.com/ps2/932312-shin-megami-tensei-persona-3/faqs/50852",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {},
  "parserParameters": {
    "parser": "Persona3BParser",
    "fileType": ".txt"
  },
  "mainPlayerCharacters": [
    "Makoto",
    "Yukari",
    "Junpei",
    "Mitsuru",
    "Akihiko",
    "Fuuka",
    "Aigis",
    "Shinjiro",
    "Ken",
    "Koromaru"
  ],
  "characterGroups": {
    "male": [
      "Makoto",
      "Junpei",
      "Akihiko",
      "Ken",
      "Shinjiro",
      "Ikutsuki",
      "Mr. Edogawa",
      "Mr. Ekoda",
      "Bunkichi",
      "Eiichiro",
      "Hidetoshi",
      "Igor",
      "Jin",
      "Kazushi",
      "Keisuke",
      "Kenji",
      "Kouetsu Kirijo",
      "Koromaru",
      "Kurosawa",
      "Maiko's Dad",
      "Mamoru",
      "Mutatsu",
      "Nozomi",
      "Pharos",
      "Ryoji",
      "Takaya",
      "Takeharu",
      "Tanaka",
      "Akinari",
      "Bartender",
      "Bebe",
      "Punk",
      "Club Member",
      "Coach",
      "Creep",
      "Male Listener",
      "Guy",
      "Male Student",
      "Monk",
      "Principal",
      "Ramen Shop Owner",
      "Senior (Front)",
      "Senior (Side)",
      "Some Guy",
      "Student Council Member",
      "Suit",
      "Teacher",
      "Teenager",
      "Voice",
      "Boy",
      "Mr. Ono",
      "Mr. Takenozuka",
      "Male Junior",
      "Male Reporter",
      "Male Senior",
      "Male Student's Voice",
      "Male Studet",
      "Male Voice",
      "Man",
      "Man In Black",
      "Man With A Long Nose",
      "Orpheus",
      "Nervous Man",
      "Old Man",
      "Pale Young Man",
      "Salaryman",
      "Sophisticated Gentleman",
      "Stalked Boy",
      "Young Man's Voice",
      "Weather Man"
    ],
    "female": [
      "Yukari",
      "Mitsuru",
      "Fuuka",
      "Aigis",
      "Ms. Kanou",
      "Ms. Toriumi",
      "Chidori",
      "Chihiro",
      "Elizabeth",
      "Maiko",
      "Maiko's Mom",
      "Natsuki",
      "Yuko",
      "Mitsuko",
      "Nobuko",
      "Chick",
      "Classmate",
      "Female Student",
      "Listener",
      "Gossip",
      "Beautiful Lady",
      "Maya",
      "Other Girl",
      "Passerby",
      "Representative",
      "Student's Friend",
      "Zealot",
      "Zealot 2",
      "Black-Socked Girl",
      "White-Socked Girl",
      "Creepy Girl",
      "Nosy Girl",
      "Girl",
      "Female Student 2",
      "Squinty-eyed Student",
      "Girl in Orange",
      "Girl in Yellow",
      "Girls",
      "Other girl",
      "Mrs. Terauchi",
      "Ms. Miyahara",
      "Ms. Ounishi",
      "Ms. Terauchi",
      "Giddy Schoolgirl",
      "Girl In A Dress",
      "Girl In A White Dress",
      "Girl In Black",
      "Girl In Green",
      "Girl In Orange",
      "Girl In Yellow",
      "Gossiping Girls",
      "Mature Girl",
      "Female Reporter",
      "Female Teenager",
      "Female Voice",
      "Female Voices",
      "Complaining Girl",
      "Critical Woman",
      "Food Girl",
      "Fortune-Loving Girl",
      "Girlfriend",
      "Housewife With Braids",
      "Listening Girl",
      "Long-Haired Housewife",
      "Mysterious Girl",
      "Old Lady",
      "Old Lady's Voice",
      "Older Female Voice",
      "Patient Woman",
      "Short-Haired Housewife",
      "Stalker Girl",
      "Strange Girl",
      "Tough Chick",
      "Woman"
    ],
    "neutral": [
      "Athletes",
      "Kids",
      "PHIL"
    ]
  },
  "aliases": {
    "Main": "Makoto",
    "Antiques Onwer": "Antiques Owner",
    "Cat-Obessed Boy": "Cat-Obsessed Boy",
    "Complaing Girl": "Complaining Girl",
    "Fortune Teller": "Fortune-Teller",
    "Gossping Student": "Gossiping Student",
    "Houswife With Braids": "Housewife With Braids",
    "Mitsusu": "Mitsuru",
    "Mitsuu": "Mitsuru",
    "Movei-Loving Man": "Movie-Loving Man",
    "Mr Ekoda": "Mr. Ekoda",
    "Mr Ono": "Mr. Ono",
    "Shuji Ijutsuki": "Shuji Ikutsuki",
    "Shuji Iktsuki": "Shuji Ikutsuki",
    "Shuji Ikustuki": "Shuji Ikutsuki",
    "Shuji Ikutsuji": "Shuji Ikutsuki",
    "Shujki Ikutsuki": "Shuji Ikutsuki",
    "Station Attendent": "Station Attendant",
    "Student With Glassess": "Student With Glasses",
    "Vistor": "Visitor",
    "Fuuka Yamagishi": "Fuuka",
    "Fuka": "Fuuka",
    "Yukari Takeba": "Yukari",
    "Shinjiro Aragaki": "Shinjiro",
    "Shinriro": "Shinjiro",
    "Akihiko Sanada": "Akihiko",
    "Eiichiro Takeba": "Eiichiro",
    "Junpeu": "Junpei",
    "Kenji Tomochika": "Kenji",
    "Mamoru Hayase": "Mamoru",
    "Mitsuru Kirijo": "Mitsuru",
    "Officer Kurosawa": "Kurosawa",
    "Ryoji Mochizuki": "Ryoji",
    "Chidroi": "Chidori",
    "Takeharu Kirijo": "Takeharu",
    "Takata": "Takaya",
    "Natsuki Moriyama": "Natsuki",
  
```

### 角色列表（共196个）

- "LOCATION" :2128,
- "Makoto" :1496,
- "ACTION" :1492,
- "Junpei" :1255,
- "Yukari" :1125,
- "Mitsuru" :806,
- "Akihiko" :623,
- "Fuuka" :556,
- "Aigis" :361,
- "CHOICE" :322,
- "Ken" :252,
- "Shuji" :196,
- "Newscaster" :186,
- "Shinjiro" :142,
- "Female Student" :123,
- "Ryoji" :99,
- "Gossiping Student" :94,
- "Chidori" :89,
- "Takaya" :83,
- "Male Student" :72,
- "Elizabeth" :67,
- "Ms. Toriumi" :66,
- "Listening Student" :65,
- "Fortune-Teller" :61,
- "Pharos" :57,
- "Man" :51,
- "Koromaru" :45,
- "Jin" :42,
- "Narrator" :40,
- "Mysterious Boy" :40,
- "Snoopy Reporter" :39,
- "Natsuki" :38,
- "Mature Girl" :35,
- "Station Attendant" :34,
- "Fat Student" :33,
- "Mitsuru Admirer" :33,
- "Cell-Phone Student" :33,
- "Salaryman" :32,
- "Mr. Edogawa" :32,
- "Movie-Loving Man" :30,
- "Woman" :29,
- "Cat-Obsessed Boy" :29,
- "Complaining Girl" :29,
- "Igor" :29,
- "Gamer Student" :28,
- "Old Man" :27,
- "Taxi Driver" :26,
- "Mr. Ono" :25,
- "Short-Haired Housewife" :24,
- "Stalker Girl" :24,
- ... 共196个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Persona/Persona3B/,True,Persona 3,Persona,TOTAL,9592,153957,48326,188476,0.09816330802690132,100.03308096949306,6.481001287111457,193
../data/Persona/Persona3B/,True,Persona 3,Persona,male,4610,58862,20417,70681,-0.2962921800349889,102.32178917205468,6.578464382273509,54
../data/Persona/Persona3B/,True,Persona 3,Persona,female,3694,65719,20384,81080,0.22548226693597684,99.188391760519,6.336978840697357,57
../data/Persona/Persona3B/,True,Persona 3,Persona,neutral,0,NA,NA,NA,NA,NA,NA,0

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
	html = html.find("div",{"id":"faqtext"})
	return(html)
	

# page = "https://gamefaqs.gamespot.com/ps2/932312-shin-megami-tensei-persona-3/faqs/50852"
# 
# html = openPage(page)
# txt = html.get_text()
# 
# o = open("raw/p3.txt",'w')
# o.write(txt)
# o.close()

time.sleep(3)

page = "https://gamefaqs.gamespot.com/ps2/932312-shin-megami-tensei-persona-3/faqs/50317"

html = openPage(page)
txt = html.get_text()

o = open("raw/p3_SocialLinks.txt",'w')
o.write(txt)
o.close()
```


## 策划参考价值
JRPG类型的对话叙事参考。Atlus的社交模拟+JRPG，Confidant系统
