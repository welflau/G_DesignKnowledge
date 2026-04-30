# 最终幻想 · FFVII（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFVII》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFVII
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy VII",
  "series": "Final Fantasy",
  "year": 1997,
  "status": "ready",
  "source": "http://www.yinza.com/Fandom/Script/",
  "sourceFeatures": {
    "type": "fan transcript",
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
    "parser": "FFVIIParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Cloud",
    "Barret",
    "Tifa",
    "Cait Sith",
    "Aerith",
    "Yuffie",
    "Red XIII",
    "Vincent",
    "Cid"
  ],
  "characterGroups": {
    "male": [
      "Cloud",
      "Barret",
      "Biggs",
      "Bugenhagen",
      "Butch",
      "Cait Sith",
      "Cid",
      "Dio",
      "Don Corneo",
      "Dyne",
      "Elder Bugah",
      "Elder Hargo",
      "Heidegger",
      "Hojo",
      "Holzoff",
      "Joe",
      "Johnny",
      "King",
      "Kotch",
      "Mukki",
      "Palmer",
      "President Shinra",
      "Reeve",
      "Reno",
      "Rude",
      "Rufus",
      "Scotch",
      "Sephiroth",
      "Tseng",
      "Vincent",
      "Wedge",
      "Zack",
      "Zangan",
      "Bald Black Man",
      "Bald Man",
      "Bald Man in Suspenders",
      "Rocket Town Barkeeper",
      "Turtle's Paradise Barkeeper",
      "Icicle Inn Barkeeper",
      "Junon Barkeeper",
      "Cosmo Canyon Barkeeper",
      "Kalm Barkeeper",
      "Wall Market Barkeeper",
      "Bar del Sol Barkeeper",
      "Bartender",
      "Big Bald Man",
      "Big Man",
      "Billy",
      "Black Man",
      "Black Surfer",
      "Black-haired Man",
      "Blond Man",
      "Choco Bill",
      "Choco Billy",
      "Chocobo Sage",
      "Boy",
      "Brown-haired Guy",
      "Captain",
      "Clone",
      "Clone #11",
      "Clone #12",
      "Clone #4",
      "Clone #5",
      "Clone #6",
      "Clone #9",
      "Clone 2",
      "Clones",
      "Small Clone",
      "Smaller Clone",
      "Commander",
      "Corneo",
      "Dark-clothed Man",
      "Dark-haired Man",
      "Delinquent Soldier",
      "Doctor",
      "Domino",
      "Doorman",
      "Downed Man",
      "EDK",
      "Fisherman",
      "Godo",
      "Gorky",
      "Guy",
      "Guy Near Mog Game",
      "Guy Near Submarine Game",
      "Guy Outside",
      "Guy on Motorcycle Game",
      "Guy on Snowboard Game",
      "Hart",
      "Johnny's Cousin",
      "Johnny's Dad",
      "Knight",
      "Large Man",
      "Little Boy",
      "Man",
      "Man 1",
      "Man 2",
      "Man 3",
      "Man 4",
      "Man 5",
      "Man Betting",
      "Man Cooking Outside",
      "Man Following",
      "Man Lifting Weights",
      "Man Looking at Painting",
      "Man Looking at Paintings",
      "Man Near Gate",
      "Man Near Sea Plane",
      "Man Outside Dress Shop",
      "Man Outside Godo's House",
      "Man Outside Restaurant",
      "Man Practicing Kicks",
      "Man Sitting Down",
      "Man Swimming",
      "Man Upstairs",
      "Man Using Punching Bag",
      "Man Waiting Outside Bathroom",
      "Man with camera",
      "Man at Table",
      "Man by Fence",
      "Man by Furnace",
      "Man in Bathroom",
      "Man in Blue",
      "Man in Corner",
      "Man in Hardhat",
      "Man in Hat",
      "Man in Nap Room",
      "Man in Overalls",
      "Man in Straw Hat",
      "Man in Thicket",
      "Man in Yard",
      "Man on Beach",
      "Man on Roof of Small House",
      "Man on Treadmill",
      "Man on the Beach",
      "Man on the Path to Godo's House",
      "Man outside Godo's House",
      "Man outside Honey Bee Inn",
      "Man with Hat",
      "Man with Head on Table",
      "Men",
      "Men Doing Squats",
      "Men on the Beach",
      "Mr. Coates",
      "Mr. Hangman",
      "Naked Man 1",
      "Naked Man 2",
      "Naked Man 3",
      "Old Man",
      "Old Man Playing with Dog",
      "Old Man Upstairs",
      "Old Man at Entrance",
      "Old Man outside Item Shop",
      "Older Man",
      "Red XIII",
      "Shinra Manager",
      "Station Man",
      "Gramps",
      "Shake",
      "Staniv",
      "Tanned Man",
      "Three Guys Posing",
      "Voice in Cloud's head",
      "Wizard",
      "Zack's Father",
      "Clothing Shop Owner",
      "Redhead in Suit",
      "Wutai Item Shopkeeper",
      "Tifa's Father",
      "Beautiful Bro",
      "Arguing Man",
      "Boys",
      "Bulletin",
      "Bystanders",
      "Carriage Driver",
      "Cat Kid",
      "Crew",
      "Crew Member",
      "Crew Member 2",
      "Crew Member 3",
      "Crew Member 4",
      "Customer",
      "Driver",
      "Elevator Guard",
      "Excavator",
      "Excavator 2",
      "Excavator 3",
      "Head Excavator",
      "Pilot",
      "Taxi Pilot",
      "Gatekeeper",
      "General Sto
```

### 角色列表（共442个）

- "ACTION" :2656,
- "Cloud" :1615,
- "STATUS" :1116,
- "Tifa" :813,
- "Barret" :674,
- "CHOICE" :573,
- "Aerith" :509,
- "Cid" :356,
- "Yuffie" :341,
- "Red XIII" :317,
- "LOCATION" :309,
- "Cait Sith" :246,
- "Vincent" :182,
- "Man" :140,
- "Sephiroth" :116,
- "Bugenhagen" :92,
- "Woman" :74,
- "Reno" :67,
- "EDK" :63,
- "Hojo" :62,
- "Soldier" :54,
- "Rufus" :52,
- "Narrator" :51,
- "Elena" :50,
- "Commander" :48,
- "Don Corneo" :47,
- "King" :45,
- "Scarlet" :44,
- "Old Man" :43,
- "Tseng" :42,
- "Heidegger" :40,
- "Rude" :39,
- "Voice in Cloud's head" :34,
- "Girl" :33,
- "Shera" :32,
- "Narration" :32,
- "Jessie" :32,
- "Godo" :31,
- "Wizard" :30,
- "Dyne" :29,
- "Corneo" :28,
- "President Shinra" :28,
- "Boy" :27,
- "Soldiers" :26,
- "Redhead" :26,
- "Dio" :25,
- "Elmyra" :25,
- "Johnny" :24,
- "Wedge" :23,
- "Biggs" :23,
- ... 共442个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFVII/,False,Final Fantasy VII,Final Fantasy,TOTAL,8379,100584,43409,117973,-0.8463334935330131,105.25743994648761,6.390788153939179,437
../data/FinalFantasy/FFVII/,False,Final Fantasy VII,Final Fantasy,male,5842,71838,30540,84142,-0.8515826401260504,105.35765472337319,6.464406367832316,291
../data/FinalFantasy/FFVII/,False,Final Fantasy VII,Final Fantasy,female,2300,25102,11383,29191,-1.0077992953819113,106.21575369225529,6.105383648409998,81
../data/FinalFantasy/FFVII/,False,Final Fantasy VII,Final Fantasy,system,3,64,12,80,1.2400000000000002,95.67166666666668,6.121502083333334,2
../data/FinalFantasy/FFVII/,False,Final Fantasy VII,Final Fantasy,ambiguous,4,27,21,37,1.081798941798942,89.59666666666666,9.548419576719574,1
../data/FinalFantasy/FFVII/,False,Final Fantasy VII,Final Fantasy,neutral,230,3553,1450,4523,0.3871374380077057,96.6513618632142,6.904482360977124,62

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import urlopen
import time
from os import path

base = "http://www.yinza.com/Fandom/Script/"

pageNum = 1
for pageNum in range(48):
	pageNum += 1
	urlx = "http://www.yinza.com/Fandom/Script/" + str(pageNum).zfill(2) + ".html"
	fileName = "raw/page_"+str(pageNum).zfill(2)+".html"
	if not path.exists(fileName):
		html = urlopen(urlx).read().decode('utf-8')
		o = open(fileName,'w')
		o.write(html)
		o.close()
		time.sleep(2)


```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
