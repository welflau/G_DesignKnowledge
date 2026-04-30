# Barbie · BarbieDiaries_HighSchoolMystery（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：Barbie, RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：RPG


> ⚠️ **数据状态：索引条目** — 本条目仅包含游戏meta信息和角色列表，完整对话数据需运行VideoGameDialogueCorpus的scraper脚本生成。

## 概述
Barbie系列《BarbieDiaries_HighSchoolMystery》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：Barbie（Barbie）
- **游戏**：BarbieDiaries_HighSchoolMystery
- **品类**：RPG
- **说明**：

### 元数据 (meta.json)

```json
{
  "game": "Barbie Diaries High School Mystery",
  "series": "Barbie",
  "year": 2006,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "https://oldgamesdownload.com/the-barbie-diaries-high-school-mystery/",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": false,
    "choices": "not included"
  },
  "parserParameters": {
    "parser": "jsonCopier",
    "fileType": ".json"
  },
  "mainPlayerCharacters": [
    "Barbie"
  ],
  "characterGroups": {
    "male": [
      "Coach Paternal",
      "Cole",
      "Kevin",
      "Milo",
      "Mr. Fermat",
      "Neil",
      "Todd"
    ],
    "female": [
      "Barbie",
      "Candy",
      "Courtney",
      "Dawn",
      "Miss Dewey",
      "Mrs. Baez",
      "Raquelle",
      "Reagan",
      "Tia",
      "Tutorial"
    ]
  },
  "aliases": {}
}
```

### 角色列表（共17个）

- "Barbie" :539,
- "Courtney" :109,
- "Tutorial" :103,
- "Tia" :102,
- "Kevin" :89,
- "Todd" :85,
- "Reagan" :85,
- "Raquelle" :85,
- "Neil" :80,
- "Dawn" :76,
- "Cole" :75,
- "Candy" :75,
- "Mrs. Baez" :68,
- "Milo" :66,
- "Coach Paternal" :57,
- "Miss Dewey" :57,
- "Mr. Fermat" :52

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Barbie/BarbieDiaries_HighSchoolMystery/,True,Barbie Diaries High School Mystery,Barbie,TOTAL,1803,20150,1849,24190,2.8259912876251274,94.2117655643786,6.6932429194507925,17
../data/Barbie/BarbieDiaries_HighSchoolMystery/,True,Barbie Diaries High School Mystery,Barbie,male,504,5318,511,6420,2.713952518088332,94.14097304579434,6.6883532158625325,7
../data/Barbie/BarbieDiaries_HighSchoolMystery/,True,Barbie Diaries High School Mystery,Barbie,female,1299,14832,1337,17770,2.873867838363596,94.21709500330405,6.695976055551925,10

```



## 策划参考价值
RPG类型的对话叙事参考。
