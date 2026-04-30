# 博德之门 · BaldursGate3（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：博德之门, CRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：CRPG

## 概述
博德之门系列《BaldursGate3》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：博德之门（BaldursGate）
- **游戏**：BaldursGate3
- **品类**：CRPG
- **说明**：BioWare/Larian经典CRPG，对话选择+D&D规则

### 元数据 (meta.json)

```json
{
  "game": "Baldur's Gate 3",
  "series": "Baldur's Gate",
  "year": 2023,
  "status": "in progress",
  "alternativeMeasure": true,
  "source": "Game data",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "2",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "N/A",
    "falsePositive_numErrors": "N/A",
    "falsePositive_notes": "Data extracted from game data"
  },
  "parserParameters": {
    "parser": "BG3Parser",
    "fileType": ".txt"
  },
  "mainPlayerCharacters": [
    "PC"
  ],
  "characterGroups": {
    "male": [
      "Arnell Hallowleaf",
      "Astarion",
      "Barcus",
      "Duke Ravengard",
      "Gale",
      "Halsin",
      "Kith'rak Voss",
      "Minsc",
      "Withers",
      "Oathbreaker Knight",
      "Omeluum",
      "Orpheus",
      "Owlbear Cub",
      "Boo",
      "Sceleritas Fel",
      "Scratch",
      "Umi",
      "Volo",
      "Elminster",
      "Wyll",
      "Yurgir",
      "Gortash",
      "Gale's Projection",
      "Raphael",
      "Zevlor",
      "Rolan",
      "Wulbren",
      "Dammon"
    ],
    "female": [
      "Alfira",
      "Arabella",
      "Dame Aylin",
      "Shadowheart",
      "Karlach",
      "Emmeline Hallowleaf",
      "Isobel",
      "Jaheira",
      "Korrilla",
      "Lae'zel",
      "Mizora",
      "Narrator",
      "Minthara",
      "Tara",
      "Yenna",
      "Netherbrain",
      "Aunty Ethel",
      "Nettie",
      "Mayrina",
      "Tara",
      "Counsellor Florrick",
      "Gauntlet Devella",
      "Kagha",
      "Gur Leader Ulma"
    ],
    "neutral": [
      "Book of Dead Gods"
    ],
    "cut": [
      "GROUP_Daisy"
    ]
  },
  "aliases": {
    "Captive": "Shadowheart",
    "Devil": "Karlach",
    "Mysterious Figure": "Withers",
    "S_FOR_OwlBear_Cub_001": "Owlbear Cub",
    "S_GLO_Boo": "Boo",
    "The Drow Minthara": "Minthara",
    "Tressym": "Tara",
    "Weary Traveller": "Elminster",
    "a480a240-b8ea-4e6a-b4b9-a8edc8fd4a3d": "Book of Dead Gods",
    "b7439d00-eb7e-5376-28fb-5b70f698445a": "Gale",
    "bbb9e4ee-8c2f-61e7-bcec-351a136091e7": "Astarion",
    "c1f13b4f-baad-34e0-9ffe-11ee706f3ec5": "Gortash",
    "Spectral Voice": "Gale's Projection",
    "e6b3c2c4-e88d-e9e6-ffa1-d49cdfadd411": "PC",
    "ea38aca4-6eb4-29a4-c119-8bb1364f681a": "PC",
    "ab8ed602-dd13-d3f9-1be2-a4d489b82d07": "PC",
    "META_NOTE": "Mappings below were automatically extracted from a different parse of the game ------",
    "META_NOTE2": "It begins with a list of character IDs that are mapped to the same text label, but presumably are different characters",
    "43b5176f-b2d8-4d60-b901-d90194d50181": "Civilian",
    "6bdaf443-e6fd-4cd0-9f4e-31f6eaf231bc": "Civilian",
    "928c724f-fb39-4776-ac11-1f828e9c699f": "Civilian",
    "bace1e81-671d-4120-bc0c-c46d26bcbbb7": "Civilian",
    "d98a20d2-8457-42b6-ab3d-0cc8f1f911ac": "Civilian",
    "1ada20fe-49b1-4663-a832-0e2c7126907d": "Ancient Servant",
    "9ede4829-ec97-40b6-ac1c-ef14b9c6d14a": "Ancient Servant",
    "ca673f78-bf5a-4170-9a3d-86956fd7320b": "Ancient Servant",
    "d03067ac-43a7-435b-be97-558065b1f7d1": "Ancient Servant",
    "e6bd5cec-2691-4dc4-99ae-2461c87bb6ba": "Ancient Servant",
    "f7e60433-053d-4735-b542-658397785f7a": "Ancient Servant",
    "00e62214-2ab7-4cdb-bd9c-ac513dd55057": "Errant Soul",
    "0f89ab40-ec11-464c-9ec1-ebeb7361957e": "Errant Soul",
    "2133c53e-3b07-457c-9e6d-a8a2ac8b275d": "Errant Soul",
    "3b91c966-5748-4c3f-a90c-0cd28ed63be9": "Errant Soul",
    "4bb77d5a-831e-4be8-aa94-0ffd978757e5": "Errant Soul",
    "68b7612d-4736-464d-8b1f-581ed2f370b6": "Errant Soul",
    "7987935d-d347-4516-98fb-129836d3aa23": "Errant Soul",
    "98e4242c-70e2-44ae-a580-e036316b5494": "Errant Soul",
    "9a0ab40d-a9d7-44e0-a141-77a790a0ff18": "Errant Soul",
    "a67db2ac-7900-4261-90b9-ad834a13e6e9": "Errant Soul",
    "abe9c76a-174c-47b2-8206-ed2df1a13354": "Errant Soul",
    "beff08ea-86ba-4bdf-a5eb-74f3c13a4e4b": "Errant Soul",
    "c9af83bb-8779-4647-9a1b-021c470fd32a": "Errant Soul",
    "c9b0316e-4d58-4b2f-8deb-4253610be051": "Errant Soul",
    "cc40b93d-eee9-49cc-9634-f2580f583564": "Errant Soul",
    "d2fff896-a953-448c-8340-45e757b69fad": "Errant Soul",
    "d72dcdf8-246f-4068-b16c-3ac06bb8a4da": "Errant Soul",
    "da546a00-04fd-4353-b519-03498a47ae98": "Errant Soul",
    "f17b337a-3ae8-4b95-9ab6-eecef8cb4e7e": "Errant Soul",
    "fb4ed249-24b7-4d76-b36d-9797260d3d9e": "Errant Soul",
    "43421d3b-74b7-4107-b0a3-c765ee282700": "Dead Toll Collector",
    "d11a407d-9d16-40f1-a4de-fce659462383": "Dead Toll Collector",
    "2840bf4a-212c-4f4c-ba7e-f34c7683308c": "Deep Rothé",
    "2cd6c5c8-cf67-4114-a4c1-b72d6705646e": "Deep Rothé",
    "697cc9bf-9f49-48f4-b270-6777882a2280": "Deep Rothé",
    "d7536f2a-ef68-42af-8834-c6fd53a91962": "Deep Rothé",
    "4dac1
```

### 角色列表（共2083个）

- "ACTION" :52019,
- "PC" :39752,
- "LOCATION" :9073,
- "Narrator" :8260,
- "Astarion" :5127,
- "Shadowheart" :4870,
- "Lae'zel" :4563,
- "Karlach" :4500,
- "Gale" :3957,
- "Wyll" :3610,
- "Minthara" :2157,
- "Jaheira" :2088,
- "Halsin" :1958,
- "Minsc" :1414,
- "Withers" :746,
- "Mizora" :743,
- "Auntie Ethel" :642,
- "Raphael" :616,
- "S_GLO_Daisy_Backup2" :601,
- "Alfira" :557,
- "Dream Visitor" :556,
- "Barcus" :528,
- "Kith'rak Voss" :518,
- "Gortash" :515,
- "Zevlor" :511,
- "Dame Aylin" :499,
- "S_GLO_Emperor_Backup2" :491,
- "Volo" :488,
- "Rolan" :465,
- "Isobel" :462,
- "Sceleritas Fel" :459,
- "Wulbren" :438,
- "Nettie" :400,
- "Mayrina" :374,
- "Tara" :373,
- "Murder Tribunal" :361,
- "Counsellor Florrick" :360,
- "Gauntlet Devella" :355,
- "Dammon" :355,
- "Kagha" :351,
- "Gur Leader Ulma" :337,
- "Orpheus" :334,
- "Child Merchant" :333,
- "Mol" :329,
- "Ketheric Thorm" :310,
- "Orin" :307,
- "Duke Ravengard" :291,
- "Disciple Z'rell" :280,
- "Aradin" :277,
- "Oskar" :275,
- ... 共2083个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/BaldursGate/BaldursGate3/,True,Baldur's Gate 3,Baldur's Gate,TOTAL,135072,1838464,415410,2242943,0.5321165433114832,99.13017508217447,6.743642516722233,2047
../data/BaldursGate/BaldursGate3/,True,Baldur's Gate 3,Baldur's Gate,male,20673,299387,61629,362892,0.6075554662417133,99.35916227373932,6.469360088929034,23
../data/BaldursGate/BaldursGate3/,True,Baldur's Gate 3,Baldur's Gate,female,28517,410759,86725,499582,0.6088178231590895,99.1336143201922,6.643443697081225,15
../data/BaldursGate/BaldursGate3/,True,Baldur's Gate 3,Baldur's Gate,neutral,0,NA,NA,NA,NA,NA,NA,0
../data/BaldursGate/BaldursGate3/,True,Baldur's Gate 3,Baldur's Gate,cut,0,NA,NA,NA,NA,NA,NA,0

```



## 策划参考价值
CRPG类型的对话叙事参考。BioWare/Larian经典CRPG，对话选择+D&D规则
