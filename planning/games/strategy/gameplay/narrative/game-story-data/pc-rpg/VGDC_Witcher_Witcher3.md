# 巫师 · Witcher3（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：巫师, ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：ARPG


> ⚠️ **数据状态：索引条目** — 本条目仅包含游戏meta信息和角色列表，完整对话数据需运行VideoGameDialogueCorpus的scraper脚本生成。

## 概述
巫师系列《Witcher3》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：巫师（Witcher）
- **游戏**：Witcher3
- **品类**：ARPG
- **说明**：CDPR开放世界ARPG，分支叙事+灰色道德选择

### 元数据 (meta.json)

```json
{
  "game": "The Witcher 3: Wild Hunt",
  "series": "The Witcher",
  "year": 2015,
  "status": "in progress",
  "source": "https://raw.githubusercontent.com/thetobysiu/witcher-3-data-pre-processing",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "Witcher3Parser",
    "fileType": ".txt"
  },
  "mainPlayerCharacters": [],
  "characterGroups": {
    "male": [],
    "female": [],
    "neutral": []
  },
  "aliases": {}
}
```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
from urllib.error import HTTPError
#from bs4 import BeautifulSoup
import re,time
import os


def openPage(url):
	req = Request(
		url, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)
	html = urlopen(req).read().decode('utf-8')
	#html = BeautifulSoup(html, 'lxml')
	#html = html.find("main")
	return(html)
	

url = "https://raw.githubusercontent.com/thetobysiu/witcher-3-data-pre-processing/refs/heads/master/w3dialog_id.txt"

html = openPage(url)

o = open("raw/w3dialog_id.txt",'w')
o.write(html)
o.close()
```


## 策划参考价值
ARPG类型的对话叙事参考。CDPR开放世界ARPG，分支叙事+灰色道德选择
