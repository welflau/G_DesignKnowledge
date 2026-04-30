# 哈迪斯 · Hades（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：哈迪斯, 肉鸽ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：肉鸽ARPG

## 概述
哈迪斯系列《Hades》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：哈迪斯（Hades）
- **游戏**：Hades
- **品类**：肉鸽ARPG
- **说明**：Supergiant的肉鸽叙事标杆，死亡循环叙事

### 元数据 (meta.json)

```json
{
  "game": "Hades",
  "series": "Hades",
  "year": 2018,
  "status": "in progress",
  "source": "https://hades-dialogue-resources.carrd.co/",
  "alternativeMeasure": true,
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "None"
  },
  "parserParameters": {
    "parser": "HadesParser2",
    "fileType": ".lua"
  },
  "mainPlayerCharacters": [
    "Zagreus"
  ],
  "characterGroups": {
    "male": [
      "Hades",
      "Achilles",
      "Charon",
      "Hypnos",
      "Orpheus",
      "Patroclus",
      "Sisyphus",
      "Storyteller",
      "Thanatos",
      "Zagreus",
      "Ares",
      "Dionysus",
      "Hermes",
      "Poseidon",
      "Zeus",
      "Asterius",
      "Skelly",
      "Theseus",
      "Bouldy"
    ],
    "female": [
      "Eurydice",
      "Megaera",
      "Nyx",
      "Dusa",
      "Persephone",
      "Aphrodite",
      "Artemis",
      "Athena",
      "Demeter",
      "Alecto",
      "Tisiphone"
    ],
    "genderless": [
      "Chaos"
    ],
    "neutral": [],
    "droppedMale": [
      "DROPPED_Ares",
      "DROPPED_Hades",
      "DROPPED_Hypnos",
      "DROPPED_Megaera",
      "DROPPED_Minotaur",
      "DROPPED_Nyx",
      "DROPPED_Orpheus",
      "DROPPED_Patroclus",
      "DROPPED_Poseidon",
      "DROPPED_Sisyphus",
      "DROPPED_Skelly",
      "DROPPED_Storyteller",
      "DROPPED_Thanatos",
      "DROPPED_Theseus",
      "DROPPED_Zagreus",
      "DROPPED_Zeus"
    ],
    "droppedFemale": [
      "DROPPED_Alecto",
      "DROPPED_Artemis",
      "DROPPED_Athena",
      "DROPPED_Cerberus",
      "DROPPED_Demeter",
      "DROPPED_Dusa",
      "DROPPED_Persephone",
      "DROPPED_Tisiphone"
    ]
  },
  "aliases": {
    "Unknown": {
      "Bouldy": [
        ".   .   .   ."
      ],
      "Asterius": [
        "Peaaaaace!"
      ],
      "Megaera": [
        "...the problem that I have with that wretched shade is his attitude.",
        "...I don't know which of them is worse, I swear to you.",
        "...He truly is an idiot, I'll give you that."
      ]
    },
    "Scratch": {
      "Achilles": [
        "Good to see you, lad, despite the circumstances."
      ],
      "Storyteller": [
        "Few tales are told of Hades,",
        "I, however, mean to tell you such a tale."
      ]
    },
    "Minotaur": "Asterius",
    "Intercom": "Hades"
  }
}
```

### 角色列表（共58个）

- "Zagreus" :8594,
- "ACTION" :5247,
- "Hades" :1846,
- "Megaera" :1265,
- "Thanatos" :858,
- "Theseus" :645,
- "Skelly" :608,
- "Dusa" :507,
- "Alecto" :445,
- "Sisyphus" :417,
- "Nyx" :409,
- "Patroclus" :390,
- "Achilles" :381,
- "Asterius" :369,
- "CHOICE" :368,
- "Chaos" :354,
- "Storyteller" :285,
- "Persephone" :284,
- "Hypnos" :271,
- "Orpheus" :264,
- "Eurydice" :237,
- "Tisiphone" :226,
- "Hermes" :218,
- "Poseidon" :208,
- "Ares" :207,
- "Demeter" :199,
- "Artemis" :199,
- "Athena" :190,
- "Zeus" :190,
- "Dionysus" :185,
- "Aphrodite" :182,
- "Charon" :175,
- "DROPPED_Zagreus" :125,
- "Bouldy" :37,
- "LOCATION" :28,
- "DROPPED_Megaera" :16,
- "DROPPED_Alecto" :13,
- "DROPPED_Thanatos" :11,
- "DROPPED_Storyteller" :10,
- "DROPPED_Hades" :9,
- "DROPPED_Hypnos" :7,
- "DROPPED_Dusa" :5,
- "DROPPED_Zeus" :4,
- "DROPPED_Poseidon" :4,
- "DROPPED_Artemis" :3,
- "DROPPED_Skelly" :3,
- "DROPPED_Orpheus" :3,
- "DROPPED_Athena" :3,
- "DROPPED_Theseus" :2,
- "DROPPED_Minotaur" :2,
- ... 共58个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Hades/Hades/,True,Hades,Hades,TOTAL,20874,236985,58011,284936,0.1908025338557504,100.97077941681812,6.35255866268606,55
../data/Hades/Hades/,True,Hades,Hades,male,16148,174521,43932,209203,0.1042612806887746,101.39059904609832,6.353933273979186,19
../data/Hades/Hades/,True,Hades,Hades,female,4142,56686,12663,68377,0.38948599918705007,100.24332360813708,6.297536232441777,11
../data/Hades/Hades/,True,Hades,Hades,genderless,354,4873,950,6298,1.661141155885817,92.28920395195873,6.836357971075852,1
../data/Hades/Hades/,True,Hades,Hades,neutral,0,NA,NA,NA,NA,NA,NA,0
../data/Hades/Hades/,True,Hades,Hades,droppedMale,202,826,417,969,-0.9746248715313452,105.57822544869677,7.2330172063801745,16
../data/Hades/Hades/,True,Hades,Hades,droppedFemale,28,79,48,89,-1.6544541139240483,109.855618407173,7.315854852320675,8

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import requests, io, os
from zipfile import ZipFile

url = "https://drive.google.com/uc?export=download&id=1EI84FH-FOXTh2thpt9GSAMTuzEyoE8TB"

r = requests.get(url)
z = ZipFile(io.BytesIO(r.content))
z.extractall("raw/")

```


## 策划参考价值
肉鸽ARPG类型的对话叙事参考。Supergiant的肉鸽叙事标杆，死亡循环叙事
