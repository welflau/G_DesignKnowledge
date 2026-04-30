# Freeciv(nation) · circassian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/circassian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的circassian定义

## 正文
```ruleset
[nation_circassian]

name=_("Circassian")
plural=_("?plural:Circassians")
groups="Ancient", "Medieval", "Early Modern", "European"
; /* xgettext:no-c-format */
legend=_("The Circassians are the indigenous peoples of the Northwest\
 Caucasus. The Circassian or Adyghe language is part of the Northwest\
 Caucasian language family, related to Kabardian, Abkhaz and Ubykh. The\
 Circassians first emerged as a coherent entity some 6000 years ago. They\
 were rarely politically united; nevertheless they successfully managed to\
 resist countless invasions from great empires throughout their history.\
 Circassians were never fully subjugated in their long history until the\
 middle of the 19th century, when they were defeated and subjected to\
 genocide at the hands of the Russian Empire. Today less than 10% of the\
 Circassian population lives in their original homeland.")
leaders = {
 "name",                  "sex"
 "Inal Teghen",		  "Male"   ; a.k.a Inal Tighen or Inal the Great
 "Mansur",                "Male"   ; a.k.a Sheikh Mansur
 "Dagomuqua Berzeg",      "Male"   ; a.k.a Hadji-Ismail Dagomuqua Berzeg
 "Idar",		  "Male"   ; a.k.a Yidar
 "Temriuk",               "Male"
 "Beslan",                "Male"
 "Qanoqwe",               "Male"
 "Gwascheney",            "Female" ; a.k.a Maria  
}
flag="adygea"
flag_alt = "-"
style = "Celtic"

ruler_titles = {
 "government",      "male_title",     "female_title"
 "Despotism",       _("%s Bey"),      _("?female:%s Bey")
 "Monarchy",        _("Emir %s"),     _("Emira %s")
 "Fundamentalism",  _("Grand Mufti %s"), _("?female:Grand Mufti %s")
}

init_techs=""
init_buildings=""
init_units=""

conflicts_with="soviet"
civilwar_nations = "abkhaz", "chechen", "ossetian", "cossack", "kalmyk",
 "crimean tatar", "golden horde"

cities =
 "Myequape (hills, plains)",
 "T'uapse (hills, plains, ocean)",
 "Sindika (hills, plains, ocean)",
 "Sochi (hills, plains, ocean)",
 "Chantchir (hills, mountains, !ocean)",
 "Anapa (ocean)",
 "Nalchik (plains)",
 "Sokhumi (ocean)",
 "Gelincik (ocean)",
 "Cherkessk",
 "'atquaj (hills, mountains)",
 "Baksan (hills, plains)",
 "Dzhybge (hills, plains, ocean)",
 "Nartkale",
 "Adygekale",
 "Liesh (ocean)",
 "Psekups (river)",
 "Ashe",
 "Shepse",
 "Baslibai (hills, mountains)",
 "Braki (hills, mountains)",
 "Chegem",
 "Dusheti",
 "Psebaj",
 "Inam",
 "Dzhedzhe",
 "Kosheblehabl",
 "Leustenhabl",
 "Askelaj Kodzhe",
 "Kamennomost",
 "Hekurynehabl",
 "Krasnogvardeyske",
 "Penezhyqwaj",
 "Tehutemyqwaj",
 "Ochepshy Kodzhe"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
