# Freeciv(nation) · cretan

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/cretan.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的cretan定义

## 正文
```ruleset
[nation_cretan]

name=_("Cretan")
plural=_("?plural:Cretans")
groups="European"
legend=_("Crete is an island in the Mediterranean Sea, the largest of the\
 Greek Archipelago. In the 3rd and 2nd millennia BCE Crete was the site of\
 Europe's first advanced civilization, the Minoan culture. An eruption of\
 nearby Thera destroyed the Minoan civilization. Crete then became part of\
 the Greek cultural realm, and was subsequently conquered by the Romans,\
 Arabs, Byzantines, Venetians and Ottoman Turks. After having been a\
 semi-independent state for 15 years, Crete finally became part of Greece\
 in 1913.")

leaders = {
 "name",                   "sex"
 "Europa",                 "Female"
 "Epimenides",             "Male" ; All Cretans are liars
 "Abou Chafes",            "Male"
 "Daskalogiannis",         "Male"
 "Eleutherios Venizelos",  "Male"
 "Georgios Psychoundakis", "Male"
}

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Despotism",       _("Despot %s"),         _("?female:Despot %s")
 "Fundamentalism",  _("Patriarch %s"),      _("Matriarch %s")
}

flag="crete"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Hellenic", "Cypriot"

cities =
 "Chania",
 "Irakleion",
 "Gortyn",
 "Rethymnon",
 "Lasithi",
 "Ierapetra",
 "Lyttos",
 "Agios Nikolaos",
 "Moirai",
 "Sitia",
 "Nea Alikarnassos",
 "Kissamos",
 "Arkalochorion",
 "Timbakion",
 "Souda",
 "Gazion",
 "Palaikastron",
 "Daratsos",
 "Panormos",
 "Kounoupidiana",
 "Mournies",
 "Anogia",
 "Neapolis",
 "Epano Archanai",
 "Nerokouros",
 "Perama",
 "Schisma",
 "Malia",
 "Kounoupidiana",
 "Zoniana",
 "Kritsa",
 "Limin Chersonisou",
 "Perivolia",
 "Livadia",
 "Gra Ligia",
 "Krouson",
 "Palaiochora",
 "Atsipopoulon",
 "Kato Chorion",
 "Zaros",
 "Galatas",
 "Agia Galini",
 "Nea Anatoli",
 "Agia Varvara",
 "Vamvakopoulon",
 "Kentrion",
 "Kastellion",
 "Sfakia"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
