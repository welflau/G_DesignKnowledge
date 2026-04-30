# 巫师 · Witcher2（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：巫师, ARPG, 对话语料, PC RPG, 角色对话
> 游戏类型：ARPG


> ⚠️ **数据状态：索引条目** — 本条目仅包含游戏meta信息和角色列表，完整对话数据需运行VideoGameDialogueCorpus的scraper脚本生成。

## 概述
巫师系列《Witcher2》的对话语料数据（角色列表+对话统计+数据来源）

## 正文

> ⚠️ **数据状态**：本条目为语料库索引条目，包含角色列表和数据来源脚本。完整对话数据需运行仓库中的`scraper.py`脚本从Wiki/Fandom抓取生成`data.json`。

## 游戏信息

- **系列**：巫师（Witcher）
- **游戏**：Witcher2
- **品类**：ARPG
- **说明**：CDPR开放世界ARPG，分支叙事+灰色道德选择

### 元数据 (meta.json)

```json
{
  "game": "The Witcher 2: Assassins of Kings",
  "series": "The Witcher",
  "year": 2011,
  "status": "in progress",
  "source": "https://laurelnose.github.io/",
  "alternativeMeasure": true,
  "parserParameters": {
    "parser": "Witcher2Parser",
    "fileType": ".html"
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
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,time

indexpage = "https://laurelnose.github.io/"
html = urlopen(indexpage).read().decode('utf-8')

soup = BeautifulSoup(html,'html5lib')
olx = soup.find("ol")
lis = olx.find_all("li")

pages = [li.find("a") for li in lis]
pages = [x for x in pages if not x is None]



href = [x['href'] for x in pages if not 'hidden' in x]
href = list(set([re.sub("#.+","",x) for x in href]))



for url in href:
	print(url)
	try:
		px = urlopen("https://laurelnose.github.io" + url).read().decode('utf-8')
		nx = "raw/P_" + url.replace("/","") + ".html"
		o = open(nx, 'w')
		o.write(px)
		o.close()
	except:
		print("  ERROR")
	time.sleep(2)
	
```


## 策划参考价值
ARPG类型的对话叙事参考。CDPR开放世界ARPG，分支叙事+灰色道德选择
