# 最终幻想 · FFVI_B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFVI_B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFVI_B
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy VI",
  "series": "Final Fantasy",
  "year": 1994,
  "status": "superseded",
  "alternativeMeasure": true,
  "source": "https://finalfantasy.fandom.com/wiki/Final_Fantasy_VI_SNES_script",
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "fandomParser",
    "fileType": ".html",
    "scriptStartCue": "<span class=\"mw-headline\" id=\"Story_Dialogue\">Story Dialogue</span>",
    "scriptEndCue": "<div class=\"printfooter\">",
    "scriptHasOptionalDialogueSection": true,
    "ignoreCharacters": []
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [
      "Arvis",
      "B.Day Suit",
      "Banon",
      "Baram",
      "Cid",
      "Clyde",
      "Curley",
      "Cyan",
      "Dadaluma",
      "Daryl",
      "Draco",
      "Duane",
      "Duncan",
      "Edgar",
      "Gestahl",
      "Gau",
      "Gerad",
      "Gestahl",
      "Gogo",
      "Gungho",
      "Kefka",
      "King Doma",
      "Larry",
      "Leo",
      "Locke",
      "Lone Wolf",
      "Maduin",
      "Moe",
      "Mog",
      "Rachel'S Dad",
      "Ralse",
      "Ramuh",
      "Sabin",
      "Setzer",
      "Shadow",
      "Sigfried",
      "Strago",
      "Umaro",
      "Vargas",
      "Vicks",
      "Wedge",
      "Yura"
    ],
    "female": [
      "Celes",
      "Relm",
      "Terra",
      "Chadarnook",
      "Elayne",
      "Katarin",
      "Madonna",
      "Lola",
      "Rachel"
    ],
    "neutral": [
      "Atma",
      "Atma Weapon",
      "Chupon",
      "Esper",
      "Espers",
      "Ifrit",
      "Ifrit / Shiva",
      "Moogle",
      "Moogles",
      "Shiva",
      "Ultros",
      "Whelk",
      "Wolf",
      "Wrexsoul"
    ],
    "genderless": [
      "Kappa"
    ]
  },
  "aliases": {
    "Emperor Gestahl": "Gestahl",
    "Gestal": "Gestal",
    "Letter": "Lola",
    "Sabib": "Sabin",
    "Sigfried": "Siegfried",
    "Ziegfried": "Siegfried",
    "♫ So Gently, You Touched My Heart. I Will Be Forever Yours.": "Celes",
    "♫ We Must Part Now. My Life Goes On. But My Heart Won'T Give You Up.": "Celes",
    "(When Defeating {{Foot|Doom Gaze|Deathgaze In Later Releases)": "Celes"
  },
  "notes": [
    "For this site, the dialogue is split into main narrative and optional dialogue.",
    "We match up each optional dialogue to its section, then add it in as e.g.:",
    "  {'CHOICE': [",
    "   [],",
    "   [{'Cloud': 'Buy one.'}]",
    "  ]}",
    " There is a section called 'other' which I've treated as optional. Each line of dialogue is treated as optional, which suggest more flexibility that there really is, but there's no other indication of how the dialogue breaks up."
  ]
}
```

### 角色列表（共134个）

- "CHOICE" :1746,
- "Npc" :737,
- "NARRATIVE" :245,
- "Locke" :229,
- "Sabin" :198,
- "Celes" :164,
- "Edgar" :160,
- "Party" :154,
- "Terra" :149,
- "Cyan" :144,
- "Kefka" :125,
- "Strago" :96,
- "Setzer" :79,
- "Gestahl" :67,
- "Relm" :62,
- "Gau" :58,
- "Banon" :56,
- "Cid" :51,
- "Shadow" :47,
- "Leo" :41,
- "Ultros" :39,
- "Soldier" :38,
- "Returner" :28,
- "Impresario" :27,
- "Maduin" :24,
- "Guard" :24,
- "Aged Man" :23,
- "Ramuh" :22,
- "Mog" :21,
- "Gungho" :20,
- "Elder" :18,
- "Unknown" :18,
- "Gerad" :15,
- "Vargas" :15,
- "Baram" :14,
- "Arvis" :13,
- "Merchant" :13,
- "Man" :13,
- "Elayne" :12,
- "Old Man" :12,
- "Wedge" :12,
- "Clyde" :11,
- "Madonna" :11,
- "Owain" :11,
- "Ghost" :11,
- "Treasure" :10,
- "Owzer" :10,
- "Yura" :10,
- "Doma Sentry" :10,
- "Duncan" :9,
- ... 共134个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFVI_B/,True,Final Fantasy VI,Final Fantasy,TOTAL,3407,29389,12844,35444,-0.46647374916363304,102.48243474746637,6.846850253504683,132
../data/FinalFantasy/FFVI_B/,True,Final Fantasy VI,Final Fantasy,male,1599,13523,6326,16238,-0.5872276514463497,103.08018648635975,6.829770209592916,41
../data/FinalFantasy/FFVI_B/,True,Final Fantasy VI,Final Fantasy,female,421,3148,1814,3734,-0.9166281035963397,104.72529310361737,6.872550000490326,9
../data/FinalFantasy/FFVI_B/,True,Final Fantasy VI,Final Fantasy,neutral,69,708,350,851,-0.6177523809523784,103.09451186440678,7.34979981598063,14
../data/FinalFantasy/FFVI_B/,True,Final Fantasy VI,Final Fantasy,genderless,6,69,20,80,-0.5633405797101432,105.2462934782609,6.553706956521738,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://finalfantasy.fandom.com/wiki/Final_Fantasy_VI_SNES_script"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
