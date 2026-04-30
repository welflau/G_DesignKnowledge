# Freeciv(nation) · malaysian

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/malaysian.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的malaysian定义

## 正文
```ruleset
[nation_malaysian]

name = _("Malaysian")
plural = _("?plural:Malaysians")
groups = "Modern", "Asian"
legend = _("Malaysia was started with the founding of Malacca (Melaka) by\
 Parameswara in the early 14th century.")

leaders = {
 "name",                "sex"
 "Parameswara",         "Male"
 "Mansur",              "Male"
 "Perak",               "Male"
 "Hang Tuah",           "Male"
 "Abdul Rahman",        "Male"
 "Abdul Razak",         "Male"
}

ruler_titles = {
 "government",      "male_title",            "female_title"
 "Fundamentalism",  _("Mullah %s"),          _("?female:Mullah %s")
 "Monarchy",        _("Paramount Ruler %s"), _("?female:Paramount Ruler %s")
}

flag = "malaysia"
flag_alt = "-"
style = "Tropical"

init_techs = ""
init_buildings = ""
init_units = ""

; Similar flags
conflicts_with = "american"
civilwar_nations = "singaporean", "indonesian", "bruneian"

cities =
 "Kuala Lumpur",
 "Putrajaya",
 "Ipoh",
 "George Town",
 "Butterworth", 
 "Muar",
 "Melaka",
 "Johor Bahru",
 "Petaling Jaya",
 "Kangar",
 "Kuala Terengganu",
 "Sungai Petani",
 "Port Dickson", 
 "Klang",
 "Alor Setar",
 "Kota Baharu",
 "Taiping",
 "Kuantan",
 "Seremban",
 "Kota Kinabalu",
 "Kuching",
 "Miri",
 "Sibu",
 "Sandakan"

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
