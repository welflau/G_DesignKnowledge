# Freeciv(nation) · thai

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/thai.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的thai定义

## 正文
```ruleset
[nation_thai]

translation_domain="freeciv"

name=_("Thai")
plural=_("?plural:Thai")
groups="Modern", "Early Modern", "Medieval", "Asian", "Core"
legend=_("The Thai kingdom was the only country in Southeast Asia to\
 preserve its independence through the colonial era of the 18th and\
 19th centuries CE.")

leaders = {
 "name",                "sex"
 "Rama Thibodi",        "Male"
 "Chao Phya Chakri",    "Male"
 "Maha Mongkut",        "Male"
 "Chulalongkorn",       "Male"
 "Pibul Songgram",      "Male"
 "Seni Pramoya",        "Male"
}

flag="thailand"
flag_alt = "-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""
civilwar_nations="shan", "khmer", "laotian"

cities =
 "Bangkok",
 "Thon Buri",
 "Nakhon Rachasima",
 "Chiang Mai",
 "Khon Kaen",
 "Hat Yai",
 "Chiang Rai",
 "Chumphon",
 "Hua Hin",
 "Lop Buri",
 "Lampang",
 "Phitsanulok",
 "Sawankhatok",
 "Songkhla",
 "Udon Thani",
 "Pattaya",
 "Laem Chabang",
 "Kanchanaburi",
 "Surat Thani",
 "Thammarat",
 "Phuket"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
