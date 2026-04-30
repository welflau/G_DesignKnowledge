# 王国之心 · KingdomHearts3D（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：王国之心, ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：ARPG

## 概述
王国之心系列《KingdomHearts3D》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：王国之心（KingdomHearts）
- **游戏**：KingdomHearts3D
- **品类**：ARPG
- **说明**：Square Enix+Disney的ARPG

### 元数据 (meta.json)

```json
{
  "game": "Kingdom Hearts 3D: Dream Drop Distance",
  "series": "Kingdom Hearts",
  "year": 2012,
  "status": "ready",
  "source": "https://gamefaqs.gamespot.com/3ds/997779-kingdom-hearts-3d-dream-drop-distance/faqs/65008",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "high",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "Repeated for new parsing; same results.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "Repeated for new parsing; same results."
  },
  "parserParameters": {
    "parser": "KingdomHearts3DParser",
    "fileType": ".html",
    "scriptHasOptionalDialogueSection": false,
    "scriptStartCue": "------------------------------------------------------------------------------",
    "scriptEndCue": "Please check out my other Kingdom Hearts scripts:",
    "actionCue": "("
  },
  "mainPlayerCharacters": [
    "Sora",
    "Riku"
  ],
  "characterGroups": {
    "male": [
      "Sora",
      "Riku",
      "Mickey",
      "Joshua",
      "Flynn",
      "Sam",
      "Goofy",
      "Jiminy",
      "Neku",
      "Donald",
      "Yen Sid",
      "Beat",
      "Frollo",
      "Quasimodo",
      "Pete",
      "Phoebus",
      "Xigbar",
      "Xehanort",
      "Pinocchio",
      "Xemnas",
      "CLU",
      "Ansem",
      "Lea",
      "Ansem the Wise",
      "Master Xehanort",
      "Laverne",
      "Hugo",
      "Victor",
      "Roxas",
      "Beagle Boy #3",
      "Beagle Boy #2",
      "Beagle Boy #1",
      "Black Guard",
      "Ienzo",
      "Geppetto",
      "Axel",
      "Aeleus",
      "Braig",
      "Ventus",
      "Terra"
    ],
    "female": [
      "Minnie",
      "Shiki",
      "Quorra",
      "Esmeralda",
      "Rhyme",
      "Maleficent",
      "Blue Fairy",
      "Ursula",
      "Xion",
      "Aqua",
      "Announcer"
    ],
    "neutral": []
  },
  "aliases": {
    "Everyone": {
      "Sora, Goofy, Donald, Riku, Mickey & Yen Sid": [
        "WHOA!"
      ],
      "Sora, Donald, Goofy & Mickey": [
        "And one for all!",
        "And one for all!",
        "All for one, and one for all!",
        "All for one, and one for all!"
      ]
    },
    "???": {
      "Lea": [
        "Where...",
        "What happened to me? Roxas?",
        "That's me.",
        "Dilan, Aeleus, Even, Ienzo -",
        "We're people again. But only the ones who joined the Organization here.",
        "I guess Xehanort doesn't count",
        "Where are they? I've turned this castle upside down.",
        "Hey. Are the other two still out cold?",
        "Gotcha. Well, I guess I'll give the castle grounds a sweep.",
        "So do ya think they were blasted off to some other world, or what?",
        "No, look, okay - the fact is - we're here. We've been recompleted, right? So they should be here too - plain and simple.",
        "What a drag. Could they not have been recompleted at all?",
        "Ah! Forget it.",
        "You know what? I'll bring 'em back myself.",
        "Why do I always get stuck with the icky jobs?",
        "Axel didn't. My name is Lea."
      ],
      "Sam": [
        "Are you a prisoner?",
        "Name's Sam.",
        "We're on the Grid.",
        "Riku!"
      ],
      "CLU": [
        "You're in luck.",
        "Only a precious few are granted Light Cycle battle privileges.",
        "I'll show you."
      ]
    },
    "????": {
      "Neku": [
        "Shut it.",
        "Talk about noise... ",
        "Sora, right?",
        "Looks like you're not a Player.",
        "C'mon, keep up. In the Game.",
        "Players get marked with the time limit. And this Game, I can't afford to lose. I need my Game partner.",
        "What? Time out. Do you trust every total stranger you meet?",
        "Now we're friends? It's not that easy.",
        "Yeah, sounds great. Whatever.",
        "Dream Eaters!",
        "Not me. Them.",
        "Don't let 'em surround us! Let's split up!",
        "Oh uh, and... it's Neku."
      ],
      "Beat": [
        "I gotchu now, Joshua!",
        "Once I take you down, yo, me and Rhyme is goin' back were we belong!"
      ],
      "Pete": [
        "What am I up to?"
      ],
      "Riku": [
        "Sora!",
        "You've gotta wake up... ",
        "Sora, don't chase the dreams. They'll lead you nowhere, just to an abyss you'll never be able to wake up from.",
        "Sora! Don't! You've gotta wake up! Sora!"
      ]
    },
    "?????": {
      "Ansem": [
        "Hey! Is this how you wanted it?",
        "I am... ",
        "That's not my name. I'm not \"Xehanort.\"",
        "My name... is Ansem.",
        "This world has been connected.",
        "That is right."
      ],
      "Rhyme": [
        "Huh?",
        "Umm... I'm not really sure. All I know is that my name is Rhyme."
      ],
 
```

### 角色列表（共52个）

- "ACTION" :830,
- "Sora" :365,
- "Riku" :293,
- "Mickey" :143,
- "Joshua" :68,
- "Flynn" :58,
- "Xehanort" :55,
- "Goofy" :52,
- "Jiminy" :51,
- "Neku" :49,
- "Sam" :48,
- "Donald" :45,
- "Yen Sid" :35,
- "Beat" :34,
- "Frollo" :32,
- "Quasimodo" :31,
- "Phoebus" :30,
- "Pete" :27,
- "Lea" :27,
- "Xigbar" :22,
- "Quorra" :22,
- "Shiki" :21,
- "Minnie" :19,
- "Ansem" :19,
- "Pinocchio" :18,
- "Rhyme" :17,
- "CLU" :16,
- "Xemnas" :16,
- "Esmeralda" :16,
- "Maleficent" :12,
- "Ansem the Wise" :10,
- "Master Xehanort" :10,
- "Blue Fairy" :8,
- "Roxas" :8,
- "Laverne" :8,
- "Hugo" :8,
- "Beagle Boy #3" :6,
- "Beagle Boy #2" :6,
- "Beagle Boy #1" :6,
- "Geppetto" :6,
- "Victor" :6,
- "Ursula" :5,
- "Black Guard" :4,
- "Ienzo" :4,
- "Axel" :4,
- "Aeleus" :2,
- "Braig" :2,
- "Xion" :1,
- "Ventus" :1,
- "Aqua" :1,
- ... 共52个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/KingdomHearts/KingdomHearts3D/,False,Kingdom Hearts 3D: Dream Drop Distance,Kingdom Hearts,TOTAL,1749,18484,4821,21459,-0.3955067360432274,104.72705887096511,6.380883798205579,51
../data/KingdomHearts/KingdomHearts3D/,False,Kingdom Hearts 3D: Dream Drop Distance,Kingdom Hearts,male,1626,17253,4514,20025,-0.4034985146772243,104.76307110793547,6.387730231570753,40
../data/KingdomHearts/KingdomHearts3D/,False,Kingdom Hearts 3D: Dream Drop Distance,Kingdom Hearts,female,123,1231,307,1434,-0.2802912808897169,104.21398476385028,6.285335949692658,11
../data/KingdomHearts/KingdomHearts3D/,False,Kingdom Hearts 3D: Dream Drop Distance,Kingdom Hearts,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *

def loadPage(page):
	req = Request(
		page, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)

	html = urlopen(req).read().decode('utf-8')
	return(html)


#page = "https://transcripts.fandom.com/wiki/Kingdom_Hearts_3D:_Dream_Drop_Distance"
page = "https://gamefaqs.gamespot.com/3ds/997779-kingdom-hearts-3d-dream-drop-distance/faqs/65008"
#html = urlopen(page).read().decode('utf-8')
html = loadPage(page)
o = open("raw/page01.html",'w')
o.write(html)
o.close()

```


## 策划参考价值
ARPG类型的对话叙事参考。Square Enix+Disney的ARPG
