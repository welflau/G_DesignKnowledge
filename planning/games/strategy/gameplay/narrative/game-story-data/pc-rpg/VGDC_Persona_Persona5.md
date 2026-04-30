# 女神异闻录 · Persona5（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：女神异闻录, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
女神异闻录系列《Persona5》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：女神异闻录（Persona）
- **游戏**：Persona5
- **品类**：JRPG
- **说明**：Atlus的社交模拟+JRPG，Confidant系统

### 元数据 (meta.json)

```json
{
  "game": "Persona 5",
  "series": "Persona",
  "year": 2016,
  "status": "superseded",
  "source": "https://transcripts.fandom.com/wiki/Persona_5",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "fandomParser2",
    "fileType": ".html",
    "scriptHasOptionalDialogueSection": false,
    "scriptStartCue": "<ul><li>",
    "scriptEndCue": "<div class=\"printfooter\">",
    "actionCue": "("
  },
  "mainPlayerCharacters": [
    "Joker"
  ],
  "characterGroups": {
    "male": [
      "Ryuji",
      "Joker",
      "Yusuke",
      "Morgana",
      "Mishima",
      "Sojiro",
      "Shrimp Stand Owner",
      "Beefy Trendsetter",
      "Scruffy Romantic",
      "Man",
      "Wealthy-looking Man",
      "Pretentious Man",
      "Man 2",
      "Boy",
      "Man in a Swimsuit"
    ],
    "female": [
      "Ann",
      "Makoto",
      "Futaba",
      "Haru",
      "Kawakami",
      "Hifumi",
      "Chihaya",
      "Takemi",
      "Ohya",
      "Slim Lady",
      "Voluptuous Lady",
      "Ms. Kawakami",
      "Tall Student",
      "Bespectacled Student",
      "Lady in Black Yukata",
      "Woman's Voice",
      "Pilot",
      "Flight Attent",
      "Woman in a Swimsuit",
      "Lady in Pink Yukata",
      "Shadow Futaba"
    ],
    "neutral": []
  },
  "aliases": {
    "Guy": "Joker",
    "Futaa": "Joker",
    "Familiar Voice": "Ryuji",
    "Brawny Voice": "Beefy Trendsetter",
    "Deep Voice": "Scruffy Romantic",
    "Lady in a Pink Yukata": "Lady in Pink Yukata"
  }
}
```

### 角色列表（共37个）

- "Ryuji" :181,
- "Ann" :107,
- "ACTION" :92,
- "Joker" :91,
- "Makoto" :83,
- "Yusuke" :66,
- "Morgana" :47,
- "Futaba" :42,
- "Mishima" :40,
- "Sojiro" :20,
- "Haru" :19,
- "Kawakami" :16,
- "Hifumi" :15,
- "Chihaya" :12,
- "Takemi" :12,
- "Ohya" :12,
- "Shrimp Stand Owner" :6,
- "Beefy Trendsetter" :5,
- "Slim Lady" :4,
- "Scruffy Romantic" :4,
- "Voluptuous Lady" :3,
- "Ms. Kawakami" :3,
- "Man" :3,
- "Wealthy-looking Man" :3,
- "Pretentious Man" :3,
- "Tall Student" :2,
- "Lady in Black Yukata" :2,
- "Lady in Pink Yukata" :2,
- "Man 2" :1,
- "Woman's Voice" :1,
- "Boy" :1,
- "Bespectacled Student" :1,
- "Pilot" :1,
- "Flight Attent" :1,
- "Man in a Swimsuit" :1,
- "Woman in a Swimsuit" :1,
- "Shadow Futaba" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Persona/Persona5/,True,Persona 5,Persona,TOTAL,811,9730,3315,11380,-0.6442663684178687,104.90947807235789,6.357492151282206,36
../data/Persona/Persona5/,True,Persona 5,Persona,male,471,5305,1750,6184,-0.6525684933351261,105.14049396795477,6.757343305776221,15
../data/Persona/Persona5/,True,Persona 5,Persona,female,340,4425,1565,5196,-0.6312843450479235,104.6246372448151,5.87850778325301,21
../data/Persona/Persona5/,True,Persona 5,Persona,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://transcripts.fandom.com/wiki/Persona_5"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
JRPG类型的对话叙事参考。Atlus的社交模拟+JRPG，Confidant系统
