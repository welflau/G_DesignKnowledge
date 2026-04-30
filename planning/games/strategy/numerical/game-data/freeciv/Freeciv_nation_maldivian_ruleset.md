# Freeciv(nation) · maldivian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/maldivian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的maldivian定义

## 正文
```ruleset
[nation_maldivian]

name=_("Maldivian")
plural=_("?plural:Maldivians")
groups="Medieval", "Early Modern", "Modern", "Asian"
legend=_("The Maldives are an archipelago in the Indian Ocean and the\
 smallest country of Asia. According to tradition, the Maldives became\
 a united sultanate when the Cholas were expelled in the 12th century.\
 The islands were a British protectorate from 1887 to 1965. The monarchy\
 was abolished three years after independence. Today, the Maldives are\
 above all known as a tourist destination.")

leaders = {
 "name",                           "sex"
 "Damahaar",                       "Female"
 "Koimala",                        "Male"
 "Dhovemi",                        "Male"
 "Khadeejah",                      "Female"
 "Hassan I",                       "Male"
 "Muhammad Thakurufaanu Al Auzam", "Male"
 "Muhammad Imaduddin I",           "Male"
 "Muhammed Ghiya'as ud-din",       "Male"
 "Muhammad Shamsuddeen III",       "Male"
 "Mohamed Amin Didi",              "Male"
 "Muhammad Fareed Didi",           "Male"
 "Maumoon Abdul Gayoom",           "Male"
}

ruler_titles = {
 "government",      "male_title",  "female_title"
 "Fundamentalism", _("Caliph %s"), _("Calipha %s")
 "Monarchy",       _("Sultan %s"), _("Sultana %s")
}

flag="maldives"
flag_alt = "-"
style = "Babylonian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations = "lankese" ;suvadive

cities =
 "Malé",
 "Hithadhoo",
 "Naifaru",
 "Kulhudhuffushi",
 "Maafushi",
 "Gamu",
 "Thinadhoo",
 "Kudahuvadhoo",
 "Fuvahmulah",
 "Villigili",
 "Eydhafushi",
 "Dhiddhoo",
 "Milandhoo",
 "Mahibadhoo",
 "Fonadhoo",
 "Nilandhoo",
 "Manadhoo",
 "Ugoofaaru",
 "Veymandoo",
 "Rasdhoo",
 "Muli",
 "Felidhoo",
 "Hinnavaru",
 "Ihavandhoo",
 "Feydhoo",
 "Hoarafushi",
 "Alifushi",
 "Maradhoo",
 "Hulhudhuffaaru",
 "Meedhoo",
 "Kaashidhoo",
 "Maamigili",
 "Buruni",
 "Thulhaadhoo",
 "Velidhoo",
 "Isdhoo",
 "Maduvvari",
 "Nolhivaramu",
 "Holhudhoo",
 "Maavah",
 "Thulusdhoo",
 "Meedhoo",
 "Hanimaadhoo",
 "Fares",
 "Gadhdhoo"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
