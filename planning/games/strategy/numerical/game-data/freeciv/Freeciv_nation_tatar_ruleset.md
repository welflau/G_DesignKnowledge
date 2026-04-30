# Freeciv(nation) · tatar

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/tatar.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的tatar定义

## 正文
```ruleset
[nation_tatar]

name=_("Tatar")
plural=_("?plural:Tatars")
groups="Medieval", "Early Modern", "Asian", "European"

legend=_("The Tatars are a Turkic-speaking nation. Various Tatar states\
 existed in the Middle Ages: Kazan, Crimea, Astrakhan, Sibir and other\
 khanates. Nowadays Tatars live in many places in the former USSR. They\
 have their own republic called Tatarstan in the Russian Federation and\
 the Autonomous Republic of Crimea in Ukraine.")

leaders = {
 "name",                "sex"
 "Küçem",               "Male" ; Sibirian khan
 "Tuqtamış",            "Male" ; Sibirian khan
 "Oluğ Mөxәmmәt",       "Male" ; Kazan khan
 "Qasim II",            "Male" ; Astrakhan khan
 "Haci I Giray",        "Male" ; Crimean khan
 "Devlet I Giray",      "Male" ; Crimean khan
 "Qasim",               "Male" ; Kasimov khan (vassal of russian tsar)
 "Sadri Maksudi Arsal", "Male" ; Leader of Idel-Ural State
 "Mintimer Shaymiev",   "Male"
}

ruler_titles = {
 "government",      "male_title",         "female_title"
 "Despotism",       _("%s Khan"),         _("%s Khatan")
 "Monarchy",        _("%s Khagan"),       _("?female:%s Khagan")
 "Fundamentalism",  _("Grand Mufti %s"),  _("?female:Grand Mufti %s")
}

flag="tatarstan"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""


civilwar_nations = "Ukrainian", "Mongol", "Turkish", "Crimean Tatar"

cities = ;transliteration of Yanalif here: ө > e, ə > e, ğ > g, ı > i, ş > sh, ç > ch
"Qazan", ;Kazan, capital of Kazan khanate
"Xacitarxan", ;capital of Astrakhan khanate
"Bakhchisaray", ;capital of Crimea khanate
"Qashliq", ;capital of Sibirian khanate
"Tumun", ;old capital of Sibirian khanate
"Kasimov", ;capital of Kasimov khanate
"Kezlev", ;names of towns of Crimean, Kazan and Kasimov khanates
"Archa",
"Kefe",
"Qashan",
"Aqmescit",
"Cuketaw",
"Qarasuvbazar",
"Chali",
"Baliqlava",
"Alat",
"Sudaq",
"Churi",
"Kerich",
"Ermish",
"Arabat",
"Kadom",
"Azov",
"Qirim",
"Chufut Qale",
"Saq",
"Aqyar",
"Yar Chally", ;tatarian names of modern Tatarstan cities and towns
"Tuben Kama",
"Elmet",
"Zelenodol",
"Bogelme",
"Alabuga",
"Chistay",
"Zey",
"Aznaqay",
"Norlat",
"Buwa",
"Egerce",
"Mamadish",
"Minzele",
"Celil",
"Uryssu",
"Hafuz", ;tatarian names of modern Crimea towns
"Sarabuz",
"Buyuk Onlar",
"Alupka",
"Aqmechit",
"Ermeni Bazar",
"Tuymazy" ;Bashkortostan town with big tatarian population


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
