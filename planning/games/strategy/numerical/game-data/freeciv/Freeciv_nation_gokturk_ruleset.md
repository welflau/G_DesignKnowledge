# Freeciv(nation) · gokturk

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/gokturk.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的gokturk定义

## 正文
```ruleset
[nation_gokturk]

name=_("Göktürk")
; pre-2.6 had plain ASCII names
rule_name="Gokturk"
plural=_("?plural:Göktürks")
groups="Medieval", "Asian"
legend=_("The Göktürk or Old Turkic Khaganate was ruled by the Ashina dynasty\
 which derived its legendary origins from the red she-wolf. The Göktürks\
 were ancestors of the modern Turkic nations in Asia and Eastern Europe.\
 They were the creators of a vast military empire, which covered the\
 steppe areas from the Kuban river in the West to Korea in the East.")

leaders = {
 "name",        "sex"
 "Asena",       "Male" ;legendary son of red she-wolf
 "Bumin",       "Male"
 "Issik",       "Male"
 "Muqan",       "Male"
 "Taspar",      "Male"
 "Ishbara",     "Male"
 "Bagha",       "Male"
 "Istami",      "Male"
 "Tardush",     "Male"
 "Heshana",     "Male"
 "Böri",        "Male"
 "Shibir",      "Male"
 "Ilterish",    "Male"
 "Qapaghan",    "Male"
 "Bilge",       "Male"
 "Tengri",      "Male"
 "Irterish",    "Male"
 "Ozmish",      "Male"
 "Kul Tigin",   "Male"
 "Tonyukuk",    "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("%s Khan"),         _("%s Khatan")
 "Monarchy",        _("%s Khagan"),       _("?female:%s Khagan")
 "Fundamentalism",  _("Great Shaman %s"), _("?female:Great Shaman %s")
}

flag = "gokturk"
flag_alt = "-"
style = "asian"

init_techs=""
init_buildings=""
init_units=""
conflicts_with = "kazakh", "uzbek", "kyrgyz", "uyghur", "khazar", "turkmen", "tatar", "crimean tatar", "turkish", "ottoman"
civilwar_nations = "tocharian", "khazar", "uyghur", "avar"

; City names come from en.wikipedia and book Drevniye Tiurki by L. Gumilov

cities =
"Suyab",	; principal capital of Western Turkic Khaganate
"Navekat",	; summer capital of Western Turkic Khaganate
"Ashite",	; Old Turkic aristocratic tribe
"Sir",		; main house of Siejento tribe
"Semerkand",
"Merv",
"Chach",	;Tashkent
"Qanqlis",
"Khalkha",
"Hohhot",
"Tulu",
"Nushipi",
"Karluk",
"Turgesh",
"Ili",
"Shutun",
"Hochen",
"Karaşar",
"Nesef",
"Derbent",
"Chik",
"Tuyuk",
"Alashan",
"Yaglakar",
"Bayirku",
"Tongra",
"Bishbalyk",
"Bukhara",
"Paykend",
"Badgis",
"Balkh",
"Kashgar",
"Kucha",
"Turfan",
"Fergana",
"Maymurg",
"Kesh",
"Usrushana"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
