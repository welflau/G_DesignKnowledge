# 最终幻想 · FFVII_Remake（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFVII_Remake》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFVII_Remake
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy VII Remake",
  "series": "Final Fantasy",
  "year": 2020,
  "status": "ready",
  "source": "https://finalfantasy.fandom.com/wiki/Final_Fantasy_VII_Remake_script",
  "sourceFeatures": {
    "type": "wiki",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "N/A",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "FFVII_RemakeParser",
    "fileType": ".html",
    "scriptHasOptionalDialogueSection": false,
    "scriptStartCue": "<span class=\"mw-headline\" id=\"Chapter_1:_The_Destruction_of_Mako_Reactor_1\">Chapter 1: The Destruction of Mako Reactor 1</span>",
    "scriptEndCue": "<span class=\"mw-headline\" id=\"Notifications\">Notifications</span>",
    "ignoreCharacters": [
      "On-Screen",
      "On-screen"
    ]
  },
  "mainPlayerCharacters": [
    "Cloud",
    "Aerith",
    "Tifa",
    "Barret",
    "Yuffie"
  ],
  "characterGroups": {
    "male": [
      "Andrea",
      "Beck",
      "Betty's Dad",
      "Biggs",
      "Burke",
      "Barret",
      "Butch",
      "Chadley",
      "Cloud",
      "Damon",
      "Don Corneo",
      "Heidegger",
      "Hojo",
      "Jay",
      "Johnny",
      "Jules",
      "Kotch",
      "Scotch",
      "Leslie",
      "Moggie",
      "Narjin",
      "Oates",
      "Palmer",
      "President Shinra",
      "Red XIII",
      "Reeve",
      "Reno",
      "Roche",
      "Ronnie",
      "Rude",
      "Rufus",
      "Sam",
      "Scotch",
      "Sephiroth",
      "Tseng",
      "Wedge",
      "Wymer",
      "Zack",
      "Domino",
      "Old Snapper",
      "Boy",
      "Boy (1)",
      "Boy (2)",
      "Boy (3)",
      "Boy (4)",
      "Boy (In Cloud'S Memory)",
      "Boy (Vision)",
      "Boy (Vision, 2)",
      "Honeyboy",
      "Johnny's father",
      "Kind Old Man",
      "Loitering Man",
      "Man In Line",
      "Man In Love",
      "Old Man",
      "Scared Man",
      "Sweet Old Man",
      "Womanizer",
      "3-C Soldier",
      "Air Traffic Controller",
      "Beastmaster",
      "Avalanche Helicopter",
      "Shinra Helicopter",
      "Security Officer (1)",
      "Security Officer (2)",
      "Security Officer",
      "Security Officer (3)",
      "Security Officer (4)",
      "Security Officer (5)",
      "Security Officer (6)",
      "Security Officer (7)",
      "Security Officer (8)",
      "Security Officer (Computer)",
      "Senior Officer",
      "New Recruit",
      "Neighborhood Watch Member (1)",
      "Neighborhood Watch Member (2)",
      "Bandit (1)",
      "Bandit (2)",
      "Bandit",
      "Barker",
      "Clothing Store Owner",
      "Clothing Store Owner'S Son",
      "Researcher (1)",
      "Researcher (2)",
      "Subordinate",
      "Honeybee Receptionist",
      "Guide",
      "Collaborator",
      "Corneo Lackey (1)",
      "Corneo Lackey (2)",
      "Corneo Lackey",
      "Customer",
      "DJ",
      "Doctor",
      "Elite Grenadier",
      "Elite Security Officer",
      "Elite Shock Trooper",
      "Flametrooper",
      "Gatekeeper",
      "Grenadier",
      "Hart",
      "Helitrooper",
      "Hoodlum (1)",
      "Hoodlum (2)",
      "Hoodlum (3)",
      "Hoodlum",
      "Item Store Owner",
      "Junk Dealer",
      "Man",
      "Materia Vendor",
      "Pharmacist",
      "Patient",
      "Restaurant Owner",
      "Host",
      "Shinra Employee (lift)",
      "Shinra Employee (table)",
      "Shinra Employee (phone)",
      "Shinra Middle Manager",
      "Shinra Employee (vent 1)",
      "Shinra Employee (train 2)",
      "Shinra Employee (tips)",
      "Shinra Employee (vending)",
      "Spectator (male 1)",
      "Spectator (male 2)",
      "Spectator (male 3)",
      "Spectator (male 4)",
      "Engineering Officer",
      "Souvenir Shop Owner",
      "Innkeeper",
      "Guest",
      "Mobile Officer",
      "Mobile Unit Officer",
      "Mobile Unit Officer (1)",
      "Mobile Unit Officer (2)",
      "Weapons Vendor",
      "Announcer (Anchor)",
      "Station Worker",
      "Stablehand",
      "Singer",
      "Neighborhood Watch Member (Male 1)",
      "Neighborhood Watch Member (Male 2)",
      "Neighborhood Watch Member (Male 3)",
      "Neighborhood Watch Member (Male 4)",
      "Radio",
      "Soldier",
      "Undercity Resident (Posters)",
      "Undercity Resident (Crash)",
      "Undercity Resident (Male 1)",
      "Undercity Resident (Male 2)",
      "Undercity Resident (Older Man with Glasses)",
      "Undercity Resident (Male 3)",
      "Undercity Resident (Server)",
      "Undercity Resident (Male 4)",
      "Undercity Resident (Older Man)",
      "Undercity Resident (Male 5)",
      "Undercity Resident (Male 6)",
      "Undercity Resident (Male 7)",
      "Undercity Resident (Male 8)",
    
```

### 角色列表（共291个）

- "ACTION" :1940,
- "Cloud" :1530,
- "Barret" :1112,
- "Tifa" :981,
- "Aerith" :863,
- "Yuffie" :359,
- "CHOICE" :319,
- "STATUS" :313,
- "Jessie" :301,
- "LOCATION" :266,
- "Biggs" :205,
- "Wedge" :193,
- "Johnny" :135,
- "Sonon" :133,
- "Security Officer" :113,
- "Madam M" :103,
- "Red XIII" :97,
- "Kotch" :91,
- "Reno" :87,
- "Leslie" :78,
- "Heidegger" :75,
- "Scotch" :69,
- "Chadley" :59,
- "Sam" :55,
- "Marle" :55,
- "Nayo" :54,
- "Announcement" :54,
- "Scarlet" :53,
- "Elmyra" :46,
- "Sephiroth" :45,
- "Security Officer (1)" :44,
- "Mireille" :43,
- "Don Corneo" :42,
- "Hojo" :41,
- "Wymer" :41,
- "President Shinra" :39,
- "Rude" :38,
- "Jules" :35,
- "Gatekeeper" :35,
- "Roche" :35,
- "Security Officer (2)" :35,
- "Boy" :33,
- "Betty" :32,
- "Kyrie" :31,
- "Marlene" :31,
- "Damon" :29,
- "New Recruit" :29,
- "Zhijie" :27,
- "Andrea" :27,
- "Oates" :27,
- ... 共291个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFVII_Remake/,False,Final Fantasy VII Remake,Final Fantasy,TOTAL,8897,86487,24793,102108,-0.2982606430584429,103.41413468275027,6.50645856153525,286
../data/FinalFantasy/FFVII_Remake/,False,Final Fantasy VII Remake,Final Fantasy,male,5622,54337,15285,64463,-0.20458482053707527,102.86107586295148,6.62548241263007,208
../data/FinalFantasy/FFVII_Remake/,False,Final Fantasy VII Remake,Final Fantasy,female,3268,32126,9491,37620,-0.45192577386639066,104.33154013143762,6.299255809289617,75
../data/FinalFantasy/FFVII_Remake/,False,Final Fantasy VII Remake,Final Fantasy,neutral,7,24,16,25,-2.713333333333331,117.1875,14.895483333333333,3

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen

page = "https://finalfantasy.fandom.com/wiki/Final_Fantasy_VII_Remake_script"
html = urlopen(page).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
