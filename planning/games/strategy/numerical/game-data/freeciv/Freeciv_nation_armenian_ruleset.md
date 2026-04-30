# Freeciv(nation) · armenian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/armenian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的armenian定义

## 正文
```ruleset
[nation_armenian]

name=_("Armenian")
plural=_("?plural:Armenians")
groups="Ancient", "Medieval", "Modern", "European", "Asian"
legend=_("According to legend, the Armenian people are the descendants of\
 Haik - the great-great-grandson of Noah. The modern Republic of Armenia\
 gained independence from the Soviet Union in 1991.")

leaders = {
 "name",                "sex"
 "Armenak",             "Male"
 "Ishpuinis",           "Male"
 "Tigranes II",         "Male"
 "Gregor Lusarovitch",  "Male"
 "Trdat III",           "Male"
 "Menuas",              "Male"
 "Argishtis I",         "Male"
 "Zabel I",             "Female"
}

ruler_titles = {
 "government",     "male_title",        "female_title"
 "Anarchy",        _("Usurper %s"),     _("?female:Usurper %s")
 "Fundamentalism", _("Patriarch %s"),   _("Matriarch %s")
}

flag="armenia"
flag_alt = "-"
style = "Classical"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "georgian", "assyrian", "karabakhi"

; Cities of modern Republic of Armenia only
cities =
 "Yerevan",
 "Gyumri",
 "Vanadzor",
 "Echmiadzin",
 "Hrazdan",
 "Abovyan",
 "Kapan",
 "Alaverdi",
 "Gavar",
 "Artashat",
 "Ijevan",
 "Vardenis",
 "Ararat",
 "Armavir",
 "Artik",
 "Ashtarak",
 "Charnentsavan",
 "Dilijan",
 "Goris",
 "Masis",
 "Sevan",
 "Sisian",
 "Yeghegnadzor",
 "Haghpat",
 "Sanahin",
 "Odzun",
 "Zvartnots"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
