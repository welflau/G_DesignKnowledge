# 流氓国家 · RogueStateRevolution（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：流氓国家, 策略模拟, 对话语料, PC RPG, 角色对话
> 游戏类型：策略模拟


> ⚠️ **数据状态：索引条目** — 本条目仅包含游戏meta信息和角色列表，完整对话数据需运行VideoGameDialogueCorpus的scraper脚本生成。

## 概述
流氓国家系列《RogueStateRevolution》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：流氓国家（RogueState）
- **游戏**：RogueStateRevolution
- **品类**：策略模拟
- **说明**：政治策略模拟

### 元数据 (meta.json)

```json
{
  "game": "Rogue State: Revolution",
  "series": "Rogue State",
  "year": 2021,
  "status": "in progress",
  "source": "game data",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "NA"
  },
  "notes": "This captures the FMVs",
  "parserParameters": {
    "parser": "RogueStateParser",
    "fileType": ".srt"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [
      "Male anchor",
      "Male vox pops",
      "Yusef"
    ],
    "female": [
      "Female anchor",
      "Female vox pops",
      "Sabriya"
    ],
    "neutral": []
  },
  "aliases": {
    "Sab": "Sabriya",
    "Yus": "Yusef",
    "Sab and Yus": [
      "Sabriya",
      "Yusef"
    ]
  }
}
```

### 角色列表（共7个）

- "Yusef" :69,
- "Sabriya" :64,
- "LOCATION" :38,
- "Male anchor" :12,
- "Female anchor" :12,
- "Female vox pops" :1,
- "Male vox pops" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/RogueState/RogueStateRevolution/,False,Rogue State: Revolution,Rogue State,TOTAL,159,3785,624,5160,2.862282859973581,85.34515209540022,7.262228194966636,6
../data/RogueState/RogueStateRevolution/,False,Rogue State: Revolution,Rogue State,male,82,1735,305,2424,3.1145188264751766,82.86495157556575,7.404281943591439,3
../data/RogueState/RogueStateRevolution/,False,Rogue State: Revolution,Rogue State,female,77,2050,318,2736,2.672833870225496,87.38171222580151,7.145058183770517,3
../data/RogueState/RogueStateRevolution/,False,Rogue State: Revolution,Rogue State,neutral,0,NA,NA,NA,NA,NA,NA,0

```



## 策划参考价值
策略模拟类型的对话叙事参考。政治策略模拟
