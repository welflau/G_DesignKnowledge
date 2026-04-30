# 质量效应 · MassEffectAndromeda（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffectAndromeda》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffectAndromeda
- **品类**：科幻RPG
- **说明**：BioWare科幻RPG，跨三部曲选择延续

### 元数据 (meta.json)

```json
{
  "game": "Mass Effect: Andromeda",
  "series": "Mass Effect",
  "year": 2017,
  "status": "in progress",
  "source": "http://www.masseffectlore.com/transcripts/mass-effect-andromeda-transcripts/",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "MassEffectAParser",
    "fileType": ".html",
    "mainCharName": "RYDER"
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

### 角色列表（共78个）

- "ACTION" :821,
- "RYDER" :434,
- "LIAM" :208,
- "CHOICE" :127,
- "CORA" :118,
- "ALEC RYDER" :78,
- "SAM" :56,
- "DIRECTOR TANN" :46,
- "KESH" :35,
- "TECHNICIAN" :35,
- "KIRKLAND" :34,
- "LEXI" :33,
- "KANDROS" :30,
- "FISHER" :26,
- "GREER" :26,
- "CAPTAIN DUNN" :25,
- "ADDISON" :24,
- "LANI" :17,
- "WELCOME VID" :14,
- "RAJ PATIL" :13,
- "CREW 1" :13,
- "DR. CARLYLE" :12,
- "CREW 2" :12,
- "CREW" :11,
- "PROFESSOR HERIK" :9,
- "AVINA" :8,
- "CASSIDY SHAW" :7,
- "DOCTOR ARIDANA" :7,
- "CHIEF LUCAN" :7,
- "OPERATIONS MANAGER" :7,
- "ALIEN" :7,
- "SETTLER" :7,
- "HAYES" :7,
- "DALE ATKINS" :6,
- "RENSUS" :6,
- "SAM (PRIVATE)" :6,
- "GENERAL LOGS OPTIONS" :5,
- "MARIETTE" :5,
- "NEXUS CONTROL" :5,
- "GREER (VOICE-OVER)" :5,
- "DR. T'SONI" :4,
- "ZARAH KELLUS" :4,
- "MELO" :4,
- "JIEN GARSON" :4,
- "BRIDGE CREW" :4,
- "TECHNICIAN 1" :4,
- "SERGEANT AKER" :3,
- "WORKER" :3,
- "ENGINEER" :3,
- "-Asari archaeologist" :2,
- ... 共78个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffectAndromeda/,True,Mass Effect: Andromeda,Mass Effect,TOTAL,1470,17279,4008,21594,0.8380959983788454,96.7324618935201,7.060602785135209,76
../data/MassEffect/MassEffectAndromeda/,True,Mass Effect: Andromeda,Mass Effect,male,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffectAndromeda/,True,Mass Effect: Andromeda,Mass Effect,female,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffectAndromeda/,True,Mass Effect: Andromeda,Mass Effect,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

pages = ["http://www.masseffectlore.com/transcriptsfiles/mea/MEA-introduction.htm","http://www.masseffectlore.com/transcriptsfiles/mea/MEA-PROLOGUE_HYPERION.htm","http://www.masseffectlore.com/transcriptsfiles/mea/MEA-PROLOGUE_HYPERION-ADS1.htm","http://www.masseffectlore.com/transcriptsfiles/mea/MEA-PLANETSIDE.htm","http://www.masseffectlore.com/transcriptsfiles/mea/MEA-NEXUSREUNION-FULLTRANSCRIPT.htm"]

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
