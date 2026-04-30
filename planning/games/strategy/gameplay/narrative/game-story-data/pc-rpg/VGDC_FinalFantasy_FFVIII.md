# 最终幻想 · FFVIII（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFVIII》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFVIII
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Final Fantasy VIII",
  "series": "Final Fantasy",
  "year": 1999,
  "status": "ready",
  "source": "https://www.neoseeker.com/finalfantasy8/faqs/136092-final-fantasy-viii-script-a.html",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "2",
    "truePositive_notes": "Source is comprehensive for mandatory dialogue, but doesn't cover all sidequests or optional dialogue.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "FF8Parser",
    "parentheticalsThatShouldStayInParentheses": [
      "(gulp)",
      "(She walks off.)",
      "(Dialogue cancelled; cannot enter Fire Cavern)",
      "(Hmmm...)",
      "(sigh)",
      "(Squall jumps off.)",
      "(No one jumps off.)",
      "(They all get on.)",
      "(They don't take the lift.)",
      "(Selphie runs away to someone else.)",
      "(He gives Squall a 'Pet Pals Vol. 1' magazine.)",
      "(Zell suppresses his frustration and Selphie walks in.)",
      "(Insert R2 here.)",
      "(This comes up seven times, so it's probably not the same person thinking it.)",
      "(sigh...)",
      "(cough)",
      "(Break)",
      "(Same as R1)",
      "(See below.)",
      "(Rinoa repeats herself, from First, I'll go over the model... to where the narrative lists all seven steps in order.)",
      "(Rinoa repeats the dialogue from Ok, now let's talk... to That's about it for the sensors.)",
      "(Rinoa repeats the dialogue from Next, let's talk about how... to That about covers the uncoupling process.)",
      "(Rinoa repeats R3, R4, and R5 in sequential order.)",
      "(Cancels dialogue; Squall and co. can run around train.)",
      "(Initiates the mission.)",
      "(Same dialogue recital as last time.)",
      "(Dialogue cancelled.)",
      "(Rinoa enters Vinzer's cabin.)",
      "(hereafter referred to as 'Party A')",
      "(hereafter referred to as 'Party B')",
      "(hereafter referred to as 'Party C')",
      "(hic)",
      "(Squall doesn't say another word on the subject.)",
      "(They don't get on; they can walk around freely)",
      "(Self-explanitory, the scene ends and the party gets off at East Academy)",
      "(Self-explanitory, the scene doesn't advance and the train doesn't rumble on yet.)",
      "(leaving)",
      "(pursuing)",
      "(list of numbers, from 0 - 9)",
      "(Already covered; look above)",
      "(huff huff...puff puff...)",
      "(s)",
      "(See below)",
      "(Nothing happens; can move around freely)",
      "(The lion-thing gets kicked and then, after looking at the Mean Guy, leaves with him.)",
      "(This line to Zell's (Doesn't sound...)",
      "(Squall can change up the parties again.)",
      "(Selphie's team beats the crap out of the soldiers, no questions asked, but afterwards, they're not able to hide in their uniforms.)",
      "(Insert R4, sans Selphie's opening line.)",
      "(Selphie's team flees.)",
      "(The party initiates battle.)",
      "(The battle starts after this.)",
      "(Same as R1, with the minute until destruction changed.)",
      "(Squall jumps between the two, gunblade flashing.)",
      "(The screen blacks out and it's assumed that they've killed the SeeD and her two junior classmen.)",
      "(R3 is repeated.)",
      "(Begin after this message)",
      "(sic)",
      "(Irvine picks which instrument Zell plays.)",
      "(He chooses another instrument for himself.)",
      "(Irvine finds her another instrument.)",
      "(She's given a different instrument to play.)",
      "(The orphanage scenes end.)",
      "(If Squall gives absolutely no orders, he'll say:)",
      "(Squall just gets pushed back against the door.)",
      "(This opens up the previously unavailable R4 and R5 options)",
      "(The battle starts.)",
      "(The party can run back to a save point.)",
      "(The party goes to the menu screen.)",
      "(They sit down and are taken for a ride.)",
      "(They don't sit down.)",
      "(They aren't allowed to go in.)",
      "(20 minutes)",
      "(And standing next to her, a very excited Irvine...)",
      "(Segway into R7, at 'There iz only...' now.)",
      "(Squall can ask the previous five questions again, except this time Laguna will answer R1, like so:)",
      "(They enter.)",
      "(They don't enter.)",
      "(NOTE: If you didn't show her around, she begins at I'm...a messenger, obviously not recognizing Squall.)"
    ]
  },
  "mainPlayerCharacters": [
    "Squall",
    "Rinoa",
    "Quistis",
    "Zell",
    "Selphie",
    "Irvine"
  ],
  "characterGroups": {
    "male": [
      "Squall",
      "Zell",
      "Irvine",
      "Cid",
      "Biggs",
      "Odine",
      "Kiros",
      "Laguna",
      "Mark",
      "Martine",
  
```

### 角色列表（共150个）

- "ACTION" :1446,
- "Squall" :989,
- "Zell" :403,
- "Rinoa" :391,
- "Selphie" :338,
- "Quistis" :302,
- "STATUS" :283,
- "Laguna" :242,
- "CHOICE" :222,
- "Irvine" :193,
- "Seifer" :116,
- "Kiros" :78,
- "Edea" :76,
- "Cid" :73,
- "Garden Faculty" :50,
- "Ellone" :47,
- "Raijin" :44,
- "Zone" :41,
- "Watts" :38,
- "Ward" :36,
- "LOCATION" :36,
- "Odine" :34,
- "Galbadian Soldier" :30,
- "Xu" :28,
- "Dr. Kadowaki" :28,
- "Fujin" :27,
- "Esthar Airstation" :25,
- "Julia" :25,
- "Tutorial" :23,
- "General Caraway" :22,
- "Nida" :21,
- "Soldier" :21,
- "Warden" :18,
- "Caraway's Guard" :18,
- "Biggs" :18,
- "Maintenance Soldier" :17,
- "Guard" :17,
- "Raine" :17,
- "Mayor Dobe" :16,
- "Security Guard" :15,
- "Doctor's Assistant" :14,
- "NORG" :14,
- "Ultimecia" :13,
- "Wedge" :13,
- "Director" :11,
- "Mean Guy" :11,
- "Loudspeaker" :11,
- "Piet" :10,
- "White SeeD Leader" :10,
- "President Deling" :10,
- ... 共150个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFVIII/,False,Final Fantasy VIII,Final Fantasy,TOTAL,4189,51368,18538,62746,-0.09562954479876318,100.68359845569232,6.7617684634812925,144
../data/FinalFantasy/FFVIII/,False,Final Fantasy VIII,Final Fantasy,male,2785,33147,12657,40511,-0.14713161600604963,100.78195449879354,6.718892863250391,93
../data/FinalFantasy/FFVIII/,False,Final Fantasy VIII,Final Fantasy,female,1310,15749,5397,18868,-0.315016987411358,102.5185763154295,6.593540259825502,28
../data/FinalFantasy/FFVIII/,False,Final Fantasy VIII,Final Fantasy,neutral,94,2472,483,3367,2.478274035659007,86.41036302237234,8.470219921003435,23

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

page = "https://www.neoseeker.com/finalfantasy8/faqs/136092-final-fantasy-viii-script-a.html"

req = Request(
    page, 
    headers={
        'User-Agent': 'XYZ/3.0'
    }
)

html = urlopen(req, timeout=10).read().decode('utf-8')
o = open("raw/page01.html",'w')
o.write(html)
o.close()
```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
