# Freeciv(nation) · srivijaya

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/srivijaya.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的srivijaya定义

## 正文
```ruleset
[nation_srivijaya]

name=_("Sri Vijaya")
plural=_("?plural:Sri Vijaya")
groups="Asian", "Medieval"

legend=_("Sri Vijaya was an empire centered on Palembang in eastern\
 Sumatra and extended its control through much of the coastal regions of\
 Sumatra, Java, Borneo and the Malay peninsula. It was founded sometime in\
 the 3rd century CE and lasted until roughly 1400, falling first to Jambi,\
 then to Singhasari and other regional powers, including the South Indian\
 Chola dynasty.")

leaders = {
 "name",                "sex"
 "Balaputra",           "Male"
 "Pramodavardhani",     "Female"
 "Samaratungga",        "Male"
 "Dharmasetu",          "Male"
 "Jayanasa",            "Male"
}

ruler_titles = {
 "government",      "male_title",        "female_title"
 "Despotism",       _("Raja %s"),        _("Rani %s")
 "Monarchy",        _("Maharaja %s"),    _("Maharani %s")
}

flag         = "srivijaya"
flag_alt     = "-"
style        = "Tropical"

init_techs=""
init_buildings=""
init_units=""

civilwar_nations="Majapahit", "indonesian", "malaysian"

cities =
 "Palembang",
 "Muara Jambi",
 "Kedah",
 "Tarumanagara",
 "Batam",
 "Lubuklinggau",
 "Pagar Alam",
 "Bandar Lampung",
 "Prabumulih",
 "Pangkalpinang",
 "Sungailiat",
 "Muntok",
 "Toboali",
 "Koba",
 "Belinyu",
 "Sungai Penuh",
 "Metro",
 "Pekanbaru",
 "Dumai",
 "Bengkalis",
 "Tanjung Balai Karimun",
 "Tanjung Pinang",
 "Daik",
 "Ranai"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
