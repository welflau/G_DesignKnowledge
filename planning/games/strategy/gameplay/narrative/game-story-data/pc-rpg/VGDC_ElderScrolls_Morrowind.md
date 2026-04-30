# 上古卷轴 · Morrowind（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：上古卷轴, 开放世界RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：开放世界RPG

## 概述
上古卷轴系列《Morrowind》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：上古卷轴（ElderScrolls）
- **游戏**：Morrowind
- **品类**：开放世界RPG
- **说明**：Bethesda开放世界RPG，海量NPC对话

### 元数据 (meta.json)

```json
{
  "game": "The Elder Scrolls III: Morrowind",
  "series": "The Elder Scrolls",
  "year": 2002,
  "status": "ready",
  "source": "https://elderscrolls.fandom.com/wiki/",
  "sourceFeatures": {
    "type": "wiki",
    "completeness": "sample",
    "dialogueOrder": false,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "5",
    "truePositive_notes": "This is only a sample of dialogue; many conversations are missing. Previous issues addressed",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "ElderScrollsWikiParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "PC"
  ],
  "characterGroups": {
    "playerChoice": [
      "PC"
    ],
    "male": [
      "Ababael Timsar-Dadisun",
      "Abassel Asserbassalit",
      "Abbard the Wild",
      "Abibaal Assillariran",
      "Abishpulu Shand",
      "Achel",
      "Adairan Lalansour",
      "Adaishah Ahanidiran",
      "Adaves Therayn",
      "Addammus",
      "Addarnat Assardidairan",
      "Adding",
      "Adibael Hainnabibi",
      "Adil Norvayn",
      "Admiral Rolston",
      "Adondasi Sadalvel",
      "Adosi Darano",
      "Aebondeius Jucanis",
      "Aengoth the Jeweler",
      "Agarond",
      "Agning",
      "Ahasour",
      "Ahaz",
      "Ainab Yassabisun",
      "Ainab (Character)",
      "Ainat Maessabibi",
      "Alanil Llaram",
      "Albecius Colollius",
      "Aldaril",
      "Alds Baro",
      "Alfhedil Elf-Hewer",
      "Allding",
      "Allian Carbo",
      "Allimir",
      "Alms Helothren",
      "Alnas Sendu",
      "Alodie Jes",
      "Alof the Easterner",
      "Alusaron",
      "Alveleg",
      "Alven Salas",
      "Alvis Teri",
      "Alvor Andas",
      "Alvos Sadri",
      "Alvur Hleran",
      "Amring",
      "An-Zaw",
      "Anarenen",
      "Anas Ulven",
      "Anasour Selitbael",
      "Anden Thilarvel",
      "Andil",
      "Andre Maul",
      "Andril Othran",
      "Anel Rethelas",
      "Anes Hlaren",
      "Anes Vendu",
      "Angaredhel",
      "Anglalos",
      "Angoril",
      "Anhaedra (Morrowind)",
      "Anit Eramarellaku",
      "Ano Andaram",
      "Ano Vando",
      "Anruin",
      "Arannir",
      "Aras Girendas",
      "Arathor",
      "Areas",
      "Arelvam Sadrano",
      "Aren Maren",
      "Arethan Mandas",
      "Ariulcabor Leontiulonus",
      "Arius Rulician",
      "Arkming the Flayer",
      "Arlowe",
      "Arnand Liric",
      "Arns Uvalas",
      "Arnskar",
      "Aroa Nethalen",
      "Aron Andaren",
      "Aronil (Morrowind)",
      "Arrille",
      "Arrinis Cerunia",
      "Arsyn Salas",
      "Arven Nalyn",
      "Arver Rethul",
      "Arvs Raram",
      "Arvyn Llerayn",
      "Aryon (Morrowind)",
      "Asha-Ammu Kutebani",
      "Ashibaal",
      "Ashu-Ahhe",
      "Ashuma-Nud Matluberib",
      "Ashur-Dan",
      "Assaba-Bentus",
      "Assallit Assunbahanammu",
      "Assamanut Sonnerralit",
      "Assamma-Idan",
      "Assantus Hansar",
      "Assatlit Assudnilamat",
      "Assemmus",
      "Assurdan Serdimapal",
      "Astien Masoriane",
      "Astius Hanotepelus",
      "Asum",
      "Athal Nerano",
      "Athanden Girith",
      "Athyn Sarethi",
      "Attelivupis Catius",
      "Atulg gro-Largum",
      "Audenian Valius",
      "Augurius Sialius",
      "Aunius Autrus",
      "Avon Ravel",
      "Avron Gols",
      "Avus Belvilo",
      "Azuk gro-Rugob",
      "Baadargo",
      "Bacola Closcius",
      "Bagamul gro-Dumul",
      "Baladas Demnevanni (Character)",
      "Balen Andrano",
      "Balen Sedrethi",
      "Balis Favani",
      "Balis Sari",
      "Balur Salvu",
      "Balver Sarethan",
      "Balyn Omavel",
      "Banden Indarys",
      "Banor Seran",
      "Baradras",
      "Baren Alen",
      "Barirrid",
      "Barnand Erelie",
      "Baronk gro-Uzuk",
      "Barusi Venim",
      "Bashag gro-Snagdu",
      "Bato Veranius",
      "Bazgulub gro-Ulfish",
      "Beden Giladren",
      "Bedraflod",
      "Bedrir",
      "Belas Othren",
      "Beldrose Dralor",
      "Belos Falos",
      "Belvis Sedri",
      "Benar Neleth",
      "Benunius Agrudilius",
      "Beraren Sadri",
      "Berel Sala",
      "Berela Andrano",
      "Berengeval",
      "Bertis Uvani",
      "Bervaso Thenim",
      "Bervyn Lleryn",
      "Bethes Sarothril",
      "Bevadar Bels",
      "Big Head (Morrowind)",
      "Bildren Areleth",
      "Bilen Velothril",
      "Bilos Andrethi",
      "Birard Adrognese",
      "Birer Indaram",
      "Bjadmund",
      "Bodean",
      "Bogakh gro-Mar",
      "Bolayn Rethan",
      "Boler Bandas",
      "Bolnor Andrani",
      "Bolrin",
      "Bolvus Ieneth",
      "Bolvyn Venim (Morrowind)",
      "Bolyn Elval",
      "Bormir",
      "Borug gro-Lazgarn",
      "Boryn Varen",
      "Boss Crito",
      "Both gro-Durug",
      "Botrir",
      "Bradil E
```

### 角色列表（共365个）

- "PC" :4639,
- "CHOICE" :2865,
- "Eno Hlaalu" :179,
- "Aryon (Morrowind)" :136,
- "Crassius Curio" :125,
- "Eydis Fire-Eye" :119,
- "Nibani Maesa" :116,
- "Caius Cosades (Morrowind)" :107,
- "Edwinna Elbert" :93,
- "Darius (Morrowind)" :89,
- "Gentleman Jim Stacey (Morrowind)" :85,
- "Athyn Sarethi" :85,
- "Nileno Dorvayn" :82,
- "Baladas Demnevanni (Character)" :80,
- "Lalatia Varian" :69,
- "Sul-Matuul" :66,
- "Neminda" :64,
- "Ajira" :64,
- "Savile Imayn" :63,
- "Duke Vedam Dren (Morrowind)" :62,
- "Vivec (Morrowind)" :59,
- "Divayth Fyr (Morrowind)" :59,
- "Edryno Arethi" :57,
- "Dagoth Ur (Character)" :57,
- "Sugar-Lips Habasi" :56,
- "Sinnammu Mirpal" :55,
- "Skink-in-Tree's-Shade" :52,
- "Kaye" :50,
- "Garothmuk gro-Muzgub" :50,
- "Aengoth the Jeweler" :50,
- "Ranis Athrys" :48,
- "Odral Helvi" :48,
- "Iulus Truptor" :47,
- "Faral Retheran" :46,
- "Tholer Saryoni" :45,
- "Han-Ammu" :45,
- "Theldyn Virith" :44,
- "Llunela Hleran" :44,
- "Lloros Sarano" :44,
- "Dondos Driler" :43,
- "Synnolian Tunifus" :42,
- "Big Helende" :42,
- "Tuls Valen" :41,
- "Manirai" :41,
- "Uvoo Llaren" :38,
- "Therana (Morrowind)" :38,
- "Radd Hard-Heart" :38,
- "Galsa Gindu" :38,
- "Mistress Dratha (Morrowind)" :37,
- "Kaushad" :35,
- ... 共365个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/ElderScrolls/Morrowind/,False,The Elder Scrolls III: Morrowind,The Elder Scrolls,TOTAL,9006,173666,26847,215812,1.5964787315016142,95.13815272706299,7.332633587742903,364
../data/ElderScrolls/Morrowind/,False,The Elder Scrolls III: Morrowind,The Elder Scrolls,playerChoice,3055,8773,4019,11840,1.1865488349013127,90.44360891005387,10.256593550800686,1
../data/ElderScrolls/Morrowind/,False,The Elder Scrolls III: Morrowind,The Elder Scrolls,male,3851,110139,14993,136970,1.9495530708405973,94.16934608145857,7.244910245449699,237
../data/ElderScrolls/Morrowind/,False,The Elder Scrolls III: Morrowind,The Elder Scrolls,female,2097,54693,7822,66933,1.5777352773978297,96.20488933053264,7.120642102192109,125
../data/ElderScrolls/Morrowind/,False,The Elder Scrolls III: Morrowind,The Elder Scrolls,neutral,3,61,10,69,0.1365409836065563,104.94841803278692,6.527584590163934,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
from bs4 import BeautifulSoup
import re,time
from os import path

baseURL = "https://elderscrolls.fandom.com"
indexPages = ["https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Assumanu+Mantiti",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Carecalmo",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Dralas+Gilu",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Eydis+Fire-Eye",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Ghost+of+Galos+Heleran",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Iingail",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Llether+Vari",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Minglos",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Oleen-Gei",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Salen+Ravel",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Talamu+Sethendas",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Ultis+Salam",
"https://elderscrolls.fandom.com/wiki/Category:Morrowind:_Characters?from=Zelay+Sobbinisun"
]


def openPage(url):
	req = Request(
		url, 
		data=None, 
		headers={
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
		}
	)
	html = urlopen(req).read().decode('utf-8')
	return(html)


for indexPage in indexPages:
	index = openPage(indexPage)
	time.sleep(2)
	pageLinks = re.findall('<a href="(.+?)" class="category-page__member-link"',index)

	for page in pageLinks:
		#print(page)
		fileName = "raw/"+page[page.rindex("/")+1:].replace(" ","").replace("(","_").replace(")","_") + ".html"
		foundDialogue = False
		if not 
```


## 策划参考价值
开放世界RPG类型的对话叙事参考。Bethesda开放世界RPG，海量NPC对话
