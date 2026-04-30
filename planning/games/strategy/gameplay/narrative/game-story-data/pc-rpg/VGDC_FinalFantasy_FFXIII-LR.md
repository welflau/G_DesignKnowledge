# 最终幻想 · FFXIII-LR（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：最终幻想, JRPG, 对话语料, PC RPG, 角色对话
> 游戏类型：JRPG

## 概述
最终幻想系列《FFXIII-LR》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：最终幻想（FinalFantasy）
- **游戏**：FFXIII-LR
- **品类**：JRPG
- **说明**：Square Enix经典JRPG，线性叙事+过场

### 元数据 (meta.json)

```json
{
  "game": "Lightning Returns: Final Fantasy XIII",
  "series": "Final Fantasy",
  "year": 2014,
  "status": "ready",
  "source": "https://www.youtube.com/watch?v=Kl_EgMs2V4A",
  "sourceFeatures": {
    "type": "fan transcript",
    "completeness": "sample",
    "dialogueOrder": true,
    "choices": "NA"
  },
  "error checks": {
    "truePositive_numTestsDone": "10",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "1",
    "truePositive_notes": "Some sidequest dialogue missing (source is just a sample)",
    "falsePositive_numTestsDone": "5",
    "falsePositive_numErrors": "0",
    "falsePositive_notes": "N/A"
  },
  "notes": "Transcription of https://www.youtube.com/watch?v=Kl_EgMs2V4A and https://www.youtube.com/watch?v=BDXGUhO18O8",
  "characterInfoSource": "https://finalfantasy.fandom.com/wiki/",
  "parserParameters": {
    "parser": "FFXIIILRParser",
    "fileType": ".txt"
  },
  "mainPlayerCharacters": [
    "Lightning"
  ],
  "characterGroups": {
    "male": [
      "Dajh",
      "Hope",
      "Noel",
      "Raines",
      "Sazh",
      "Snow",
      "Adonis",
      "Bhakti",
      "Bhunivelze",
      "Caius",
      "Director Sarzhak",
      "Dr. Gysahl",
      "Drunk Pyrotechnician",
      "Elmer",
      "Funicula",
      "Holmes",
      "Thorton",
      "Inquisitor",
      "Man Awaiting The End",
      "Mog",
      "Witness",
      "Man at North Platform",
      "Strange Man",
      "Cultist on Phone",
      "Man in Jagd Village",
      "Man in Jagd Woods",
      "Mogbo",
      "Moguire",
      "Tour Guide",
      "Adventuring Essentials",
      "Adventuring Essentials (Wildlands)",
      "Angel of Valhalla",
      "Audience member",
      "Banquet Maitre D'",
      "Black Market Dealer",
      "Chocobo",
      "Fireworks Boss",
      "Tormented Tourist",
      "Male Bandit",
      "Male Bandit 2",
      "Bandits",
      "God",
      "Goddess's Disciple on Phone",
      "Goddess's Disciple",
      "Goddess's Disciple 1",
      "Man on Street",
      "Hunter",
      "Hunter Chief",
      "Hunter Hopeful",
      "Luxerion Innkeeper",
      "Man near Sarala",
      "Kaj",
      "Knowledgeable Tourist",
      "Lazy Station Worker",
      "Man",
      "Proud Pyrotechnician",
      "Man 1",
      "Officer",
      "Outfitters",
      "Passenger 1",
      "Passenger 2",
      "Rusted Gate Man",
      "Pilgrims Causeway Man",
      "Idol Ave Man",
      "Relieved Man",
      "Man in Fountain Square",
      "Man in Pleasure Alley",
      "Little Boy",
      "Man on Sacred Path",
      "Resident Moogle",
      "Man by Victim",
      "Man at Machine",
      "Man at Station",
      "Cultist",
      "Sentry by Twin Gates",
      "Cathedral Plaza Sentry",
      "Priest",
      "Man on Steps",
      "Other Man in Jagd Village",
      "Man in Restaurant District",
      "Beseeching Man",
      "Boy in Jagd Village",
      "2nd Ave Sentry",
      "Ruins Gatekeeper",
      "Secutor",
      "Seller",
      "Sentry that confronts Lightning",
      "Snow's Sentry",
      "Sentry",
      "Cactuar Plaza Sentry",
      "Fountain Square Sentry",
      "Sentry 1",
      "Sentry 2",
      "Seven",
      "Soldier",
      "Soldier 2",
      "Station Attendant",
      "Supplier",
      "Surveying Man",
      "Suspicious Gatekeeper",
      "Warehouse Employee",
      "Idol Ave Sentry"
    ],
    "female": [
      "Chocolina",
      "Lightning",
      "Serah",
      "Vanille",
      "Fang",
      "Aremiah",
      "Cardesia",
      "High Priestess",
      "Lumina",
      "Lyla",
      "Nadia",
      "Sarala",
      "Pious Cleric",
      "Resident in tan blazer",
      "Woman 3",
      "Paddra Nsu-Yeul",
      "Yeul who gave Caius the heart of chaos",
      "Yeul who wishes to save Caius",
      "Yeul who loves Noel",
      "Another Yeul",
      "Yeul",
      "Girl in the Grasslands",
      "Woman by road in Grasslands",
      "Mogwin",
      "Train Announcement",
      "Announcer",
      "Assistant",
      "Child",
      "Cleric",
      "Flighty Tourist",
      "Tourist 1",
      "Tourist 2",
      "Female Bandit",
      "Young Female Bandit",
      "Goddess's Disciple 2",
      "Goddess's Disciple 3",
      "Guide",
      "Woman in Jagd Village",
      "Woman 1",
      "Woman 2",
      "Mounted Woman",
      "Jagd Village Innkeeper",
      "Woman by machine",
      "Woman in Luxerion",
      "Central Ave Woman",
      "Woman in Jagd Woods",
      "Woman by Victim",
      "Pilgrims Passage Woman",
      "Sentry 3",
      "Woman in Cathedral",
      "Woman by Tour Guide",
      "Woman on Steps",
      "Young Woman in Yusnaan",
      "Woman Announcement",
      "Young Woman in Cactuar Plaza",
      "Shop Owner",
      "Central Ave Female Seller",
      "Woman in Pink",
      "Slaughterhouse Zoe",
      "Excited Woman",
      "Woman",
      "Woman Seller",
      "Worker",
      "Woman in Green",
      "Yeuls"
    ],
    "neutral": [
      "Bystander",
      "Goddess's Disciples",
      "Moogle",
      "W
```

### 角色列表（共174个）

- "ACTION" :1253,
- "Lightning" :833,
- "Hope" :374,
- "LOCATION" :207,
- "Lumina" :105,
- "Fang" :92,
- "Noel" :34,
- "Dr. Gysahl" :33,
- "Snow" :32,
- "Mog" :31,
- "Vanille" :29,
- "Announcer" :29,
- "Serah" :25,
- "Sazh" :21,
- "Slaughterhouse Zoe" :21,
- "Director Sarzhak" :21,
- "Chocolina" :20,
- "Aremiah" :20,
- "Caius" :19,
- "Adonis" :17,
- "Bhakti" :16,
- "Nadia" :16,
- "Yeul" :14,
- "Elmer" :13,
- "Raines" :12,
- "Cardesia" :12,
- "Angel of Valhalla" :11,
- "Funicula" :11,
- "Drunk Pyrotechnician" :11,
- "Paddra Nsu-Yeul" :10,
- "Bhunivelze" :9,
- "Hunter Hopeful" :9,
- "Tour Guide" :9,
- "Goddess's Disciple 1" :9,
- "High Priestess" :8,
- "Lyla" :8,
- "Warehouse Employee" :7,
- "Passenger 1" :6,
- "Goddess's Disciples" :6,
- "Holmes" :6,
- "Sentry" :6,
- "Lazy Station Worker" :5,
- "Chocobo" :5,
- "Fireworks Boss" :5,
- "Suspicious Gatekeeper" :5,
- "Thorton" :5,
- "Train Announcement" :5,
- "Dajh" :4,
- "Moguire" :4,
- "Yeul who gave Caius the heart of chaos" :4,
- ... 共174个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/FinalFantasy/FFXIII-LR/,False,Lightning Returns: Final Fantasy XIII,Final Fantasy,TOTAL,2182,47916,8949,56301,0.36311921491171617,101.99587329074625,6.083267621701482,172
../data/FinalFantasy/FFXIII-LR/,False,Lightning Returns: Final Fantasy XIII,Final Fantasy,male,855,21702,3740,25739,0.6680754966273845,100.60801764173638,6.249666965542494,102
../data/FinalFantasy/FFXIII-LR/,False,Lightning Returns: Final Fantasy XIII,Final Fantasy,female,1317,26151,5192,30486,0.13040993808389878,103.09868468576538,5.94709747270784,65
../data/FinalFantasy/FFXIII-LR/,False,Lightning Returns: Final Fantasy XIII,Final Fantasy,neutral,10,63,17,76,0.09021475256769484,101.01638655462187,6.326660971055088,5

```


### 数据来源脚本 (scraper.py)

```python
import time
print("The source is a custom transcription of two youtube files (see readme).")
print("  (sleeping for 30 seconds)")
time.sleep(30)
```


## 策划参考价值
JRPG类型的对话叙事参考。Square Enix经典JRPG，线性叙事+过场
