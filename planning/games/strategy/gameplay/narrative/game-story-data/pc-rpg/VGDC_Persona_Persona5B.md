# 女神异闻录 · Persona5B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：女神异闻录, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
女神异闻录系列《Persona5B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：女神异闻录（Persona）
- **游戏**：Persona5B
- **品类**：JRPG
- **说明**：Atlus的社交模拟+JRPG，Confidant系统

### 元数据 (meta.json)

```json
{
  "game": "Persona 5",
  "series": "Persona",
  "year": 2016,
  "status": "ready",
  "source": "https://lparchive.org/Persona-5/",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "partial"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "The source only provides a sample, first because some of the dialogue is in untranscribed images, but also because it only shows one path through each dialogue tree.",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "parserParameters": {
    "parser": "Persona5BParser",
    "fileType": ".html"
  },
  "mainPlayerCharacters": [
    "Joker",
    "Morgana",
    "Ryuji Sakamoto",
    "Ann Takamaki",
    "Yusuke Kitagawa",
    "Makoto Niijima",
    "Futaba Sakura",
    "Haru Okumura"
  ],
  "characterGroups": {
    "male": [
      "Joker",
      "Ryuji Sakamoto",
      "Yusuke Kitagawa",
      "Goro Akechi",
      "Igor",
      "Morgana",
      "Sojiro Sakura",
      "Munehisa Iwai",
      "Shinya Oda",
      "Yuuki Mishima",
      "Shadow Yuuki Mishima",
      "Toranosuke Yoshida",
      "Hiruta",
      "Inui",
      "Ushimaru",
      "Suguru Kamoshida",
      "Shadow Suguru Kamoshida",
      "Ichiryusai Madarame",
      "Shadow Ichiryusai Madarame",
      "Junya Kaneshiro",
      "Kunikazu Okumura",
      "Shadow Kunikazu Okumura",
      "Masayoshi Shido",
      "Shadow Masayoshi Shido",
      "Yaldabaoth",
      "SIU Director",
      "Natsuhiko Nakanohara",
      "Shadow Natsuhiko Nakanohara",
      "Sugimura",
      "President Tanaka",
      "Arsene",
      "Armored Soldier",
      "Busy Young Man",
      "Drunk Man",
      "Flashy Man",
      "Homeless Man",
      "Transient Man",
      "Man 2",
      "Plump Man",
      "Man 5",
      "Young Male Customer",
      "Man 7",
      "Man 8",
      "Man 9",
      "Over-Friendly Guy",
      "Menacing Man",
      "Miwa-Chan's Physician",
      "Neighborhood Man",
      "Elderly Male Customer",
      "Dazed Old Man",
      "Talkative Old Man",
      "Sad Old Man",
      "Old Shadow Prisoner",
      "Old Man 3",
      "Old Man 4",
      "Old Man talking to Rocker",
      "Pierced Man",
      "Pretentious Man",
      "Rural Young Man",
      "Wealthy Looking Man",
      "Wealthy Man",
      "Young Man",
      "Boy 1",
      "Boy 10",
      "Boy 11",
      "Boy 12",
      "Boy 13",
      "Stylish Male Student",
      "Boy 2",
      "Boy 3",
      "Boy 4",
      "Quiet Student",
      "Scary-looking Student",
      "Cowardly Student",
      "Boy 5",
      "Boy 6",
      "Boy 7",
      "Boy 9",
      "Defiant Boy",
      "Quiet Boy",
      "Reserved Boy",
      "ATM",
      "Accomplice",
      "Accomplice 2",
      "Agent",
      "Agent 2",
      "Agent 3",
      "Akiyama",
      "Anchor 1",
      "Anchor 2",
      "Slouching Office Worker",
      "Exhausted Office Worker",
      "Anime Cop",
      "Anime Cop 2",
      "Archangel",
      "Art Patron",
      "Asakura",
      "Asmodeus",
      "Protesting Man",
      "Clear-Eyed Man",
      "Shadow Junya Kaneshiro",
      "Shadow Yuichi Fukurai",
      "Bar Promoter",
      "Beefy Trendsetter",
      "Scruffy Romantic",
      "Benzo",
      "Taxi Driver",
      "Bodyguard",
      "Convenience Store Manager",
      "Bossy AD",
      "Broadcaster",
      "Brother",
      "Cameraman",
      "Cameraman 2",
      "Cameraman 3",
      "Casino Shadow",
      "Casino Shadow 2",
      "Chairman Fukurai",
      "Cheerful Host",
      "Chief",
      "Chief Detective",
      "Cleaner",
      "ClerkBot",
      "ChiefBot",
      "Partying College Student",
      "College Student 2",
      "Timid Cop",
      "Patrolling Officer",
      "Patrolling Officer 2",
      "Counselor",
      "Crying Grade Schooler",
      "Curious Child",
      "Customs",
      "Daisoujou",
      "Shadow Takanashi",
      "Deliveryman",
      "Detective",
      "Older Detective",
      "Hard-Boiled Detective",
      "Detective 5",
      "Dionysus",
      "Doctor",
      "Drunk Regular",
      "Shogi Magazine Editor",
      "Calm Employee",
      "Exhibit Staff",
      "FianceBot",
      "Fishy Hawker",
      "Foreign Barker",
      "Former noble",
      "Friendly Promoter",
      "Futsunushi",
      "Fuu ki",
      "Upset Gamer",
      "Nishiyama",
      "Girimehkala",
      "Goemon",
      "Rebellious Grade Schooler",
      "Innocent Grade Schooler",
      "Interrogation Room Guard",
      "Guide",
      "Haughty Regular",
      "Hecatoncheires",
      "Hell Biker",
      "Shadow Honyo",
      "Iida",
      "Ikeda",
      "Ikesugi",
      "Incubus",
      "Injured Student",
      "Tired Investigator",
      "Investigator 2",
      "Ippon Datara",
      "Irritated Promoter",
      "Jack Frost",
      "Jikokuten",
      "Shadow Jochi",
      "Junior Detective",
     
```

### 角色列表（共714个）

- "ACTION" :34380,
- "Morgana" :2816,
- "Ryuji Sakamoto" :2812,
- "Ann Takamaki" :2214,
- "Makoto Niijima" :1813,
- "Yusuke Kitagawa" :1513,
- "Futaba Sakura" :1115,
- "Joker" :852,
- "Haru Okumura" :753,
- "Anon" :710,
- "Sojiro Sakura" :620,
- "Goro Akechi" :533,
- "Yuuki Mishima" :379,
- "Sae Niijima" :373,
- "Sadayo Kawakami" :347,
- "Chihaya Mifune" :279,
- "Tae Takemi" :252,
- "Ichiko Ohya" :248,
- "Hifumi Togo" :201,
- "Justine" :199,
- "Chatter" :197,
- "Munehisa Iwai" :197,
- "Caroline" :197,
- "Newscaster" :171,
- "Shinya Oda" :168,
- "Toranosuke Yoshida" :155,
- "Masayoshi Shido" :138,
- "Whisper" :128,
- "Murmur" :121,
- "Igor" :111,
- "Lala Escargot" :71,
- "SIU Director" :70,
- "Post-Festival MC" :69,
- "Inui" :59,
- "Shadow Suguru Kamoshida" :54,
- "Newspaper Club Member" :53,
- "Shadow Junya Kaneshiro" :48,
- "Shadow Ichiryusai Madarame" :47,
- "Suguru Kamoshida" :47,
- "Shadow Sae Niijima" :46,
- "Souse" :45,
- "Chouno" :44,
- "COMMENT" :43,
- "Matsushita" :43,
- "Art Patron" :42,
- "Haughty Regular" :42,
- "Principal" :42,
- "Lavenza" :40,
- "Ushimaru" :39,
- "Shadow Futaba Sakura" :36,
- ... 共714个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/Persona/Persona5B/,False,Persona 5,Persona,TOTAL,24295,385817,102404,476492,0.4526076463654576,98.52813378069403,7.002187843726429,711
../data/Persona/Persona5B/,False,Persona 5,Persona,male,13706,225840,57441,278630,0.5016024812300586,98.46912573768576,7.059428401958106,436
../data/Persona/Persona5B/,False,Persona 5,Persona,female,9193,148100,41703,182990,0.37490023767471925,98.70001530363028,6.842917295484711,197
../data/Persona/Persona5B/,False,Persona 5,Persona,neutral,1396,11877,3259,14872,0.6068871407016534,97.20254749026556,7.914657373133945,78

```


### 数据来源脚本 (scraper.py)

```python
import re, time
from bs4 import BeautifulSoup
from urllib.request import urlopen


avoidPages = ["https://lparchive.org/Persona-5/Update%20113/", "https://lparchive.org/Persona-5/Update%20114/",
"https://lparchive.org/Persona-5/Update%20115/"]

indexPage = "https://lparchive.org/Persona-5/"

html = urlopen(indexPage).read().decode('utf-8')
time.sleep(3)
pageLinks = re.findall('href="(Update.+?)"',html)

pageLinksUnique = []
for p in pageLinks:
	if not p in pageLinksUnique:
		pageLinksUnique.append(p)

pageNum = 1
for pageLink in pageLinksUnique:
	filename = "raw/page" + str(pageNum).zfill(3)+".html"
	url = "https://lparchive.org/Persona-5/"+pageLink
	if not url in avoidPages:
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
