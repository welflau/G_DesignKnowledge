# 极乐迪斯科 · DiscoElysium（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：极乐迪斯科, 叙事RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：叙事RPG

## 概述
极乐迪斯科系列《DiscoElysium》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：极乐迪斯科（DiscoElysium）
- **游戏**：DiscoElysium
- **品类**：叙事RPG
- **说明**：ZA/UM的叙事巅峰之作，技能系统=内心声音

### 元数据 (meta.json)

```json
{
  "game": "Disco Elysium",
  "series": "Disco Elysium",
  "year": 2019,
  "status": "in progress",
  "source": "http://fayde.seadragonlair.co.uk/",
  "alternativeMeasure": true,
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "None"
  },
  "parserParameters": {
    "parser": "DiscoElysiumParser",
    "fileType": ".db"
  },
  "mainPlayerCharacters": [
    "Hades"
  ],
  "characterGroups": {
    "male": [],
    "female": [],
    "neutral": []
  },
  "aliases": {}
}
```

### 角色列表（共299个）

- "SYSTEM" :33294,
- "You" :23947,
- "GOTO" :23712,
- "CHOICE" :16349,
- "Kim Kitsuragi" :9391,
- "Narrator" :6575,
- "Jump to" :6455,
- "Cuno" :1722,
- "Klaasje (Miss Oranje Disco Dancer)" :1223,
- "The Deserter" :1108,
- "Joyce Messier" :1040,
- "Empathy" :1034,
- "Rhetoric" :957,
- "Evrart Claire" :954,
- "Logic" :935,
- "Inland Empire" :905,
- "Garte, the Cafeteria Manager" :850,
- "Lena, the Cryptozoologist's wife" :759,
- "Conceptualization" :700,
- "Soona, the Programmer" :692,
- "Esprit de Corps" :682,
- "Encyclopedia" :669,
- "Idiot Doom Spiral" :668,
- "Jean Vicquemare" :659,
- "Noid" :643,
- "Electrochemistry" :628,
- "Titus Hardie" :627,
- "Shivers" :623,
- "Acele" :614,
- "Volition" :545,
- "Andre" :542,
- "Authority" :532,
- "Plaisance" :525,
- "Half Light" :523,
- "Savoir Faire" :484,
- "Composure" :483,
- "Drama" :482,
- "Bird's Nest Roy" :476,
- "Lilienne, the Net Picker" :476,
- "Steban, the Student Communist" :476,
- "Novelty Dicemaker" :472,
- "Reaction Speed" :452,
- "Gary, the Cryptofascist" :444,
- "Suggestion" :441,
- "Endurance" :438,
- "Interfacing" :438,
- "Visual Calculus" :437,
- "Egg Head" :435,
- "Measurehead" :430,
- "Sunday Friend" :430,
- ... 共299个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/DiscoElysium/DiscoElysium/,True,Disco Elysium,Disco Elysium,TOTAL,88859,926528,233119,1153573,0.6516304605413872,97.46973026302705,6.635290580982031,296
../data/DiscoElysium/DiscoElysium/,True,Disco Elysium,Disco Elysium,male,0,NA,NA,NA,NA,NA,NA,0
../data/DiscoElysium/DiscoElysium/,True,Disco Elysium,Disco Elysium,female,0,NA,NA,NA,NA,NA,NA,0
../data/DiscoElysium/DiscoElysium/,True,Disco Elysium,Disco Elysium,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import requests, io, os
from zipfile import ZipFile

url = "http://fayde.seadragonlair.co.uk/downloads/dealogue-db-jv-21-12-21.zip"

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("raw/db.zip")

os.rename("raw/db.zip/discobase12-17-2021-4-18-51-PM.db", "raw/discobase12-17-2021-4-18-51-PM.db")
```


## 策划参考价值
叙事RPG类型的对话叙事参考。ZA/UM的叙事巅峰之作，技能系统=内心声音
