# 质量效应 · MassEffect3（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffect3》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffect3
- **品类**：科幻RPG
- **说明**：BioWare科幻RPG，跨三部曲选择延续

### 元数据 (meta.json)

```json
{
  "game": "Mass Effect 3",
  "series": "Mass Effect",
  "year": 2012,
  "status": "superseded",
  "alternativeMeasure": true,
  "source": "https://docs.google.com/document/pub?id=1O5sjL4pL0bTs1MNSmsrhAE-4WTTeE0foicqJrHpiOOg#h.n8e48vc5s8nz",
  "parserParameters": {
    "parser": "MassEffect3Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Shepard"
  ],
  "characterGroups": {
    "male": [],
    "female": [],
    "neutral": []
  },
  "aliases": {
    "Gylph": "Glyph"
  }
}
```

### 角色列表（共46个）

- "Shepard" :1351,
- "ACTION" :408,
- "James" :328,
- "Kaidan" :312,
- "Garrus" :310,
- "Liara" :226,
- "Tali" :202,
- "EDI" :163,
- "Ashley" :154,
- "Steve" :122,
- "Javik" :105,
- "Samantha" :80,
- "Joker" :61,
- "Aethyta" :39,
- "Jacob" :39,
- "Anderson" :30,
- "Wrex" :25,
- "Diana" :21,
- "Kasumi" :16,
- "Kenneth" :15,
- "Bau" :15,
- "Legion" :15,
- "Gabby" :13,
- "Thane" :13,
- "Soldier" :10,
- "Kurin" :9,
- "Miranda" :9,
- "Chakwas" :8,
- "Scientist" :7,
- "Illusive Man" :6,
- "Glyph" :6,
- "Udina" :5,
- "Kaidan|Ashley" :5,
- "Victus" :5,
- "Wreav" :4,
- "Robert" :4,
- "Party" :3,
- "NPC" :2,
- "Oriana" :1,
- "Raan" :1,
- "Turian" :1,
- "New turian" :1,
- "New Asari" :1,
- "Asari" :1,
- "Liara|Kaidan|Ashley" :1,
- "Gylph" :1

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffect3/,True,Mass Effect 3,Mass Effect,TOTAL,3740,46712,11608,57385,0.47553249797666375,98.82067016457816,6.744833999754968,45
../data/MassEffect/MassEffect3/,True,Mass Effect 3,Mass Effect,male,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffect3/,True,Mass Effect 3,Mass Effect,female,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffect3/,True,Mass Effect 3,Mass Effect,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time

pages = ["https://docs.google.com/document/pub?id=1O5sjL4pL0bTs1MNSmsrhAE-4WTTeE0foicqJrHpiOOg"]

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


	html = urlopen(req).read()#.decode('cp1252').encode('utf-8')#.decode('ISO-8859-1')
	o = open(fileName,'w')
	o.write(html)
	o.close()
	time.sleep(3)
	#with codecs.open(fileName, "w", "utf-8") as targetFile:
	#	targetFile.write(html)

```


## 策划参考价值
科幻RPG类型的对话叙事参考。BioWare科幻RPG，跨三部曲选择延续
