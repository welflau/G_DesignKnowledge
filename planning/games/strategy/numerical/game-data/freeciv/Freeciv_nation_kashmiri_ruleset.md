# Freeciv(nation) · kashmiri

> 来源：longturn/freeciv21
> 原始链接：https://github.com/longturn/freeciv21/blob/main/data/nation/kashmiri.ruleset
> 分类：numerical
> 标签：文明, 4X策略, 规则集, nation

## 概述
Freeciv nation规则集的kashmiri定义

## 正文
```ruleset
[nation_kashmiri]

name=_("Kashmiri")
plural=_("?plural:Kashmiris")
groups="Medieval", "Early Modern", "Asian"
legend=_("The Kashmir valley is situated by the western foothills of the\
 Himalayas. Having been inhabited for millennia, it is a melting pot of\
 Hindu, Tibetan, and Islamic culture.")

leaders = {
 "name",            "sex"
 "Gulab Singh",     "Male"
 "Zain-ul-Abidin",  "Male"
 "Shah Mir Swati",  "Male"
 "Kota",            "Female"
 "Didda",           "Female"
 "Sugandha",        "Female"
 "Lalitaditya",     "Male"
}

ruler_titles = {
 "government",      "male_title",      "female_title"
 "Despotism",       _("Raja %s"),      _("Rani %s")
 "Monarchy",        _("Maharaja %s"),  _("Maharani %s")
}

flag="kashmir"
flag_alt="-"
style = "Asian"

init_techs=""
init_buildings=""
init_units=""

conflicts_with="Indian", "Pakistani"
civilwar_nations="Sikh", "Mughal"

cities=
 "Rajapura", ; ancient capital
; Kashmir valley
 "Srinagar",
 "Anamtnag", ; Anantnag
 "Baramulla",
 "Awantipora",
 "Pahalgam",
 "Sonamarg",
 "Sopore",
 "Uri",
 "Gaoran",
 "Hera Ahlan",
 "Kupwara",
; Azad Kashmir
 "Udabhanda", ; Muzaffarabad
 "Kotli",
 "Mirpur",
 "Bhimber",
 "Keran",
 "Kel",
 "Rawalakot",
; Jammu
 "Jammu",
 "Akhnoor",
 "Rajouri",
 "Doda",
 "Udhampur",
 "Balhar",
 "Dumare",
 "Kishtwar",
 "Nagrota",
 "Kaluchak",
 "Samba",
 "Poonch",
 "Kathua"
 

```

## 策划参考价值
4X SLG鼻祖级数值参考：单位/建筑/科技树/文明特性。
