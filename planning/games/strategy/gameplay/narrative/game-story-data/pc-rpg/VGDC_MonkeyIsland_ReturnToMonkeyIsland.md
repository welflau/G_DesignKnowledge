# 猴岛小英雄 · ReturnToMonkeyIsland（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：猴岛小英雄, 冒险游戏, 对话语料, PC RPG, 角色对话
> 游戏类型：冒险游戏

## 概述
猴岛小英雄系列《ReturnToMonkeyIsland》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：猴岛小英雄（MonkeyIsland）
- **游戏**：ReturnToMonkeyIsland
- **品类**：冒险游戏
- **说明**：LucasArts经典点击冒险

### 元数据 (meta.json)

```json
{
  "game": "Return to Monkey Island",
  "series": "Monkey Island",
  "year": 2022,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "Game data",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "complete",
    "dialogueOrder": false,
    "choices": "Not included"
  },
  "error checks": {},
  "notes": "See Readme",
  "parserParameters": {
    "parser": "YackParser",
    "fileType": ".yack.txt"
  },
  "mainPlayerCharacters": [
    "Guybrush"
  ],
  "characterGroups": {
    "male": [
      "Boybrush",
      "Captain Trent",
      "Chuckie",
      "Clint",
      "Cobb",
      "Cook",
      "Curator",
      "Flambe",
      "Gullet",
      "Guybrush",
      "Judge",
      "Lechuck",
      "Lookout",
      "Murray",
      "Ned",
      "Otis",
      "Parkmale",
      "Quarantined Pirate 1",
      "Quarantined Pirate 2",
      "Stan",
      "Toothrot",
      "Wally",
      "Bob",
      "Guard",
      "Fisher1",
      "Fisher2",
      "Fishmonger",
      "Vendor",
      "Youngpirate1",
      "Youngpirate3",
      "Youngpirate5",
      "Finickypirate",
      "Janitor"
    ],
    "female": [
      "Captain Lila",
      "Captain Madison",
      "Carla",
      "Dee",
      "Elaine",
      "Flair Gorey",
      "Ironrose",
      "Locksmith",
      "Parkfemale",
      "Putra",
      "Queen",
      "Voodoolady",
      "Wideybones",
      "Youngpirate2",
      "Youngpirate4"
    ],
    "neutral": [
      "Art",
      "Hint",
      "Sfx",
      "SYSTEM",
      "Todo",
      "Guybrush (internal)"
    ]
  },
  "aliases": {
    "Captainlila": "Captain Lila",
    "Captainmadison": "Captain Madison",
    "Captaintrent": "Captain Trent",
    "Flairgorey": "Flair Gorey",
    "Quarantinedpirate1": "Quarantined Pirate 1",
    "Quarantinedpirate2": "Quarantined Pirate 2",
    "System": "SYSTEM",
    "Yardarm": "Bob"
  }
}
```

### 角色列表（共88个）

- "Guybrush (internal)" :2408,
- "Guybrush" :2283,
- "Hint" :1168,
- "Elaine" :296,
- "Boybrush" :293,
- "Lechuck" :268,
- "Judge" :208,
- "Gullet" :201,
- "Putra" :196,
- "Stan" :196,
- "Ironrose" :189,
- "Cook" :164,
- "Queen" :153,
- "Curator" :147,
- "Murray" :147,
- "Voodoolady" :144,
- "Carla" :140,
- "Bob" :139,
- "Locksmith" :131,
- "Fishmonger" :131,
- "Flair Gorey" :118,
- "Captain Madison" :115,
- "Captain Lila" :114,
- "Chuckie" :114,
- "Fisher1" :106,
- "Wideybones" :100,
- "Toothrot" :100,
- "Todo" :96,
- "Flambe" :87,
- "Guard" :83,
- "Dee" :70,
- "Wally" :69,
- "Ned" :69,
- "Art" :66,
- "LOCATION" :66,
- "Otis" :61,
- "Captain Trent" :57,
- "Quarantined Pirate 1" :46,
- "Lookout" :46,
- "Vendor" :44,
- "Youngpirate4" :34,
- "Sfx" :31,
- "Cobb" :30,
- "Quarantined Pirate 2" :29,
- "Brrrmudian9" :27,
- "Brrrmudian12" :27,
- "Brrrmudian4" :27,
- "Brrrmudian5" :27,
- "Brrrmudian14" :27,
- "Brrrmudian7" :25,
- ... 共88个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MonkeyIsland/ReturnToMonkeyIsland/,True,Return to Monkey Island,Monkey Island,TOTAL,11084,92275,21788,111984,0.38206027142071086,99.86664544474708,6.743092682481968,86
../data/MonkeyIsland/ReturnToMonkeyIsland/,True,Return to Monkey Island,Monkey Island,male,5165,41793,10052,50973,0.4234125315568882,99.43222557020485,6.667261882992017,32
../data/MonkeyIsland/ReturnToMonkeyIsland/,True,Return to Monkey Island,Monkey Island,female,1812,14869,3821,17926,0.15366928367112997,100.89185726152164,6.573568345863919,15
../data/MonkeyIsland/ReturnToMonkeyIsland/,True,Return to Monkey Island,Monkey Island,neutral,3777,35027,7275,42292,0.5351909030412187,99.80106488275074,6.796461766002996,6

```



## 策划参考价值
冒险游戏类型的对话叙事参考。LucasArts经典点击冒险
