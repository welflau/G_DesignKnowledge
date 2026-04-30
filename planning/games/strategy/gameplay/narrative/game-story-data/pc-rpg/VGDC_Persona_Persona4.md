# 女神异闻录 · Persona4（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：女神异闻录, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
女神异闻录系列《Persona4》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：女神异闻录（Persona）
- **游戏**：Persona4
- **品类**：JRPG
- **说明**：Atlus的社交模拟+JRPG，Confidant系统

### 元数据 (meta.json)

```json
{
  "game": "Persona 4",
  "series": "Persona",
  "year": 2008,
  "status": "ready",
  "source": "https://lparchive.org/Persona-4/",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "not included"
  },
  "error checks": {
    "truePositive_numTestsDone": "6",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "Due to the nature of the source, we miss some lines of dialogue (as they are shown in screenshots rather than transcribed). This was the case in one instance of the six instances checked.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "Persona4Parser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Souji",
    "Yosuke Hanamura",
    "Chie Satonaka",
    "Yukiko Amagi",
    "Kanji Tatsumi",
    "Rise Kujikawa",
    "Teddie",
    "Naoto Shirogane"
  ],
  "characterGroups": {
    "male": [
      "Daidara",
      "Daisuke Nagase",
      "Edogawa",
      "Mr. Hosoi",
      "Igor",
      "Kanji Tatsumi",
      "Shadow Kanji Tatsumi",
      "Kinshiro Morooka",
      "Mr. Kondo",
      "Kou Ichijo",
      "Mitsuo Kubo",
      "Shadow Mitsuo Kubo",
      "Naoki",
      "Ryotaro Dojima",
      "Shu Nakajima",
      "Taro Namatame",
      "Teddie",
      "Shadow Teddie",
      "Tohru Adachi",
      "Mr. Yamada",
      "Yosuke Hanamura",
      "Shadow Yosuke",
      "Yuuta",
      "Souji",
      "Kunino Sagiri",
      "Tanaka",
      "Ameno Sagiri",
      "Agency Spokesman",
      "Magazine Reporter",
      "Commercial Voice",
      "Ailurophobe",
      "Aiya Owner",
      "Announcer",
      "Moel Gas Station Attendant",
      "Awestruck Student",
      "Bespectacled Student",
      "Guy With A Backpack",
      "Bored Teenager",
      "Idle Teenager",
      "Lazy Student",
      "Brown-Haired Student",
      "Businessman",
      "Chie Fan",
      "Commentator",
      "Conceited Student",
      "Smirking Student",
      "Other Student",
      "Crying Kid",
      "Out-of-towner",
      "Deputy Mayor",
      "Eager Student",
      "Doctor",
      "Doubtful Student",
      "Dumbfounded Student",
      "Drama Club President",
      "Duty Officer",
      "Elderly Person",
      "Slacker Student",
      "Follower Student",
      "Enthusiastic Student",
      "Excited Student",
      "Rumor-Loving Student",
      "Knowledgeable Student",
      "Gekkoukan Principal",
      "Glasses-Wearing Student",
      "White-Collar Man",
      "Inoue",
      "Shady Reporter",
      "P.E. Teacher",
      "Yasogami Student",
      "Candy Apple Man",
      "Lottery Worker",
      "MC",
      "Saki's Dad",
      "Narrator",
      "Onlooking Student",
      "Spectacled Student",
      "Optimistic Student",
      "Partner",
      "Patrolman",
      "Photographer",
      "Police Officer",
      "Policeman",
      "Postcard",
      "Principal",
      "Punk",
      "Punk Leader",
      "Reporter",
      "Rise Fan",
      "Risette Fan",
      "Sitting Student",
      "Smirking Senior",
      "Soccer Player",
      "Sporty Student",
      "Student",
      "Student's Friend",
      "Suspicious Guy",
      "TV-Loving Student",
      "Takeshi",
      "Uniformed Officer",
      "Varsity Player",
      "Worried Student",
      "Yakushiji",
      "Yukiko Fan",
      "Despondent Man",
      "Gas-Masked Man",
      "Kind Man",
      "Loud Old Man",
      "Akio's Dad",
      "Man",
      "Construction Crew",
      "Male Patient",
      "Old Man (Fisherman)",
      "Keita's Grandpa",
      "Older Man's Voice",
      "Suspicious Man",
      "Young Man",
      "Young Man with Shady Reporter",
      "Young Man's Voice",
      "Akio",
      "Yuuta",
      "Lonely Boy",
      "Doll Boy",
      "Boy's Voice",
      "Easygoing Boy",
      "Visiting Boy",
      "Yumi's Father",
      "Male Class Rep",
      "Male Employee",
      "Male Student (Infirmary)",
      "Male Student"
    ],
    "female": [
      "Ai Ebihara",
      "Chie Satonaka",
      "Shadow Chie Satonaka",
      "Chihiro Fushimi",
      "Eri",
      "Hanako Ohtani",
      "Hisano Kuroda",
      "Kimiko Sofue",
      "Margaret",
      "Mayumi Yamano",
      "Mrs. Nakayama",
      "Nanako",
      "Noriko Kashiwagi",
      "Rise Kujikawa",
      "Shadow Rise Kujikawa",
      "Saki",
      "Sayoko Uehara",
      "Yukiko Amagi",
      "Shadow Yukiko Amagi",
      "Yumi Ozawa",
      "Izanami",
      "Appalled Student",
      "Brisk Student",
      "Cold Student",
      "Commercial",
      "Textile Shop Owner",
      "Customer",
      "Daisuke's Ex",
      "Day Care Supervisor",
      "Disinterested Student",
      "Impressed Student",
      "Drama Club Vice President",
      "Jealous Student",
      "Non-Drama Club Member",
      "Recorded Message",
      "Whiny Student",
      "Gaudy Student",
      "Snooty Student",
      "Singers",
      "Kasai",
   
```

### 角色列表（共261个）

- "ACTION" :8381,
- "Yosuke Hanamura" :2357,
- "Chie Satonaka" :1561,
- "Naoto Shirogane" :1123,
- "Yukiko Amagi" :1017,
- "Rise Kujikawa" :992,
- "Teddie" :920,
- "Kanji Tatsumi" :908,
- "Ryotaro Dojima" :797,
- "Nanako" :637,
- "Tohru Adachi" :493,
- "Ai Ebihara" :309,
- "Yumi Ozawa" :284,
- "Hisano Kuroda" :266,
- "Margaret" :259,
- "Souji" :249,
- "Kou Ichijo" :205,
- "Daisuke Nagase" :182,
- "Sayoko Uehara" :181,
- "Taro Namatame" :177,
- "Igor" :144,
- "Shu Nakajima" :115,
- "Mr. Kondo" :112,
- "Kinshiro Morooka" :99,
- "Eri" :96,
- "Moel Gas Station Attendant" :94,
- "Noriko Kashiwagi" :91,
- "Kimiko Sofue" :83,
- "Shadow Rise Kujikawa" :77,
- "Announcer" :77,
- "Mr. Hosoi" :74,
- "Mr. Yamada" :63,
- "Mrs. Nakayama" :63,
- "Shadow Yukiko Amagi" :63,
- "Izanami" :62,
- "Ameno Sagiri" :59,
- "Mitsuo Kubo" :59,
- "Shadow Kanji Tatsumi" :58,
- "Old Man (Fisherman)" :52,
- "MC" :50,
- "Doll Boy" :50,
- "Shadow Naoto Shirogane" :44,
- "Inoue" :41,
- "Wallet Misplacer" :40,
- "Doctor" :40,
- "Kanji's Mother" :38,
- "Police Officer" :38,
- "Edogawa" :37,
- "Awkward Girl" :37,
- "Shady Reporter" :37,
- ... 共261个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Persona/Persona4/,False,Persona 4,Persona,TOTAL,16477,156753,58123,186273,-0.5160050402068634,103.56560717749417,6.365116384127596,259
../data/Persona/Persona4/,False,Persona 4,Persona,male,8421,81960,29100,96995,-0.5269379229495907,103.8569678344478,6.415571009141999,130
../data/Persona/Persona4/,False,Persona 4,Persona,female,7993,74354,28874,88652,-0.5166069165980751,103.35298570790201,6.301532863523767,115
../data/Persona/Persona4/,False,Persona 4,Persona,neutral,63,439,148,626,2.3932480145293358,83.18738849042667,7.812052570337992,14

```


### 数据来源脚本 (scraper.py)

```python
import re, time, os
from bs4 import BeautifulSoup
from urllib.request import urlopen

indexPage = "https://lparchive.org/Persona-4/"

html = urlopen(indexPage).read().decode('utf-8')
time.sleep(3)
pageLinks = re.findall('href="(Update.+?)"',html)

pageLinksUnique = []
for p in pageLinks:
	if not p in pageLinksUnique:
		pageLinksUnique.append(p)
	# Don't capture info entries
	if p == "Update%20106/":
		break

pageLinksUnique += ["Update%20108/","Update%20109/"]

pageNum = 1
for pageLink in pageLinksUnique:
	filename = "raw/page" + str(pageNum).zfill(3)+".html"
	if not os.path.isfile(filename):
		url = indexPage+pageLink
		html = urlopen(url).read().decode('utf-8')
		time.sleep(2)
	
		soup = BeautifulSoup( html, "html5lib")
		cont = soup.find("div",{"id":"content"})
		towrite = pageLink + "\n" + str(cont)
	
		o = open(filename,'w')
		o.write(towrite)
		o.close()
	pageNum += 1

```


## 策划参考价值
JRPG类型的对话叙事参考。Atlus的社交模拟+JRPG，Confidant系统
