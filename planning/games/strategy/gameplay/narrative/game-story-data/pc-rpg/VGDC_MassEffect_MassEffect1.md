# 质量效应 · MassEffect1（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffect1》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffect1
- **品类**：科幻RPG
- **说明**：BioWare科幻RPG，跨三部曲选择延续

### 元数据 (meta.json)

```json
{
  "game": "Mass Effect",
  "series": "Mass Effect",
  "year": 2007,
  "status": "superseded",
  "alternativeMeasure": true,
  "source": "http://www.masseffectlore.com/transcripts/mass-effect-1-transcripts/",
  "parserParameters": {
    "parser": "MassEffectAParser",
    "fileType": ".html",
    "mainCharName": "SHEPARD"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [],
    "female": [],
    "neutral": []
  },
  "aliases": {
    "White text appears on a black background": "ACTION",
    "": "ACTION"
  }
}
```

### 角色列表（共27个）

- "ACTION" :324,
- "SHEPARD" :144,
- "CHOICE" :84,
- "ASHLEY" :41,
- "ANDERSON" :39,
- "KAIDAN" :25,
- "NIHLUS" :25,
- "JOKER" :21,
- "CHAKWAS" :20,
- "JENKINS" :17,
- "POWELL" :16,
- "COLE" :15,
- "PRESSLY" :12,
- "DR. WARREN" :11,
- "MANUEL" :7,
- "SAREN" :6,
- "FARMER" :4,
- "OFFICIER" :3,
- "CAPTAIN ANDERSON" :3,
- "MATRIARCH BENEZIA" :2,
- "BLAKE" :2,
- "SAREN (to geth)" :1,
- "SHEPARD (to Ashley)" :1,
- "ANDERSON (to Shepard)" :1,
- "ANDERSON (to Nihlus)" :1,
- "ON SCREEN" :1,
- "CORPORAL JENKINS" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffect1/,True,Mass Effect,Mass Effect,TOTAL,419,6609,1357,8345,1.2089487761101108,95.06958250473079,7.144057302233962,25
../data/MassEffect/MassEffect1/,True,Mass Effect,Mass Effect,male,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffect1/,True,Mass Effect,Mass Effect,female,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffect1/,True,Mass Effect,Mass Effect,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

pages = ["http://www.masseffectlore.com/transcriptsfiles/me1/PROLOGUE_FINDTHEBEACON.htm","http://www.masseffectlore.com/transcriptsfiles/me1/PROLOGUE_FINDTHEBEACON-ADS1.htm","http://www.masseffectlore.com/transcriptsfiles/me1/PROLOGUE_FINDTHEBEACON-ADS2.htm"]

pageNum = 0
for page in pages:
	pageNum += 1
	fileName = "raw/page_"+str(pageNum).zfill(3)+".html"
	req = Request(
		page, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)


	html = urlopen(req).read().decode('cp1252').encode('utf-8')#.decode('ISO-8859-1')
	o = open(fileName,'wb')
	o.write(html)
	o.close()
	time.sleep(3)
	#with codecs.open(fileName, "w", "utf-8") as targetFile:
	#	targetFile.write(html)

```


## 策划参考价值
科幻RPG类型的对话叙事参考。BioWare科幻RPG，跨三部曲选择延续
