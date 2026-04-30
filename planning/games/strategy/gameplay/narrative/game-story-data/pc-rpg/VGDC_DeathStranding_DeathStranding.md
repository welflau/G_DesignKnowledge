# 死亡搁浅 · DeathStranding（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：死亡搁浅, 开放世界, 对话语料, PC RPG, 角色对话
> 游戏类型：开放世界

## 概述
死亡搁浅系列《DeathStranding》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：死亡搁浅（DeathStranding）
- **游戏**：DeathStranding
- **品类**：开放世界
- **说明**：小岛秀夫的开放世界+叙事

### 元数据 (meta.json)

```json
{
  "game": "Death Stranding",
  "series": "Death Stranding",
  "year": 2019,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "https://game-scripts-wiki.blogspot.com/2019/12/death-stranding-full-transcript.html",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "NA"
  },
  "error checks": {},
  "parserParameters": {
    "parser": "DeathStrandingParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Sam"
  ],
  "characterGroups": {
    "male": [],
    "female": [],
    "neutral": []
  },
  "aliases": {
    "Die-Harman": "Die-Hardman",
    "Deadman Holorgam": "Deadman",
    "Deaman": "Deadman",
    "Frgile": "Fragile",
    "Hartman": "Heartman",
    "Hartman’s Hologram": "Heartman",
    "Mama &amp; Lockne": [
      "Mama",
      "Lockne"
    ],
    "Lockne/Mama": [
      "Mama",
      "Lockne"
    ],
    "Sam &amp; Fragile": [
      "Sam",
      "Fragile"
    ],
    "Amelia Hologram (of Hologram?)": "Amelie",
    "Amelia": "Amelie",
    "Bridget Strand": "Bridget",
    "": "Hologram",
    "ACTION": {
      "Man": [
        "See the sunset // The day is ending // Let that yawn out // There's no pretending //"
      ],
      "Amelie": [
        "See the sunset // The day is ending // Let that yawn out // There's no pretending // I will hold you // And protect you // So let love warm you // 'til the morning"
      ],
      "Clifford Unger": [
        "See the sunset // The day is ending // Let that yawn out // There's no pretending // I will hold you // And protect you // So let love warm you // Till the morning //"
      ]
    }
  }
}
```

### 角色列表（共64个）

- "ACTION" :581,
- "Sam" :428,
- "Deadman" :192,
- "Die-Hardman" :151,
- "Fragile" :107,
- "Mama" :99,
- "Heartman" :81,
- "Amelie" :63,
- "Bridget" :63,
- "Higgs" :46,
- "Clifford Unger" :33,
- "Lockne" :30,
- "John" :29,
- "South Knot City" :28,
- "Igor" :27,
- "Computer" :18,
- "LOCATION" :16,
- "Man" :15,
- "Junk Dealer" :13,
- "Junk Dealer's Girlfriend" :11,
- "Port Knot City" :11,
- "Mountain Knot City" :10,
- "Mountaineer" :8,
- "Soldier" :8,
- "Combat Veteran" :8,
- "Loudspeaker" :5,
- "Woman" :5,
- "???" :4,
- "Paleontologist" :4,
- "Doctor" :4,
- "Die-Hardman Holorgam" :4,
- "Young Sam" :4,
- "Old Bridget" :3,
- "Photographer" :3,
- "Roboticist" :3,
- "Lake Knot City" :3,
- "Wind Farm" :3,
- "Hologram" :3,
- "Special Forces" :2,
- "Evo-devo Biologist" :2,
- "Spiritualist" :2,
- "Shady Operator" :2,
- "Capital Knot City" :2,
- "Center West" :2,
- "Doctor 2" :2,
- "Doctor 1" :2,
- "Woman in Red" :2,
- "Soldiers" :1,
- "Young Bridget" :1,
- "Lisa" :1,
- ... 共64个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/DeathStranding/DeathStranding/,False,Death Stranding,Death Stranding,TOTAL,1562,46505,7188,57235,1.4558151792786589,96.14856350235077,6.966347460110589,62
../data/DeathStranding/DeathStranding/,False,Death Stranding,Death Stranding,male,0,NA,NA,NA,NA,NA,NA,0
../data/DeathStranding/DeathStranding/,False,Death Stranding,Death Stranding,female,0,NA,NA,NA,NA,NA,NA,0
../data/DeathStranding/DeathStranding/,False,Death Stranding,Death Stranding,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
from bs4 import BeautifulSoup


# ??? characters
# 'you still with me sam?'
# https://www.youtube.com/watch?v=3J3wLlCnCQw&t=5s

page = "https://game-scripts-wiki.blogspot.com/2019/12/death-stranding-full-transcript.html"

req = Request(
    page, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

html = urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, "html5lib")
post = soup.find("div", {"class":"post-body"})

o = open("raw/page01.html",'w')
o.write(str(post))
o.close()



```


## 策划参考价值
开放世界类型的对话叙事参考。小岛秀夫的开放世界+叙事
