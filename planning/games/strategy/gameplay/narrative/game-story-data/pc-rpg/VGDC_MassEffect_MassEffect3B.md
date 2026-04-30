# 质量效应 · MassEffect3B（对话语料）

> 来源：seannyD/VideoGameDialogueCorpusPublic
> 原始链接：https://github.com/seannyD/VideoGameDialogueCorpusPublic
> 分类：gameplay
> 标签：质量效应, 科幻RPG, 对话语料, PC RPG, 角色对话
> 游戏类型：科幻RPG

## 概述
质量效应系列《MassEffect3B》的对话语料数据（角色列表+对话统计+数据来源）

## 正文
## 游戏信息

- **系列**：质量效应（MassEffect）
- **游戏**：MassEffect3B
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
  "source": "http://mod.gib.me/masseffect3/testdump2.txt",
  "parserParameters": {
    "parser": "MassEffect3GibbedParser",
    "fileType": "testdump2.txt"
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
    "CHECK.[bioa_cat002_050shuttle_loc_int.cat002_shuttle_ride_m_d.1": "Liara T'soni",
    "CHECK.bioa_cat002_050shuttle_loc_int.gthn7a_shuttle_down_m_D.1": "Admiral Xen",
    "CHECK.biod_citsam_500cell_loc_int.citsam_logs_dead_commando_a_D.1": "Tashya Porae",
    "CHECK.biod_nor_110tour_loc_int.norpro_tour_m_D.1": "Samantha Traynor",
    "CHECK.biod_kro001_90openingconvo_loc_int.kro001_base_intro_m_D.1": "Padok Wiks",
    "CHECK.biod_cat002_100intro_loc_int.cat002_soldier_m_d.1": "Lieutenant Kurin",
    "CHECK.biod_nor_204gth001_intro_loc_int.norgth_campaign_intro_m_D.1": "Admiral Shala'Raan vas Tonbay",
    "CHECK.biod_omgjck_340orionconvo_loc_int.omgjck_meet_student_m_d.1": "Ensign Prangley",
    "CHECK.bioa_cithub_presidium_global_loc_int.citprs_news_ann_a_D.1": "Iris Dunnigan",
    "CHECK.biod_cithub_embassy_loc_int.citprs_news_ann_a_D.1": "Iris Dunnigan",
    "CHECK.bioa_gthn7a_000leveltrans_loc_int.gthn7a_shuttle_down_m_D.1": "Admiral Xen",
    "CHECK.biod_citsam_700entryway_loc_int.citsam_logs_matriarch_a_D.1": "Gallae",
    "CHECK.biod_gthn7a_430end_loc_int.gthn7a_rescue_endings_v_D.1": "Admiral Zaal'Koris",
    "CHECK.biod_kro001_100landingarea_loc_int.kro001_elevator_m_D.1": "Senior Research Director Wiks",
    "CHECK.biod_kron7a_050start_loc_int.kron7a_level01_v_D.1": "Lieutenant Tarquin Victus",
    "CHECK.biod_gth002_100landingzone_loc_int.gth002_radioreact0_a_D.1": "Admiral Han'Gerrel",
    "CHECK.biod_gth002_300chase_loc_int.gth002_turret_askhelp_a_D.1": "Admiral Han'Gerrel",
    "CHECK.biod_krogar_500gate_loc_int.krogar_after_the_bigbrute_m_D.1": "Corinthus",
    "CHECK.biod_nor_204bhackett_loc_int.norcer_jcb_wrap_vid_v_D.1": "Admiral Hackett",
    "citsam_falere": "Falere",
    "Jeff \"Joker\" Moreau": "Joker"
  }
}
```

### 角色列表（共672个）

- "STATUS" :13554,
- "Shepard" :12089,
- "GOTO" :11590,
- "CHOICE" :5158,
- "ACTION" :1547,
- "LOCATION" :1547,
- "Liara T'soni" :1239,
- "EDI" :1227,
- "James Vega" :1213,
- "Garrus Vakarian" :1191,
- "Javik" :985,
- "Ashley Williams" :820,
- "Tali'Zorah" :792,
- "Kaidan Alenko" :763,
- "hench_garrus" :725,
- "hench_liara" :705,
- "hench_edi" :467,
- "global_salarian_alt" :451,
- "hench_kaidan" :424,
- "hench_ashley" :420,
- "Urdnot Wreav" :402,
- "hench_tali" :397,
- "hench_marine" :381,
- "global_zaeed" :344,
- "Urdnot Wrex" :330,
- "Mordin Solus" :325,
- "global_hackett" :319,
- "global_legion" :280,
- "nor_comm" :273,
- "cit_background_male" :270,
- "global_anderson" :264,
- "cit_background_female" :264,
- "global_joker" :259,
- "CHECK.biosimpledlgcontainer_horde_loc_int.ss_mp_horde_narr_v1_D.1" :184,
- "npc_anderson" :183,
- "global_reporter" :168,
- "global_turian_leader" :156,
- "Joker" :139,
- "global_krogan_female" :138,
- "nor_chakwas" :136,
- "nor_pilot" :135,
- "global_miranda" :130,
- "global_illusive_man" :129,
- "global_admiral" :120,
- "global_avina" :116,
- "global_mordin" :115,
- "nor_adams" :112,
- "global_wrex" :109,
- "global_jack" :105,
- "radio_wrex" :103,
- ... 共672个角色

### 对话统计 (stats.csv)

```csv
folder,alternativeMeasure,game,series,group,lines,words,sentences,syllables,FleschKincaidReadability,FleschReadability,DaleChallReadability,numCharacters
../data/MassEffect/MassEffect3B/,True,Mass Effect 3,Mass Effect,TOTAL,34248,295819,80006,375397,0.8263167365004431,95.72390889114416,7.197979036890899,667
../data/MassEffect/MassEffect3B/,True,Mass Effect 3,Mass Effect,male,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffect3B/,True,Mass Effect 3,Mass Effect,female,0,NA,NA,NA,NA,NA,NA,0
../data/MassEffect/MassEffect3B/,True,Mass Effect 3,Mass Effect,neutral,0,NA,NA,NA,NA,NA,NA,0

```


### 数据来源脚本 (scraper.py)

```python
from urllib.request import *
import codecs, time, os.path

pages = [
 ("https://mod.gib.me/masseffect3/testdump2.txt","testdump2.txt"),
 ("https://pastebin.com/raw/eVZPgnb2", "bools.txt"),
 ("https://mod.gib.me/masseffect3/conditionals.txt", "conditionals.txt"),
 ("https://pastebin.com/raw/eqiNW7rE","plotDatabase.txt")]

for page,fn in pages:
	fileName = "raw/"+fn
	if not os.path.isfile(fileName):
		req = Request(
			page, 
			data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			}
		)

		html = urlopen(req).read()#.decode('cp1252').encode('utf-8')#.decode('ISO-8859-1')
		o = open(fileName,'wb')
		o.write(html)
		o.close()
		time.sleep(3)
	#with codecs.open(fileName, "w", "utf-8") as targetFile:
	#	targetFile.write(html)

```


## 策划参考价值
科幻RPG类型的对话叙事参考。BioWare科幻RPG，跨三部曲选择延续
