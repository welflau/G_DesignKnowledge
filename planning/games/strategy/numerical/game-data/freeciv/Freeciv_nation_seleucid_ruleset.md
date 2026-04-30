# Freeciv(nation) · seleucid

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/seleucid.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的seleucid定义

## 正文
```ruleset
[nation_seleucid]

name=_("Seleucid")
plural=_("?plural:Seleucids")
groups="Asian", "Ancient"
legend=_("The Seleucid Empire was one of the diadochi states founded when\
 Alexander the Great's generals carved up his empire after his death. It\
 was named after its founder Seleucus I Nicator. Centered in Syria, the\
 Seleucids were the most powerful of the diadochi states but eventually\
 succumbed to Rome in the last century BCE.")

leaders = {
 "name",                        "sex"
 "Seleukos Nikator",            "Male"
 "Antiochos Soter",             "Male"
 "Antiochos Theos",             "Male"
 "Seleukos Kallinikos",         "Male"
 "Antiochos Megas",             "Male"
 "Antiochos Epifanes",          "Male"
 "Demetrios Nikator",           "Male"
 "Kleopatra Thea",              "Female"
 "Antiochos Grypos",            "Male"
 "Filippos Filoromaios",        "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Anarchy",         _("Usurper %s"),   _("?female:Usurper %s")
 "Despotism",       _("Satrap %s"),    _("?female:Satrap %s")
}

flag="seleucid"
flag_alt = "-"
style = "Classical"


init_techs=""
init_buildings=""
init_units=""

conflicts_with = "persian", "syrian", "israeli"
civilwar_nations = "parthian", "aramean", "israelite"

cities =
 "Seleukeia",
 "Antiocheia",
 "Laodikeia",
 "Damaskos",
 "Ierousalem",
 "Tyros",
 "Karrai",
 "Arbela",
 "Babylona",
 "Sousa",
 "Ekbatana",
 "Persepoli",
 "Harmoseia",
 "Artikaudna",
 "Antiocheia tes Margianes",
 "Baktra",
 "Marakanda",
 "Alexandreia Eschate",
 "Edessa",
 "Alexandreia Arachoseia",
 "Kaboura",
 "Gaza",
 "Sardes",
 "Hekatompylos",
 "Alexandreia Asiana",
 "Apameia",
 "Ephesos",
 "Patara",
 "Iasos",
 "Alexandreia Bukefalous",
 "Side",
 "Erythrai",
 "Magneseia",
 "Makedonopoli",
 "Abydos",
 "Kyzikos"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
