# 星露谷物语 · StardewValley（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：星露谷物语, 模拟经营RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：模拟经营RPG

## 概述
星露谷物语系列《StardewValley》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：星露谷物语（StardewValley）
- **游戏**：StardewValley
- **品类**：模拟经营RPG
- **说明**：ConcernedApe的田园模拟，NPC日程+好感度

### 元数据 (meta.json)

```json
{
  "game": "Stardew Valley",
  "series": "Stardew Valley",
  "year": 2016,
  "status": "ready",
  "source": "https://drive.google.com/drive/folders/0BwyXuxAqGS7ueVdFX2dQSUVzcUk",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "",
    "truePositive_numSourceErrors": "4",
    "truePositive_notes": "Television reports (such as weather report, fortune teller) are missing from the source file. Some sidequest dialogue (eg Willy fishing quest) is missing too.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "1",
    "falsePositive_notes": "Some system text identified (line starts with %), and fixed."
  },
  "characterInfoSource": "https://stardewvalleywiki.com",
  "parserParameters": {
    "parser": "StardewValleyParser",
    "fileType": ".yaml"
  },
  "mainPlayerCharacters": [
    "PC"
  ],
  "characterGroups": {
    "playerChoice": [
      "PC"
    ],
    "male": [
      "Sam",
      "Sebastian",
      "Alex",
      "Elliott",
      "Shane",
      "Harvey",
      "Lewis",
      "Demetrius",
      "Pierre",
      "Clint",
      "Linus",
      "Wizard",
      "George",
      "Gus",
      "Willy",
      "Kent",
      "Vincent",
      "Morris",
      "Gunther",
      "Marlon",
      "Grandpa",
      "Mister Qi",
      "Gil",
      "Krobus"
    ],
    "female": [
      "Abigail",
      "Leah",
      "Haley",
      "Emily",
      "Maru",
      "Penny",
      "Pam",
      "Jodi",
      "Robin",
      "Marnie",
      "Evelyn",
      "Caroline",
      "Sandy",
      "Jas"
    ],
    "undefined": [
      "Dwarf"
    ]
  },
  "aliases": {
    "Haley": {
      "SYSTEM": [
        "Haley is ignoring you."
      ]
    },
    "Marnie": {
      "SYSTEM": [
        "Marnie doesn't seem to notice"
      ]
    },
    "Abigail": {
      "SYSTEM": [
        "Abgail is lost in her music"
      ]
    },
    "Pam": {
      "SYSTEM": [
        "Pam isn't responding",
        "Pam seems out of it"
      ]
    },
    "Sebastian": {
      "SYSTEM": [
        "Sebastian seems lost in thought"
      ]
    },
    "Shane": {
      "SYSTEM": [
        "Shane's hard at work."
      ]
    }
  }
}
```

### 角色列表（共44个）

- "ACTION" :3538,
- "Sam" :334,
- "Abigail" :329,
- "Leah" :313,
- "Sebastian" :303,
- "Alex" :303,
- "Haley" :283,
- "Elliott" :263,
- "Emily" :259,
- "Penny" :243,
- "Maru" :241,
- "Shane" :231,
- "Harvey" :230,
- "STATUS" :210,
- "CHOICE" :150,
- "PC" :130,
- "Lewis" :128,
- "Demetrius" :105,
- "Pierre" :104,
- "Pam" :103,
- "Jodi" :101,
- "Clint" :89,
- "Linus" :84,
- "Wizard" :73,
- "Marnie" :72,
- "Robin" :71,
- "George" :69,
- "Evelyn" :68,
- "Caroline" :67,
- "Gus" :53,
- "Willy" :44,
- "Jas" :42,
- "Sandy" :41,
- "Vincent" :41,
- "Kent" :40,
- "Morris" :26,
- "Dwarf" :25,
- "Krobus" :24,
- "Gunther" :22,
- "Grandpa" :15,
- "Marlon" :15,
- "Mister Qi" :10,
- "SYSTEM" :7,
- "Gil" :2

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/StardewValley/StardewValley/,False,Stardew Valley,Stardew Valley,TOTAL,4991,53870,15560,64438,-0.12491136306914363,102.12449866275713,5.947651431681431,40
../data/StardewValley/StardewValley/,False,Stardew Valley,Stardew Valley,playerChoice,127,745,270,900,-0.25885533184190734,101.83300956997266,6.48627201093711,1
../data/StardewValley/StardewValley/,False,Stardew Valley,Stardew Valley,male,2606,28967,8716,34756,-0.1356553949927637,101.95457088430042,6.021001650294626,24
../data/StardewValley/StardewValley/,False,Stardew Valley,Stardew Valley,female,2233,23900,6505,28449,-0.11115243825959276,102.40347370706151,5.837080391973988,14
../data/StardewValley/StardewValley/,False,Stardew Valley,Stardew Valley,undefined,25,258,67,333,1.142023602915657,93.73346928149948,6.520365231979636,1

```


### 数据来源脚本 (scraper.py)

```python
import time,os
from google_drive_downloader import GoogleDriveDownloader as gdd

sources = [('0BwyXuxAqGS7uZU5VVXdUMXVrMVk', 'Abigail.yaml' ),
 ('0BwyXuxAqGS7uNWY5U2NIOXItRWs', 'Alex.yaml' ),
 ('0BwyXuxAqGS7ueVRUSlVuN3c5Mk0', 'Caroline.yaml' ),
 ('0BwyXuxAqGS7ubWc3eUZnRjk4dkU', 'Clint.yaml' ),
 ('0BwyXuxAqGS7uNnduc2pBdzdDNzg', 'Demetrius.yaml' ),
 ('0BwyXuxAqGS7uZld0VUxydFBxelk', 'Dwarf.yaml' ),
 ('0BwyXuxAqGS7uZk1OTVY0SWdHSGc', 'Elliott.yaml' ),
 ('0BwyXuxAqGS7ud1BWOEFEYU9nLXM', 'Emily.yaml' ),
 ('0BwyXuxAqGS7uYXowVVJiUlczMEE', 'Evelyn.yaml' ),
 ('0BwyXuxAqGS7uczR0T09vYjJLNXM', 'George.yaml' ),
 ('0BwyXuxAqGS7uWFgyRXhneXk1VWc', 'Gil.yaml' ),
 ('0BwyXuxAqGS7uRnRWdlFCd1RDZGs', 'Gus.yaml' ),
 ('0BwyXuxAqGS7uaGQwRnFSTS12VHc', 'Haley.yaml' ),
 ('0BwyXuxAqGS7ubUlfX3NoX1B6bmM', 'Harvey.yaml' ),
 ('0BwyXuxAqGS7uUHVxSVkzZ0ZMb1U', 'Jas.yaml' ),
 ('0BwyXuxAqGS7uNy1tbDJMNDRLS2c', 'Jodi.yaml' ),
 ('0BwyXuxAqGS7uVkNmRmhmUlhObnc', 'Kent.yaml' ),
 ('0BwyXuxAqGS7uejc4X2luZExfZms', 'Krobus.yaml' ),
 ('0BwyXuxAqGS7ucFdNNVNPYXprc0k', 'Leah.yaml' ),
 ('0BwyXuxAqGS7uV0REN1hDS0cyWUE', 'Lewis.yaml' ),
 ('0BwyXuxAqGS7uak9jQ1NIMzJudWc', 'Linus.yaml' ),
 ('0BwyXuxAqGS7uUHlRSzVYSWVwVnc', 'Marnie.yaml' ),
 ('0BwyXuxAqGS7uSFdtNkhnM1FlOWc', 'MarriageDialogue.yaml' ),
 ('0BwyXuxAqGS7uQ1Rsb1RyekVzcTA', 'MarriageDialogueAbigail.yaml' ),
 ('0BwyXuxAqGS7uVWhwcFFCRERuUzA', 'MarriageDialogueAlex.yaml' ),
 ('0BwyXuxAqGS7uUUhzN2trMndvQk0', 'MarriageDialogueElliott.yaml' ),
 ('0BwyXuxAqGS7uRUZ3dkV0Y2Z0MUE', 'MarriageDialogueEmily.yaml' ),
 ('0BwyXuxAqGS7uajBHZEZsSU51d2s', 'MarriageDialogueHaley.yaml' ),
 ('0BwyXuxAqGS7udEFLQWIteFVOVlE', 'MarriageDialogueHarvey.yaml' ),
 ('0BwyXuxAqGS7uekx3eXdyLWcxY28', 'MarriageDialogueLeah.yaml' ),
 ('0BwyXuxAqGS7uU2xEbEdkOHNVbVE', 'MarriageDialogueMaru.yaml' ),
 ('0BwyXuxAqGS7uMEp1VW4wSlhEZFU', 'MarriageDialoguePenny.yaml' ),
 ('0BwyXuxAqGS7uYndqYVdpbGNCRUk', 'MarriageDialogueSam.yaml' ),
 ('0BwyXuxAqGS7uOXpuY3VIUjlVVTA', 'MarriageDialogueSebastian.yaml' ),
 ('0BwyXuxAq
```


## 策划参考价值
模拟经营RPG类型的对话叙事参考。ConcernedApe的田园模拟，NPC日程+好感度
