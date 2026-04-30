# Freeciv(nation) · djiboutian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/djiboutian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的djiboutian定义

## 正文
```ruleset
[nation_djiboutian]

name=_("Djiboutian")
plural=_("?plural:Djiboutians")
groups="Modern", "African"
legend=_("Djibouti is one of the smallest countries of Africa, located on\
 the Gulf of Aden. It has been independent from France since 1977.\
 Djibouti's main ethnic groups are the Afar and the Somalis. The country\
 has one of the hottest climates in the world.")

leaders = {
 "name",                  "sex"
 "Léonce Lagarde",        "Male"
 "Hassan Gouled Aptidon", "Male"
 "Ahmed Dini Ahmed",      "Male"
 "Ismail Omar Guelleh",   "Male"
}

ruler_titles = {
 "government",      "male_title",       "female_title"
 "Fundamentalism", _("Grand Mufti %s"), _("?female:Grand Mufti %s")
}

flag="djibouti"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "eritrean", "somali"

cities =
 "Djibouti",
 "Tadjoura",
 "Ali Sabieh",
 "Dikhil",
 "Obock",
 "Arta",
 "As Eila",
 "Balho",
 "Dorra",
 "Randa",
 "Yobocki",
 "Alaili Dadda",
 "Holhol",
 "Oueah",
 "Galafi",
 "Khor Angar",
 "Daddato",
 "Damerjog",
 "Ali Adde",
 "Balbala",
 "Loyada",
 "Chebelle",
 "Daimoli",
 "Daoudaouya",
 "Dorale",
 "Doumera",
 "Godoria",
 "Sagaliou",
 "Ras Siyyan"


```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
