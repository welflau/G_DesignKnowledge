# 女神异闻录 · Persona3（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：女神异闻录, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
女神异闻录系列《Persona3》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：女神异闻录（Persona）
- **游戏**：Persona3
- **品类**：JRPG
- **说明**：Atlus的社交模拟+JRPG，Confidant系统

### 元数据 (meta.json)

```json
{
  "game": "Persona 3",
  "series": "Persona",
  "year": 2006,
  "status": "ready",
  "source": "https://lparchive.org/Persona-3/",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "Screenshots in the source aren't transcribed, so some dialogue is missed.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "Persona3Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
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
      "Boy"
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
      "Other girl"
    ],
    "neutral": [
      "Athletes",
      "Kids",
      "PHIL"
    ]
  },
  "aliases": {
    "ken": "Ken",
    "(Note": "ACTION",
    "(note": "ACTION",
    "AKihiko": "Akihiko",
    "Ahikhiko": "Akihiko",
    "Akiihiko": "Akihiko",
    "AKinari": "Akinari",
    "Ekoda": "Mr. Ekoda",
    "Bukichi": "Bunkichi",
    "Ikutuski": "Ikutsuki",
    "Kaz": "Kazushi",
    "Kirijo-senpai": "Kouetsu Kirijo",
    "Mitusko": "Mitsuko",
    "Mistuko": "Mitsuko",
    "Posted by": "ACTION",
    "Shinijro": "Shinjiro",
    "Shinjir": "Shinjiro",
    "Yoshie": "Chidori",
    "Chidori Yoshino": "Chidori",
    "Bonus Video": "ACTION",
    "Glasses Guy": "Keisuke",
    "Foreigner": "Bebe",
    "Gourmet King": "Nozomi",
    "Gourmet King?": "Nozomi",
    "Lady": "Beautiful Lady",
    "Lady?": "Beautiful Lady",
    "Letter": "Eiichiro",
    "Note": "ACTION",
    "Scientist": "Eiichiro",
    "Server": "Ramen Shop Owner",
    "Smart Guy": "Jin",
    "Pale Man": "Takaya",
    "Some girl": "Listener",
    "Striped Shirt": "Akinari",
    "Old Man": "Bunkichi",
    "Old Woman": "Mitsuko",
    "Woman": "Maiko's Mom",
    "Girl A": "Listener",
    "Girl B": "Gossip",
    "Brunette": {
      "Natsuki": [
        "I-I never thought it'd turn out like this ... Fuuka ..."
      ],
      "Yukari": [
        "Who's he?",
        "... Is it okay for him to be here?"
      ]
    },
    "Listener": {
      "Male Listener": [
        "It's becaues the building wasn't built that long ago, so everything's still gleaming. You know, I heard from my parents there was an explosion here 10 years ago. They replaced the building after that, but ... there's more to it, too. Around that time, a lot of students stopped coming to school. Maybe that's why they put up the new building ... to start with a clean slate ..."
      ]
    },
    "Other Girl": {
      "Gossip": [
        "N-no! Not that one! I mean the story about the first-year student! Not only did she stop coming to school, she does nothing but sit and stare at the walls all day. If her mother tries to talk to her, she only mutters to herself, \"It's coming! It's coming!\"",
        "You don't believe me ... ?"
      ]
    },
    "Senior": {
      "Senior (Front)": [
        "Huh? ... what're you doing?"
      ]
    },
    "Student": {
      "Female Student": [
        "Yeah, I've had enough of this. I just wanna get accepted to college and start having some fun.",
        "Next, we
```

### 角色列表（共92个）

- "ACTION" :8626,
- "Junpei" :381,
- "Yukari" :373,
- "Mitsuru" :303,
- "Akihiko" :240,
- "Fuuka" :183,
- "Ikutsuki" :92,
- "Shinjiro" :66,
- "Aigis" :65,
- "Ken" :56,
- "Chidori" :53,
- "Maya" :50,
- "Takaya" :46,
- "Akinari" :45,
- "Yuko" :45,
- "Chihiro" :43,
- "Bunkichi" :40,
- "Tanaka" :37,
- "Mutatsu" :35,
- "Pharos" :33,
- "Mamoru" :32,
- "Bebe" :32,
- "Kenji" :32,
- "Maiko" :31,
- "Natsuki" :28,
- "Ryoji" :26,
- "Jin" :21,
- "Mr. Edogawa" :19,
- "Nozomi" :18,
- "Takeharu" :16,
- "Mitsuko" :16,
- "Kazushi" :15,
- "Listener" :15,
- "Igor" :12,
- "Beautiful Lady" :11,
- "Gossip" :11,
- "Ms. Toriumi" :11,
- "Punk" :10,
- "Eiichiro" :9,
- "Monk" :7,
- "Nobuko" :6,
- "Keisuke" :6,
- "Teenager" :6,
- "Mr. Ekoda" :6,
- "Female Student" :6,
- "Male Student" :5,
- "Maiko's Dad" :4,
- "Maiko's Mom" :4,
- "Black-Socked Girl" :4,
- "Ramen Shop Owner" :4,
- ... 共92个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Persona/Persona3/,False,Persona 3,Persona,TOTAL,2685,44447,12334,53645,0.05733883720082211,101.06994341364674,6.444123193808727,91
../data/Persona/Persona3/,False,Persona 3,Persona,male,1391,25287,6666,30471,0.10851443982931919,101.04111719414321,6.4491397995262805,49
../data/Persona/Persona3/,False,Persona 3,Persona,female,1289,19098,5656,23089,-0.007227231374004717,101.12849505650378,6.436472379847382,39
../data/Persona/Persona3/,False,Persona 3,Persona,neutral,5,62,11,85,2.7856011730205275,85.130219941349,7.226870087976539,3

```


### 数据来源脚本 (scraper.py)

```python
import re, time, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

indexPage = "https://lparchive.org/Persona-3/"

html = urlopen(indexPage).read().decode('utf-8')
time.sleep(3)
pageLinks = re.findall('HREF="(Update.+?)"',html)


pageLinksUnique = []
for p in pageLinks:
	if not p in pageLinksUnique:
		pageLinksUnique.append(p)



pageNum = 1
for pageLink in pageLinksUnique:
	filename = "raw/page" + str(pageNum).zfill(3)+".html"
	if not os.path.isfile(filename):
		url = indexPage+pageLink
		html = urlopen(url).read().decode('utf-8')
		time.sleep(2)
	
		soup = BeautifulSoup( html, "html5lib")
		cont = soup.find("div",{"id":"content"})
		towrite = pageLink + "\n" + str(cont)
	
		o = open(filename,'w')
		o.write(towrite)
		o.close()
	pageNum += 1

```


## 策划参考价值
JRPG类型的对话叙事参考。Atlus的社交模拟+JRPG，Confidant系统
