# Freeciv(nation) · cambodian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/cambodian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的cambodian定义

## 正文
```ruleset
[nation_cambodian]

name=_("Cambodian")
plural=_("?plural:Cambodians")
groups="Modern", "Asian"
legend=_("Kampuchea (known in English as Cambodia) is the modern successor\
 state of the mighty Khmer Empire, which ruled most of the Indochinese\
 Peninsula between the 11th\
 and 14th centuries.")

leaders = {
 "name",                "sex"
 "Pol Pot",             "Male"
 "Norodom Sihanouk",    "Male"
 "Ang Chan",            "Male"
 "Jayavarman II",       "Male"
}

flag="kampuchea"
flag_alt = "-"
style = "Asian"

ruler_titles = {
 "government",      "male_title",           "female_title"
 "Communism",       _("Brother %s"),        _("Sister %s")
}

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="thai", "vietnamese"

cities =
 "Phnom Penh",
 "Angkor Thom",
 "Battambang",
 "Angkor Wat",
 "Siem Reap",
 "Takeo",
 "Kompong Speu",
 "Prey Veng",
 "Sisophon",
 "Pailin",
 "Kampot",
 "Kep",
 "Stung Treng",
 "Banlung",
 "Cheom Ksan",
 "Pursat",
 "Kompong Chhnang",
 "Kompong Thum",
 "Svay Rieng",
 "Kompong Cham",
 "Kratie",
 "Sen Monorom",
 "Kompong Luong",
 "Udong",
 "Veal Renh",
 "Banam",
 "Siem Pang",
 "Koulen",
 "Krong Koh Kong",
 "Samrong",
 "Phnom Thbeng Meanchey",
 "Kaopong Sralao",
 "Phsar Oudong",
 "Boung Long",
 "Lomphat",
 "Snuol",
 "Sre Khtum",
 "Moung",
 "Kralanh",
 "Lomphat",
 "Rovieng",
 "Koulen"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
