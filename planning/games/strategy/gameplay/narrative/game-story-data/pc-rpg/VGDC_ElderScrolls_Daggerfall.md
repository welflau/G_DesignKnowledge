# 上古卷轴 · Daggerfall（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：上古卷轴, 开放世界RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：开放世界RPG

## 概述
上古卷轴系列《Daggerfall》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：上古卷轴（ElderScrolls）
- **游戏**：Daggerfall
- **品类**：开放世界RPG
- **说明**：Bethesda开放世界RPG，海量NPC对话

### 元数据 (meta.json)

```json
{
  "game": "The Elder Scrolls II: Daggerfall",
  "series": "The Elder Scrolls",
  "year": 1996,
  "status": "ready",
  "source": "https://github.com/Interkarma/daggerfall-unity",
  "sourceFeatures": {
    "type": "game data",
    "completeness": "high",
    "dialogueOrder": false,
    "choices": "complete"
  },
  "error checks": {
    "truePositive_numTestsDone": "5",
    "truePositive_numParsingErrors": "0",
    "truePositive_numSourceErrors": "0",
    "truePositive_notes": "Quest dialogue present; other dialogue not included in source.",
    "falsePositive_numTestsDone": "N/A",
    "falsePositive_numErrors": "N/A",
    "falsePositive_notes": "N/A"
  },
  "note": "Source contains only quest dialogue.",
  "parserParameters": {
    "parser": "DaggerfallParser3",
    "fileType": ".txt"
  },
  "mainPlayerCharacters": [
    "PC"
  ],
  "characterGroups": {
    "playerChoice": [
      "PC"
    ],
    "random": [
      "60C00Y00#_qgfriend_",
      "A0C00Y16#_missingperson_",
      "R0C11Y28#_widow_",
      "M0B11Y18#_target_",
      "S0000012#_dispatcher_",
      "N0B00Y16#_merchant_",
      "B0B00Y00#_vamp_",
      "Q0C00Y07#_daedra_",
      "R0C10Y20#_questgiver_",
      "L0B60Y10#_questgiver_",
      "R0C20Y22#_orsinium_",
      "S0000106#_thievesguild_",
      "R0C10Y18#_questgiver_",
      "R0C11Y26#_hooker_",
      "N0B30Y15#_questgiver_",
      "R0C11Y27#_npc2_",
      "S0000001#_agentuk_",
      "S0000010#_agentuk_",
      "O0B00Y01#_questgiver_",
      "R0C10Y21#_dummyorc_",
      "V0C00Y00#_contact_",
      "L0B10Y03#_contact_",
      "B0C00Y06#_local_",
      "B0B71Y03#_witch_",
      "Q0C0XY02#_daedra_",
      "A0C10Y02#_qgiver_",
      "S0000500#_contact2_",
      "CUREWER#_child_",
      "C0B00Y01#_lover_",
      "M0B00Y16#_villager_",
      "S0000008#_Underking_",
      "C0C00Y10#_healer_",
      "K0C00Y04#_qgiver_",
      "A0C00Y12#_informant_",
      "A0C00Y06#_traitor_",
      "S0000106#_P.15_",
      "M0B00Y17#_love_",
      "N0B20Y05#_wizard_",
      "M0B00Y17#_victim_",
      "30C00Y00#_questgiver_",
      "R0C11Y03#_dummydaedra_",
      "10C00Y00#_qgfriend_",
      "B0B70Y16#_local_",
      "S0000106#_magesguild_",
      "C0C00Y12#_decoy_",
      "N0B20Y02#_sleepingmage_",
      "K0C01Y00#_victim_",
      "N0B21Y14#_love_",
      "K0C00Y04#_competitor_",
      "S0000010#shopkeeper1",
      "A0C00Y14#_questgiver_",
      "U0C00Y00#_questgiver_",
      "L0A01L00#_apothecary_",
      "K0C00Y03#_contact_",
      "T0C00Y00#_qgfriend_",
      "Q0C20Y02#_questgiver_",
      "A0C0XY04#_qgiver_",
      "Q0C00Y03#_child_",
      "S0000106#_P.13_",
      "S0000106#_P.04_",
      "90C00Y00#_qgfriend_",
      "F0B00Y00#_questgiver_",
      "N0B00Y08#_warrior_",
      "N0B00Y09#_db_",
      "P0B00L03#_vampname_",
      "K0C00Y06#_noble_",
      "C0B10Y05#_custodian_",
      "R0C10Y09#_questgiver_",
      "W0C00Y00#_enemy_",
      "N0B00Y16#_questgiver_",
      "80C0XY00#_murder_",
      "L0B20Y02#_damsel_",
      "S0000106#_P.12_",
      "L0B20Y02#_questgiver_",
      "R0C10Y08#_questgiver_",
      "C0B00Y02#_hooker_",
      "N0B00Y16#_mage_",
      "C0C00Y12#_thief_",
      "R0C11Y19#_questgiver_",
      "C0B00Y04#_qgiver_",
      "Q0C0XY02#_man_",
      "S0000988#_P.03_",
      "30C00Y00#_qgfriend_",
      "P0B00L06#_mage_",
      "Q0C00Y03#_daedra_",
      "R0C10Y02#_contact_",
      "A0C00Y08#_darkb_",
      "A0C01Y03#_teacher_",
      "N0B00Y17#_questgiver_",
      "R0C10Y14#_contact_",
      "A0C0XY04#_dummydarkb_",
      "M0B00Y16#_dummy_",
      "K0C00Y06#_thief_",
      "A0C00Y10#_giver_",
      "R0C10Y17#_questgiver_",
      "R0C11Y16#_npc2_",
      "C0B00Y02#_child_",
      "CUREVAM#_hunter_",
      "S0000106#_P.11_",
      "B0B71Y03#_child_",
      "K0C30Y03#_victin_",
      "L0B50Y11#_questgiver_",
      "S0000106#_queston2_",
      "L0B10Y01#_questgiver_",
      "B0C00Y10#_local_",
      "B0B60Y12#_local_",
      "S0000007#courtier",
      "A0C01Y09#_questg_",
      "C0B10Y07#_enemy_",
      "R0C10Y10#_questgiver_",
      "N0B21Y14#_noble_",
      "L0B00Y02#_qgiver_",
      "O0B00Y00#_questgiver_",
      "20C00Y00#_contact_",
      "A0C10Y05#_priest_",
      "U0C00Y00#_qgfriend_",
      "B0B81Y02#_wizard_",
      "A0C00Y11#_healer_",
      "C0C00Y13#_enemy_",
      "K0C00Y07#_kidnapper_",
      "S0000500#_contact1_",
      "K0C30Y03#_patsy_",
      "K0C00Y06#_merchant_",
      "K0C30Y03#_guard_",
      "C0B00Y00#_qgiver_",
      "A0C00Y15#_questgiver_",
      "Q0C00Y06#_witch_",
      "C0B10Y07#_priest_",
      "R0C10Y02#_questgiver_",
      "A0C01Y13#informant2",
      "P0B10L08#_daedra_",
      "O0B00Y01#_contact_",
      "L0B50Y11#_marknpc_",
      "K0C01Y00#_qgiver_",
      "N0B00Y17#_maker_",
      "R0C30Y25#_contact_",
      "C0B00Y01#_priest_",
      "I0B00Y00#_questgiver_",
      "A0C10Y02#_child_",
      "R0C11Y19#_contact_",
      "A0C0XY04#_dummymage_",
      "C0B00Y03#_cleric_",
      "A0C10Y02#_dummydarkb_",
      "B0B40Y09#_local_",
      "B0B71Y03#_local_",
      "C0B00Y02#_g
```

### 角色列表（共355个）

- "PC" :550,
- "CHOICE" :370,
- "ACTION" :243,
- "Unknown" :116,
- "Queen Akorithi" :15,
- "B0B81Y02#_wizard_" :12,
- "A0C00Y10#_giver_" :12,
- "A0C01Y09#_questg_" :11,
- "A0C00Y16#_questgiver_" :10,
- "Mynisera" :9,
- "K0C00Y09#_qgiver_" :9,
- "Queen Barenziah" :8,
- "Nulfaga" :8,
- "K0C00Y07#_qgiver_" :8,
- "K0C00Y02#_qgiver_" :8,
- "A0C00Y08#_questgiver_" :8,
- "A0C00Y00#_qgiver_" :8,
- "Queen Aubk-i" :7,
- "Prince Helseth" :7,
- "N0B00Y17#_scholar_" :7,
- "K0C00Y06#_qgiver_" :7,
- "K0C00Y05#_child_" :7,
- "A0C00Y15#_questgiver_" :7,
- "A0C00Y14#_questgiver_" :7,
- "Gortwog" :6,
- "S0000007#_barmaid_" :6,
- "Princess Elysana" :6,
- "Q0C10Y00#_qgiver_" :6,
- "O0B00Y11#_questgiver_" :6,
- "N0B40Y07#_qgiver_" :6,
- "Baltham Greyman" :6,
- "N0B11Y18#_questgiver_" :6,
- "N0B00Y17#_questgiver_" :6,
- "Whitka" :6,
- "E0B00Y00#_questgiver_" :6,
- "C0B00Y01#_prophet_" :6,
- "A0C01Y06#_qgiver_" :6,
- "A0C00Y17#_questgiver_" :6,
- "A0C00Y11#_giver_" :6,
- "X0C00Y00#_contact_" :5,
- "Lady Brisienna" :5,
- "King of Worms" :5,
- "P0B00L06#_mg_" :5,
- "N0C00Y11#_qgiver_" :5,
- "N0B30Y15#_questgiver_" :5,
- "N0B20Y05#_questgiver_" :5,
- "N0B10Y01#_questgiver_" :5,
- "Lord K'avar" :5,
- "L0B50Y11#_questgiver_" :5,
- "L0B00Y02#_qgiver_" :5,
- ... 共355个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/ElderScrolls/Daggerfall/,False,The Elder Scrolls II: Daggerfall,The Elder Scrolls,TOTAL,1757,43855,6342,52791,1.3112506106441995,97.97796485722192,6.224397328216128,353
../data/ElderScrolls/Daggerfall/,False,The Elder Scrolls II: Daggerfall,The Elder Scrolls,playerChoice,550,550,549,550,-3.399289617486337,121.21815118397086,0.0496903460837887,1
../data/ElderScrolls/Daggerfall/,False,The Elder Scrolls II: Daggerfall,The Elder Scrolls,random,453,17593,2389,21262,1.5429024372469016,97.11713525088474,6.2320901907216655,154
../data/ElderScrolls/Daggerfall/,False,The Elder Scrolls II: Daggerfall,The Elder Scrolls,female,117,5044,623,6199,2.069582397215898,94.64512189362821,6.570612571998835,45
../data/ElderScrolls/Daggerfall/,False,The Elder Scrolls II: Daggerfall,The Elder Scrolls,male,557,18756,2486,22580,1.5582143260951877,97.32881168709845,6.2887984551749545,152
../data/ElderScrolls/Daggerfall/,False,The Elder Scrolls II: Daggerfall,The Elder Scrolls,neutral,80,1912,293,2200,0.5323887928941708,102.86842253702146,5.900886151770031,1

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import time,os

base = "https://raw.githubusercontent.com/Interkarma/daggerfall-unity/57b758a1c3dce41f4379dd1934c2af43f12b5526/Assets/StreamingAssets/Quests/"

pages = ['$CUREVAM.txt', '$CUREWER.txt', '00B00Y00.txt', '10C00Y00.txt', '20C00Y00.txt', '30C00Y00.txt', '40C00Y00.txt', '50C00Y00.txt', '60C00Y00.txt', '70C00Y00.txt', '80C0XY00.txt', '90C00Y00.txt', 'A0C00Y00.txt', 'A0C00Y06.txt', 'A0C00Y07.txt', 'A0C00Y08.txt', 'A0C00Y10.txt', 'A0C00Y11.txt', 'A0C00Y12.txt', 'A0C00Y14.txt', 'A0C00Y15.txt', 'A0C00Y16.txt', 'A0C00Y17.txt', 'A0C01Y01.txt', 'A0C01Y03.txt', 'A0C01Y06.txt', 'A0C01Y09.txt', 'A0C01Y13.txt', 'A0C0XY04.txt', 'A0C10Y02.txt', 'A0C10Y05.txt', 'A0C41Y18.txt', 'B0B00Y00.txt', 'B0B00Y01.txt', 'B0B10Y04.txt', 'B0B20Y07.txt', 'B0B40Y08.txt', 'B0B40Y09.txt', 'B0B50Y11.txt', 'B0B60Y12.txt', 'B0B70Y14.txt', 'B0B70Y16.txt', 'B0B71Y03.txt', 'B0B80Y17.txt', 'B0B81Y02.txt', 'B0C00Y05.txt', 'B0C00Y06.txt', 'B0C00Y10.txt', 'B0C00Y13.txt', 'C0B00Y00.txt', 'C0B00Y01.txt', 'C0B00Y02.txt', 'C0B00Y03.txt', 'C0B00Y04.txt', 'C0B00Y14.txt', 'C0B10Y05.txt', 'C0B10Y06.txt', 'C0B10Y07.txt', 'C0B10Y15.txt', 'C0B20Y08.txt', 'C0B3XY09.txt', 'C0C00Y10.txt', 'C0C00Y11.txt', 'C0C00Y12.txt', 'C0C00Y13.txt', 'CUSTOM01.txt', 'D0B00Y00.txt', 'E0B00Y00.txt', 'F0B00Y00.txt', 'G0B00Y00.txt', 'H0B00Y00.txt', 'I0B00Y00.txt', 'J0B00Y00.txt', 'K0C00Y00.txt', 'K0C00Y02.txt', 'K0C00Y03.txt', 'K0C00Y04.txt', 'K0C00Y05.txt', 'K0C00Y06.txt', 'K0C00Y07.txt', 'K0C00Y08.txt', 'K0C00Y09.txt', 'K0C01Y00.txt', 'K0C01Y10.txt', 'K0C0XY01.txt', 'K0C30Y03.txt', 'L0A01L00.txt', 'L0B00Y00.txt', 'L0B00Y01.txt', 'L0B00Y02.txt', 'L0B00Y03.txt', 'L0B10Y01.txt', 'L0B10Y03.txt', 'L0B20Y02.txt', 'L0B30Y03.txt', 'L0B30Y09.txt', 'L0B40Y04.txt', 'L0B50Y11.txt', 'L0B60Y10.txt', 'M0B00Y00.txt', 'M0B00Y06.txt', 'M0B00Y07.txt', 'M0B00Y15.txt', 'M0B00Y16.txt', 'M0B00Y17.txt', 'M0B11Y18.txt', 'M0B1XY01.txt', 'M0B20Y02.txt', 'M0B21Y19.txt', 'M0B30Y03.txt', 'M0B30Y04.txt', 'M0B30Y08.txt', 'M0B40Y05.
```


## 策划参考价值
开放世界RPG类型的对话叙事参考。Bethesda开放世界RPG，海量NPC对话
